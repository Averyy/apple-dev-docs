# Accessing provisioned secrets with identifiers

**Framework**: Managedapp

Specify the secrets your app requires for device management features, receive secrets from MDM servers and use secrets in your app.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- visionOS 2.4+

#### Overview

Some device management features rely on , that is, secure credentials provisioned by an administrator (MDM admin) for your app, such as passwords, certificates, and identities. Secrets can support:

- Automatically logging in a person
- Cryptographic signing
- Certificate pinning to improve trust evaluation of servers and signatures

Your app accesses secrets by their identifier using the framework supplied secret  classes. Each provider offers a list of identifiers that catalogs all the currently available secrets, of a particular type, that an MDM admin provisions. You can access secrets using predefined identifiers, or identifiers that you add to your app’s configuration.

The provider’s list of identifiers is an [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence). If your app requires notification when the available secrets change, or if your app supports dynamic lists of secrets, iterate the sequence for the lifetime of the app using `for await`.

#### Specify the Secrets Your App Supports

To implement features with secrets, identify the provisions that you require from MDM admins. Publish a specification that details the requirements in a location accessible to MDM admins; for example, hosting it on your app website.

> **Note**: If your app also defines a configuration specification for general information, you can add your secrets requirements to the same document. For more information about general configuration, see [`Specifying and decoding a configuration`](specifying-and-decoding-a-configuration.md).

