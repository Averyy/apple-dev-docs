# deleteCredential(_:)

**Framework**: SecureElementCredential  
**Kind**: method  
**Role**: Instance Method

Deletes a credential on the Secure Element.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
func deleteCredential(_ credential: CredentialSession.Credential) async throws
```

## Mentions

- [Accessing and using secure element credentials](../accessing-and-using-secure-element-credentials.md)

## Discussion

- The most common errors are:

  - [`CredentialSession.ErrorCode.invalidSessionState`](./errorcode/invalidsessionstate.md): The session isn’t in the [`CredentialSession.State.management`](./state-swift.enum/management.md) state.

## Parameters

- `credential`: The credential to delete.

## See Also

### Managing a credential
- [func provisionCredential(configurationUUID: UUID, name: String) async throws -> CredentialSession.Credential](./provisioncredential%28configurationuuid,name%29.md)
  Creates a credential in the Secure Element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/deletecredential(_:))*