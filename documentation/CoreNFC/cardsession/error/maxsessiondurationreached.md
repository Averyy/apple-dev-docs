# CardSession.Error.maxSessionDurationReached

**Framework**: Core NFC  
**Kind**: case

The session is no longer valid because it reached its maximum duration.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
case maxSessionDurationReached
```

#### Discussion

If you reach the emulation session’s maximum duration, you can reset with [`stopEmulation(status:)`](cardsession/stopemulation(status:).md). However, the API enforces a “cool down” period, and restarting emulation too quickly can produce a [`CardSession.Error.systemNotAvailable`](cardsession/error/systemnotavailable.md) error. If this happens, wait before attempting another call to [`startEmulation()`](cardsession/startemulation().md).

## See Also

- [CardSession.Error.invalidated](cardsession/error/invalidated.md)
  The system invalidated the card session.
- [CardSession.Error.userInvalidated](cardsession/error/userinvalidated.md)
  The person using the app invalidated the card session.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/cardsession/error/maxsessiondurationreached)*