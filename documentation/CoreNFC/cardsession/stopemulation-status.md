# stopEmulation(status:)

**Framework**: Core NFC  
**Kind**: method

Stop card emulation and display a status.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
func stopEmulation(status: CardSession.EmulationUIStatus) async
```

## Parameters

- `status`: The final status to display.

## See Also

- [func startEmulation() async throws](cardsession/startemulation.md)
  Start the card emulation and present a modal user interface to the person using the app.
- [CardSession.Error](cardsession/error.md)
  An error type that indicates problems with a card session.
- [CardSession.EmulationUIStatus](cardsession/emulationuistatus.md)
  The final status to show in the user interface when ending card emulation.
- [var isEmulationInProgress: Bool](cardsession/isemulationinprogress.md)
  A Boolean value that indicates whether emulation is currently active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/cardsession/stopemulation(status:))*