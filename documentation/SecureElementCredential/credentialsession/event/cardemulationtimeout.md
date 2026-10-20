# CredentialSession.Event.cardEmulationTimeout

**Framework**: SecureElementCredential  
**Kind**: case  
**Role**: Case

The session’s card emulation timer expired.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
case cardEmulationTimeout
```

#### Discussion

This event the session’s state back to [`CredentialSession.State.management`](../state-swift.enum/management.md).

When handling this event, SwiftUI applications must invalidate the [`CredentialTransaction.Configuration`](../../credentialtransaction/configuration.md) requested for this transaction.

## See Also

### Timeout events
- [CredentialSession.Event.presentmentIntentAssertionTimeout](./presentmentintentassertiontimeout.md)
  The session’s presentment intent assertion timed out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/event/cardemulationtimeout)*