# CardSession.EmulationUIStatus

**Framework**: Core NFC  
**Kind**: enum  
**Role**: Enumeration

The final status to show in the user interface when ending card emulation.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
enum EmulationUIStatus
```

## Topics

### Emulation statuses
- [CardSession.EmulationUIStatus.success](./emulationuistatus/success.md)
  A status display to indicate a successful operation, such as a checkmark.
- [CardSession.EmulationUIStatus.failure](./emulationuistatus/failure.md)
  A status display to indicate an error, such as an exclamation mark.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Managing card emulation
- [func startEmulation() async throws](./startemulation%28%29.md)
  Start the card emulation and present a modal user interface to the person using the app.
- [CardSession.Error](./error.md)
  An error type that indicates problems with a card session.
- [func stopEmulation(status: CardSession.EmulationUIStatus) async](./stopemulation%28status%29.md)
  Stop card emulation and display a status.
- [var isEmulationInProgress: Bool](./isemulationinprogress.md)
  A Boolean value that indicates whether emulation is currently active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/cardsession/emulationuistatus)*