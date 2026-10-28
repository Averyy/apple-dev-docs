# state

**Framework**: SecureElementCredential  
**Kind**: property  
**Role**: Instance Property

The current state of the session.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
var state: CredentialSession.State { get async }
```

## Mentions

- [Accessing and using secure element credentials](../accessing-and-using-secure-element-credentials.md)

## Discussion

Sessions start in the [`CredentialSession.State.management`](./state-swift.enum/management.md) state. Calls to the wired or card emulation APIs change the state to [`CredentialSession.State.wired(credential:)`](./state-swift.enum/wired%28credential%29.md) or [`CredentialSession.State.cardEmulation(credential:)`](./state-swift.enum/cardemulation%28credential%29.md). Leaving wired or card emulation mode returns the state to [`CredentialSession.State.management`](./state-swift.enum/management.md).

Explicitly invalidating the session, encountering an error, or the app entering the background changes the state to [`CredentialSession.State.invalid`](./state-swift.enum/invalid.md). An invalid session can’t return to one of the other states.

## See Also

### Accessing the session state
- [CredentialSession.State](./state-swift.enum.md)
  An enumeration of the possible states of a card session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/state-swift.property)*