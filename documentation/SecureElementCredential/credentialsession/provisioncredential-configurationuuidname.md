# provisionCredential(configurationUUID:name:)

**Framework**: SecureElementCredential  
**Kind**: method

Creates a credential in the Secure Element.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
func provisionCredential(configurationUUID: UUID, name: String) async throws -> CredentialSession.Credential
```

## Mentions

- [Accessing and using secure element credentials](accessing-and-using-secure-element-credentials.md)

#### Return Value

A [`CredentialSession.Credential`](credentialsession/credential.md), initialized with the [`CredentialSession.Credential.State.installationPending`](credentialsession/credential/state-swift.enum/installationpending.md) state.

#### Discussion

This method installs into the Secure Element an applet bundle that you’ve submitted through the [`Apple Business Register`](https://developer.apple.comhttps://register.apple.com/login) portal.

## Parameters

- `configurationUUID`: A UUID corresponding to an applet bundle configured on the   portal. The system uses the corresponding applet bundle to provision the instance associated with the created credential. The UUID is opaque to the device.
- `name`: A friendly name assigned for ease of identification the provisioned credential. The name is opaque to the device.

## See Also

- [func deleteCredential(CredentialSession.Credential) async throws](credentialsession/deletecredential(_:).md)
  Deletes a credential on the Secure Element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/provisioncredential(configurationuuid:name:))*