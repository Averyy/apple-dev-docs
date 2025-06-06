# CardSession.EmulationUIStatus

**Framework**: Core NFC  
**Kind**: enum

The final status to show in the user interface when ending card emulation.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
enum EmulationUIStatus
```

## Topics

### Emulation statuses
- [CardSession.EmulationUIStatus.success](cardsession/emulationuistatus/success.md)
  A status display to indicate a successful operation, such as a checkmark.
- [CardSession.EmulationUIStatus.failure](cardsession/emulationuistatus/failure.md)
  A status display to indicate an error, such as an exclamation mark.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [func startEmulation() async throws](cardsession/startemulation.md)
  Start the card emulation and present a modal user interface to the person using the app.
- [CardSession.Error](cardsession/error.md)
  An error type that indicates problems with a card session.
- [func stopEmulation(status: CardSession.EmulationUIStatus) async](cardsession/stopemulation(status:).md)
  Stop card emulation and display a status.
- [var isEmulationInProgress: Bool](cardsession/isemulationinprogress.md)
  A Boolean value that indicates whether emulation is currently active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/cardsession/emulationuistatus)*