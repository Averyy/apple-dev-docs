# CredentialSession.State

**Framework**: SecureElementCredential  
**Kind**: enum  
**Role**: Enumeration

An enumeration of the possible states of a card session.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
enum State
```

## Topics

### Credential session states
- [CredentialSession.State.management](./state-swift.enum/management.md)
  The state for managing the credential session.
- [case wired(credential: CredentialSession.Credential)](./state-swift.enum/wired%28credential%29.md)
  The state for performing wired operations with a given credential.
- [case cardEmulation(credential: CredentialSession.Credential)](./state-swift.enum/cardemulation%28credential%29.md)
  The state for performing card emulation with a given credential.
- [CredentialSession.Credential](./credential.md)
  Information about a credential that a credential session retrieves from the Secure Element.
- [CredentialSession.State.invalid](./state-swift.enum/invalid.md)
  The state of an invalid credential session.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing the session state
- [var state: CredentialSession.State](./state-swift.property.md)
  The current state of the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/state-swift.enum)*