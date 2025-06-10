# Establishing your app’s integrity

**Framework**: DeviceCheck

Ensure that requests your server receives come from legitimate instances of your app.

#### Overview

You can’t rely on your app’s logic to perform security checks on itself because a compromised app can falsify the results. Instead, you use the [`shared`](dcappattestservice/shared.md) instance of the [`DCAppAttestService`](dcappattestservice.md) class in your app to create a hardware-based, cryptographic key that uses Apple servers to certify that the key belongs to a valid instance of your app. Then you use the service to cryptographically sign server requests using the certified key. Your app uses these measures to assert its legitimacy with any server requests for sensitive or premium content.

![A diagram showing that your app receives challenges from your server and responds with an attestation and assertions, while relying on the App Attest logic.](https://docs-assets.developer.apple.com/published/2b7a2d8c173ccb7e4e7f4c52f5a21925/establishing_your_app_s_integrity-1%402x.png)

This article describes how to modify your app to use the App Attest service. For a description of the complementary logic that you add to your server, see [`Validating apps that connect to your server`](validating-apps-that-connect-to-your-server.md).

> **Note**: To use the App Attest service, your app must have an App ID that you register on the [`Apple Developer`](https://developer.apple.comhttps://developer.apple.com/account/) website.

##### Check for Availability

Not all devices can use the App Attest service, so it’s important to have your app run a compatibility check before accessing the service. If the user’s app doesn’t pass the compatibility check, gracefully bypass the service. You check for availability by reading the [`isSupported`](dcappattestservice/issupported.md) property.

```swift
let service = DCAppAttestService.shared
if service.isSupported {
    // Perform key generation and attestation.
}
// Continue with server access.
```

You change the behavior of both your app, as the example above shows, and your server — which can no longer require assertions — when you find that the device doesn’t support the service.

> ❗ **Important**: Most app extensions don’t support App Attest. Generally, when executing code in these extensions, bypass key generation and attestation, even if the [`isSupported`](dcappattestservice/issupported.md) method property is [`true`](https://developer.apple.com/documentation/swift/true). The only app extensions that support App Attest are watchOS extensions in watchOS 9 or later. For these extensions, you can use the results from [`isSupported`](dcappattestservice/issupported.md) to indicate whether your WatchKit extension bypasses attestation.

##### Create a Key Pair

For each user account on each device running your app, generate a unique, hardware-based, cryptographic key pair by calling the [`generateKey(completionHandler:)`](dcappattestservice/generatekey(completionhandler:).md) method.

```swift
service.generateKey { keyId, error in
    guard error == nil else { /* Handle the error. */ }

    // Cache keyId for subsequent operations.
}
```

On success, the method’s completion handler returns a key identifier that you use later to access the key. Record the identifier in persistent storage — for example, by writing it to a file — because there’s no way to use the key without the identifier, and no way to get the identifier later. The device automatically stores the associated private key in the Secure Enclave, from where the App Attest service can use it to create signatures, but from where no process can ever directly read or modify it, ensuring its security.

> ❗ **Important**: If you create a key pair in an App Clip, use the same key pair in the corresponding app. To support this, be sure to store the identifier in a shared container accessible from your full app. For more information about sharing data between your App Clip and your full app, see [`Sharing data between your App Clip and your full app`](https://developer.apple.com/documentation/AppClip/sharing-data-between-your-app-clip-and-your-full-app).

Don’t reuse a key among multiple users on a device because this weakens security protections. In particular, it becomes hard to detect an attack that uses a single compromised device to serve multiple remote users running a compromised version of your app. For more information, see [`Assessing fraud risk`](assessing-fraud-risk.md).

##### Certify the Key Pairs As Valid

Before using a key pair, ask Apple to attest to its origin on Apple hardware running an uncompromised version of your app. Because you can’t trust your app’s logic to verify the attestation result, you send the result to your server. To reduce the risk of replay attacks during this procedure, attestation embeds the hash of a unique, one-time challenge from your server. You can create a suitable value using the [`SHA256`](https://developer.apple.com/documentation/CryptoKit/SHA256) implementation in CryptoKit. The challenge should be at least 16 bytes in length to ensure sufficient entropy to ensure guessing them is infeasible.

```swift
import CryptoKit

let challenge = <# Data from your server. #>
let hash = Data(SHA256.hash(data: challenge))
```

Using the hash, along with the key pair you create in the previous section, call the [`attestKey(_:clientDataHash:completionHandler:)`](dcappattestservice/attestkey(_:clientdatahash:completionhandler:).md) method to initiate attestation.

```swift
service.attestKey(keyId, clientDataHash: hash) { attestation, error in
    guard error == nil else { /* Handle error and return. */ }

    // Send the attestation object to your server for verification.
}
```

If the method, which accesses a remote Apple server, returns the [`serverUnavailable`](dcerror-swift.struct/serverunavailable.md) error, try attestation again later with the same key. For any other error, discard the key identifier and create a new key when you want to try again. Otherwise, send the completion handler’s attestation object and the `keyId` to your server for processing.

> ❗ **Important**: If your app already has millions of daily active users and you want to start calling the [`attestKey(_:clientDataHash:completionHandler:)`](dcappattestservice/attestkey(_:clientdatahash:completionhandler:).md) method to initiate attestation from your app, please review [`Preparing to use the app attest service`](preparing-to-use-the-app-attest-service.md) for guidance on safely ramping your users.

If you use the [`URL Loading System`](https://developer.apple.com/documentation/Foundation/url-loading-system) to communicate with your server, you can send an unmodified attestation object. If you communicate with your server by generating text-based HTTPS queries, convert the attestation object to a Base64-encoded string first.

```swift
let attestationString = attestation?.base64EncodedString()
```

Your server deems the app instance to be valid if it can successfully verify the attestation object. In this case, be sure to persistently store the key identifier — not the attestation object — in your app for future use in signing server requests.

##### Assert Your Apps Validity As Necessary

After successfully verifying a key’s attestation, your server can require the app to assert its legitimacy for any or all future server requests. The app does this by signing the request. In the app, first obtain a unique, one-time challenge from the server. You use a challenge here, like for attestation, to avoid replay attacks. Then combine the challenge with the server request to create a hash.

```swift
let challenge = <# A string from your server #>
let request = [ "action": "getGameLevel",
                "levelId": "1234",
                "challenge": challenge ]
guard let clientData = try? JSONEncoder().encode(request) else { return }
let clientDataHash = Data(SHA256.hash(data: clientData))
```

Use this hash and the key identifier that you generate above to create an assertion object by calling the [`generateAssertion(_:clientDataHash:completionHandler:)`](dcappattestservice/generateassertion(_:clientdatahash:completionhandler:).md) method.

```swift
service.generateAssertion(keyId, clientDataHash: clientDataHash) { assertion, error in
    guard error == nil else { /* Handle the error. */ }

    // Send the assertion and request to your server.
}
```

On success, pass the completion handler’s assertion object, along with the client data, to the server. If the assertion object fails verification, it’s your responsibility to decide how to handle the request.

There’s no restriction on the number of assertions that you can make with a key. Nevertheless, you typically reserve assertions for requests made at sensitive moments in your app’s life cycle, like when the app downloads premium content.

##### Start Over on Reinstallation

The keys that you generate remain valid through regular app updates, but don’t survive app reinstallation, device migration, or restoration of a device from a backup. In these cases, you need to start the process from the beginning and generate a new key. Try to limit new key generation to only these events, or to the addition of new users. Keeping the key count low on a device helps when trying to detect certain kinds of fraud.

## See Also

- [Validating apps that connect to your server](validating-apps-that-connect-to-your-server.md)
  Verify that connections to your server come from legitimate instances of your app.
- [Assessing fraud risk](assessing-fraud-risk.md)
  Request and analyze risk data using server-to-server calls.
- [Preparing to use the app attest service](preparing-to-use-the-app-attest-service.md)
  Test your implementation in a development environment and onboard users gradually.
- [class DCAppAttestService](dcappattestservice.md)
  A service that you use to validate the instance of your app running on a device.
- [App Attest Environment](../BundleResources/Entitlements/com.apple.developer.devicecheck.appattest-environment.md)
  The environment for an app that uses the App Attest service to validate itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicecheck/establishing-your-app-s-integrity)*