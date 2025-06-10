# CardSession.Error

**Framework**: Core NFC  
**Kind**: enum

An error type that indicates problems with a card session.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
enum Error
```

## Topics

### Card session errors
- [CardSession.Error.invalidated](cardsession/error/invalidated.md)
  The system invalidated the card session.
- [CardSession.Error.userInvalidated](cardsession/error/userinvalidated.md)
  The person using the app invalidated the card session.
- [CardSession.Error.maxSessionDurationReached](cardsession/error/maxsessiondurationreached.md)
  The session is no longer valid because it reached its maximum duration.
- [CardSession.Error.transmissionError](cardsession/error/transmissionerror.md)
  The card session experienced a general error transmitting data.
- [CardSession.Error.systemNotAvailable](cardsession/error/systemnotavailable.md)
  A system resource is currently unavailable.
- [CardSession.Error.accessNotAccepted](cardsession/error/accessnotaccepted.md)
  The person using the app hasn’t yet accepted or declined your app’s request to use the NFC card emulation service.
- [CardSession.Error.systemEligibilityFailed](cardsession/error/systemeligibilityfailed.md)
  The current system setting or hardware configuation isn’t eligible to use the NFC card emulation service.
- [CardSession.Error.emulationStopped](cardsession/error/emulationstopped.md)
  The card emulation stopped.
- [CardSession.Error.radioDisabled](cardsession/error/radiodisabled.md)
  The card session failed because the NFC radio is disabled.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init() async throws](cardsession/init.md)
  Creates a contactless card session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/cardsession/error)*