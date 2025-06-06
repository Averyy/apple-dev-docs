# CredentialSession.Credential

**Framework**: SecureElementCredential  
**Kind**: struct

Information about a credential that a credential session retrieves from the Secure Element.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
struct Credential
```

## Mentions

- [Accessing and using secure element credentials](accessing-and-using-secure-element-credentials.md)

#### Overview

A credential is an abstraction of the cryptographic elements of your applet bundle installed in the Secure Element. You perform this installation with [`provisionCredential(configurationUUID:name:)`](credentialsession/provisioncredential(configurationuuid:name:).md), which retrieves the applet bundle you registered with the [`Apple Business Register`](https://developer.apple.comhttps://register.apple.com/login), installs it in the Secure Element, and returns a `Credential` instance.

`Credential` objects are snapshots of credential data at the time the [`listCredentials()`](credentialsession/listcredentials().md) method loads them. To ensure up-to-date metadata, reload credentials with that same method.

## Topics

### Identifying a credential
- [let identifier: UUID](credentialsession/credential/identifier.md)
  A unique identifier for the credential.
### Getting a display name
- [let name: String](credentialsession/credential/name.md)
  A readable name for the credential.
### Inspecting credential state
- [let state: CredentialSession.Credential.State](credentialsession/credential/state-swift.property.md)
  A snapshot of the credential’s installation state.
- [CredentialSession.Credential.State](credentialsession/credential/state-swift.enum.md)
  An enumeration of possible values of a credential’s installation state.
### Hashing
- [func hash(into: inout Hasher)](credentialsession/credential/hash(into:).md)
  Hashes the essential components of the value by feeding them into the given hasher.
### Comparing credentials
- [static func == (CredentialSession.Credential, CredentialSession.Credential) -> Bool](credentialsession/credential/==(_:_:).md)
  Returns a Boolean value that indicates whether two values are equal.
### Structures
- [CredentialSession.Credential.InstanceInfo](credentialsession/credential/instanceinfo.md)
  Information about an applet instance associated with a specific credential.
### Default Implementations
- [Equatable Implementations](credentialsession/credential/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func listCredentials() async throws -> [CredentialSession.Credential]](credentialsession/listcredentials.md)
  Retrieves a list of of credentials to which the app has access rights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/credential)*