# startEmulation()

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method

Start the card emulation and present a modal user interface to the person using the app.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
func startEmulation() async throws
```

## Discussion

Set the [`alertMessage`](./alertmessage.md) prior to calling this method.

This method throws an error of type [`CardSession.Error`](./error.md) if card emulation fails. Possible error conditions are:

- [`CardSession.Error.systemNotAvailable`](./error/systemnotavailable.md)
- [`CardSession.Error.accessNotAccepted`](./error/accessnotaccepted.md)
- [`CardSession.Error.systemEligibilityFailed`](./error/systemeligibilityfailed.md)
- [`CardSession.Error.radioDisabled`](./error/radiodisabled.md)

## See Also

### Managing card emulation
- [CardSession.Error](./error.md)
  An error type that indicates problems with a card session.
- [func stopEmulation(status: CardSession.EmulationUIStatus) async](./stopemulation%28status%29.md)
  Stop card emulation and display a status.
- [CardSession.EmulationUIStatus](./emulationuistatus.md)
  The final status to show in the user interface when ending card emulation.
- [var isEmulationInProgress: Bool](./isemulationinprogress.md)
  A Boolean value that indicates whether emulation is currently active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/cardsession/startemulation())*