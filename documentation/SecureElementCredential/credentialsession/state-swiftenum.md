# CredentialSession.State

**Framework**: SecureElementCredential  
**Kind**: enum

An enumeration of the possible states of a card session.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
enum State
```

## Topics

### Card session states
- [CredentialSession.State.management](credentialsession/state-swift.enum/management.md)
  The state for managing the credential session.
- [case wired(credential: CredentialSession.Credential)](credentialsession/state-swift.enum/wired(credential:).md)
  The state for performing wired operations with a given credential.
- [case cardEmulation(credential: CredentialSession.Credential)](credentialsession/state-swift.enum/cardemulation(credential:).md)
  The state for performing card emulation with a given credential.
- [CredentialSession.Credential](credentialsession/credential.md)
  Information about a credential that a credential session retrieves from the Secure Element.
- [CredentialSession.State.invalid](credentialsession/state-swift.enum/invalid.md)
  The state of an invalid credential session.
### Comparing states
- [static func == (CredentialSession.State, CredentialSession.State) -> Bool](credentialsession/state-swift.enum/==(_:_:).md)
  Returns a Boolean value that indicates whether two values are equal.
### Default Implementations
- [Equatable Implementations](credentialsession/state-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var state: CredentialSession.State](credentialsession/state-swift.property.md)
  The current state of the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/state-swift.enum)*