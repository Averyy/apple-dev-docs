# deleteCredential(_:)

**Framework**: SecureElementCredential  
**Kind**: method

Deletes a credential on the Secure Element.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
func deleteCredential(_ credential: CredentialSession.Credential) async throws
```

## Mentions

- [Accessing and using secure element credentials](accessing-and-using-secure-element-credentials.md)

## Parameters

- `credential`: The credential to delete.

## See Also

- [func provisionCredential(configurationUUID: UUID, name: String) async throws -> CredentialSession.Credential](credentialsession/provisioncredential(configurationuuid:name:).md)
  Creates a credential in the Secure Element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/deletecredential(_:))*