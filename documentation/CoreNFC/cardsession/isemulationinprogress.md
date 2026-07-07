# isEmulationInProgress

**Framework**: Core NFC  
**Kind**: property

A Boolean value that indicates whether emulation is currently active.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
var isEmulationInProgress: Bool { get async }
```

## See Also

- [func startEmulation() async throws](cardsession/startemulation.md)
  Start the card emulation and present a modal user interface to the person using the app.
- [CardSession.Error](cardsession/error.md)
  An error type that indicates problems with a card session.
- [func stopEmulation(status: CardSession.EmulationUIStatus) async](cardsession/stopemulation(status:).md)
  Stop card emulation and display a status.
- [CardSession.EmulationUIStatus](cardsession/emulationuistatus.md)
  The final status to show in the user interface when ending card emulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/cardsession/isemulationinprogress)*