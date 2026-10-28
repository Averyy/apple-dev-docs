# provisionCredential(configurationUUID:name:)

**Framework**: SecureElementCredential  
**Kind**: method  
**Role**: Instance Method

Creates a credential in the Secure Element.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
func provisionCredential(configurationUUID: UUID, name: String) async throws -> CredentialSession.Credential
```

## Mentions

- [Accessing and using secure element credentials](../accessing-and-using-secure-element-credentials.md)

## Return Value

A [`CredentialSession.Credential`](./credential.md), initialized with the [`CredentialSession.Credential.State.installationPending`](./credential/state-swift.enum/installationpending.md) state.

## Discussion

This method installs into the Secure Element an applet bundle that you’ve submitted through the [Apple Business Register](https://register.apple.com/login) portal.

> **Note**: If there is not enough space in the Secure Element to provision the new credential, the system shows a space management UI over the current app. A person using the device can use this interface to remove other credentials to free up space or cancel the provisioning attempt.

- The most common errors are:

  - [`CredentialSession.ErrorCode.invalidInput`](./errorcode/invalidinput.md): The `name` parameter is empty.
  - [`CredentialSession.ErrorCode.invalidSessionState`](./errorcode/invalidsessionstate.md): The session isn’t in the [`CredentialSession.State.management`](./state-swift.enum/management.md) state.
  - [`CredentialSession.ErrorCode.invalidProductConfigID`](./errorcode/invalidproductconfigid.md): The `configurationUUID` does not correspond to a known product configuration.
  - [`CredentialSession.ErrorCode.insufficientSpace`](./errorcode/insufficientspace.md): The Secure Element doesn’t have enough storage space.
  - [`CredentialSession.ErrorCode.network`](./errorcode/network.md): A network error occurred during provisioning.
  - [`CredentialSession.ErrorCode.conditionsNotSatisfied`](./errorcode/conditionsnotsatisfied.md): The iCloud account or passcode conditions aren’t met.

## Parameters

- `configurationUUID`: A UUID corresponding to an product configuration configured on the [Apple Business Register](https://register.apple.com/login) portal. The system uses the corresponding product configuration to provision the instance associated with the created credential. The UUID is opaque to the device.
- `name`: A friendly name assigned for ease of identification the provisioned credential. The name is opaque to the device.

## See Also

### Managing a credential
- [func deleteCredential(CredentialSession.Credential) async throws](./deletecredential%28_%29.md)
  Deletes a credential on the Secure Element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/provisioncredential(configurationuuid:name:))*