When an admin provisions secrets on their MDM server according to your specification, they use [`Device Management`](https://developer.apple.com/documentation/DeviceManagement). The device’s operating system works with [`Device Management`](https://developer.apple.com/documentation/DeviceManagement) to ingest the secrets on the device. From the perspective of your app, [`ManagedApp`](ManagedApp.md) receives the secrets automatically.

#### Retrieve Secrets Using a Known Identifier

The framework defines a provider class for each type of secret:

- [`ManagedAppPasswordsProvider`](managedapppasswordsprovider.md)
- [`ManagedAppCertificatesProvider`](managedappcertificatesprovider.md)
- [`ManagedAppIdentitiesProvider`](managedappidentitiesprovider.md)

A provider contains:

- An accessor that returns secrets by ID
- A list of identifiers that contains all of the currently available secrets

The following code acquires a password using the [`password(withIdentifier:)`](managedapppasswordsprovider/password(withidentifier:).md) accessor with a predefined identifier:

```swift
let loginPasswordIdentifier = "mainLoginPassword"
let loginPassword: String?
do { /* Attempt to look up the login password. */
    loginPassword = try await passwordsProvider.password(
        withIdentifier: loginPasswordIdentifier)
} catch {
    // Handle the password-lookup error.
    loginPassword = nil
}
// Use the password.
```

Another task that often uses known identifiers is responding to client certificate authentication challenges. The following example responds to a client certificate challenge within the [`URLSessionDelegate`](https://developer.apple.com/documentation/Foundation/URLSessionDelegate) callback, and requests an identity using the [`ManagedAppIdentitiesProvider`](managedappidentitiesprovider.md) accessor:

```swift
public func urlSession(_ session: URLSession, 
            didReceive challenge: URLAuthenticationChallenge) 
                async -> (URLSession.AuthChallengeDisposition, 
                          URLCredential?) {
    switch challenge.protectionSpace.authenticationMethod {
    case NSURLAuthenticationMethodClientCertificate:
        // Look up the identity. 
        guard let identity = try? await identitiesProvider.identity(
                withIdentifier: identityIdentifier) else {
            return (.cancelAuthenticationChallenge, nil)
        }
        // Use the identity to authenticate.
        return (.useCredential, URLCredential(identity: identity, 
                                          certificates: nil, 
                                           persistence: .forSession))
    case NSURLAuthenticationMethodServerTrust:
        // Perform server trust evaluation.
        break;
    default:
        return (.performDefaultHandling, nil)
    }
}
```

> ❗ **Important**: For security reasons, only request a secret from the framework when your app needs it immediately. This minimizes the amount of time that the secret is in your app’s memory. Avoid logging sensitive information such as passwords or private-key data.

#### Retrieve Secrets Using the Providers Identifiers Sequence

If your app needs a notification when the available secrets change, or if your app maintains dynamic lists of secrets, use the provider’s [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence).  Use a `for await` construct on the provider’s `identifiers` property to listen for changes. The following example builds a list of available usernames by iterating the  [`ManagedAppIdentitiesProvider`](managedappidentitiesprovider.md) sequence:

```swift
let accountUsernameIdentifierPrefix = "User:"
Task {
    var accountUsernames: [String] = []
    let identitiesProvider = ManagedAppIdentitiesProvider()
    for await identityIdentifiers in await identitiesProvider.identifiers {
        accountUsernames = identityIdentifiers.filter { 
            $0.hasPrefix(accountUsernameIdentifierPrefix) 
        }.map { String($0.dropFirst(accountUsernameIdentifierPrefix.count)) }
        // Update the UI to list the available accounts.
    }
}
```

> **Note**: Instead of predefining identifiers, you can add identifiers to your configuration specification so the identifiers are flexible and MDM admins can configure them. For more information, see [`Specifying and decoding a configuration`](specifying-and-decoding-a-configuration.md).

#### Access an Identity for Authentication or Signing

To log someone in, an app needs to authenticate with a server. To acquire the person’s identity to authenticate, pass the person’s username as the identifier argument of the identity provider’s accessor, for example:

```swift
@ObservationIgnored let idsProvider = ManagedAppIdentitiesProvider()
let identityID = selectedUsername
...
let identity: SecIdentity
do { /* Access the identity. */
    identity = try await idsProvider.identity( 
        withIdentifier: identityID)
} catch {
    // Handle identity-lookup error.
}
```

Alternatively, your app can use the identity for cryptographic signing. Because [`SecIdentity`](https://developer.apple.com/documentation/Security/SecIdentity) is in the [`Security`](https://developer.apple.com/documentation/Security) framework, you can create a cryptographic signature using other [`Security`](https://developer.apple.com/documentation/Security) framework API. The following code begins a signature by acquiring a reference to the identity’s private key:

```swift
// Access the private key. 
var privateKey: SecKey? = nil
SecIdentityCopyPrivateKey(identity, &privateKey)
```

The [`SecKey`](https://developer.apple.com/documentation/Security/SecKey) object is an opaque reference to the underlying private key data that’s in system memory. Don’t load actual private key data in your app’s memory unless absolutely necessary; for example, when using the  [`SecKeyCopyExternalRepresentation(_:_:)`](https://developer.apple.com/documentation/Security/SecKeyCopyExternalRepresentation(_:_:)) function.

While choosing the signing algorithm, call [`SecKeyIsAlgorithmSupported(_:_:_:)`](https://developer.apple.com/documentation/Security/SecKeyIsAlgorithmSupported(_:_:_:)) to ensure the admin-provisioned key supports the algorithm:

```swift
// Choose signing algorithm. 
let algorithm: SecKeyAlgorithm = isRSAKey(secKey: privateKey) ? .rsaSignatureMessagePKCS1v15SHA256 : .ecdsaSignatureMessageX962SHA256
guard SecKeyIsAlgorithmSupported(privateKey, .sign, algorithm) else {
    // Handle incompatible algorithm.
    return
}
```

To facilitate compatibility, document the algorithms and associated key types your app supports in your specification.

Finally, create the signature:

```swift
// Perform the signing operation.
let message = Data("This is a secret message.".utf8) 
let signature = SecKeyCreateSignature(privateKey, algorithm, message as CFData, &error)
// Use the signature.
```

## See Also

- [class ManagedAppCertificatesProvider](managedappcertificatesprovider.md)
  A class that provides certificates that an MDM admin provisions for a managed app or extension.
- [class ManagedAppIdentitiesProvider](managedappidentitiesprovider.md)
  A class that provides identities that an MDM admin provisions for a managed app or extension.
- [class ManagedAppPasswordsProvider](managedapppasswordsprovider.md)
  A class that provides passwords that an MDM admin provisions for a managed app or extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ManagedApp/accessing-provisioned-secrets-with-identifiers)*