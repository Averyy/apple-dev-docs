# CardSession.Error.transmissionError

**Framework**: Core NFC  
**Kind**: case

The card session experienced a general error transmitting data.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
case transmissionError
```

#### Discussion

If you receive this error, you can retry the transmission if the connection with the NFC reader remains valid.

## See Also

- [CardSession.Error.invalidated](cardsession/error/invalidated.md)
  The system invalidated the card session.
- [CardSession.Error.userInvalidated](cardsession/error/userinvalidated.md)
  The person using the app invalidated the card session.
- [CardSession.Error.maxSessionDurationReached](cardsession/error/maxsessiondurationreached.md)
  The session is no longer valid because it reached its maximum duration.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/cardsession/error/transmissionerror)*