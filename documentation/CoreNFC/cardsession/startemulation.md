# startEmulation()

**Framework**: Core NFC  
**Kind**: method

Start the card emulation and present a modal user interface to the person using the app.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
func startEmulation() async throws
```

#### Discussion

Set the [`alertMessage`](cardsession/alertmessage.md) prior to calling this method.

This method throws an error of type [`CardSession.Error`](cardsession/error.md) if card emulation fails. Possible error conditions are:

- [`CardSession.Error.systemNotAvailable`](cardsession/error/systemnotavailable.md)
- [`CardSession.Error.accessNotAccepted`](cardsession/error/accessnotaccepted.md)
- [`CardSession.Error.systemEligibilityFailed`](cardsession/error/systemeligibilityfailed.md)
- [`CardSession.Error.radioDisabled`](cardsession/error/radiodisabled.md)

## See Also

- [CardSession.Error](cardsession/error.md)
  An error type that indicates problems with a card session.
- [func stopEmulation(status: CardSession.EmulationUIStatus) async](cardsession/stopemulation(status:).md)
  Stop card emulation and display a status.
- [CardSession.EmulationUIStatus](cardsession/emulationuistatus.md)
  The final status to show in the user interface when ending card emulation.
- [var isEmulationInProgress: Bool](cardsession/isemulationinprogress.md)
  A Boolean value that indicates whether emulation is currently active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/cardsession/startemulation())*