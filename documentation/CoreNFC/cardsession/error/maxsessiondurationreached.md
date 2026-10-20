# CardSession.Error.maxSessionDurationReached

**Framework**: Core NFC  
**Kind**: case  
**Role**: Case

The session is no longer valid because it reached its maximum duration.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
case maxSessionDurationReached
```

#### Discussion

If you reach the emulation session’s maximum duration, you can reset with [`stopEmulation(status:)`](../stopemulation%28status%29.md). However, the API enforces a “cool down” period, and restarting emulation too quickly can produce a [`CardSession.Error.systemNotAvailable`](./systemnotavailable.md) error. If this happens, wait before attempting another call to [`startEmulation()`](../startemulation%28%29.md).

## See Also

### Card session errors
- [CardSession.Error.invalidated](./invalidated.md)
  The system invalidated the card session.
- [CardSession.Error.userInvalidated](./userinvalidated.md)
  The person using the app invalidated the card session.
- [CardSession.Error.transmissionError](./transmissionerror.md)
  The card session experienced a general error transmitting data.
- [CardSession.Error.systemNotAvailable](./systemnotavailable.md)
  A system resource is currently unavailable.
- [CardSession.Error.accessNotAccepted](./accessnotaccepted.md)
  The person using the app hasn’t yet accepted or declined your app’s request to use the NFC card emulation service.
- [CardSession.Error.systemEligibilityFailed](./systemeligibilityfailed.md)
  The current system setting or hardware configuation isn’t eligible to use the NFC card emulation service.
- [CardSession.Error.emulationStopped](./emulationstopped.md)
  The card emulation stopped.
- [CardSession.Error.radioDisabled](./radiodisabled.md)
  The card session failed because the NFC radio is disabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/cardsession/error/maxsessiondurationreached)*