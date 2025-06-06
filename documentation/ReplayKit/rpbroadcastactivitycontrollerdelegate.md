# RPBroadcastActivityControllerDelegate

**Framework**: ReplayKit  
**Kind**: protocol

A protocol that defines the methods to implement to respond to selection events from a broadcast activity controller.

**Availability**:
- macOS 11.0+

## Declaration

```swift
protocol RPBroadcastActivityControllerDelegate : NSObjectProtocol
```

## Topics

### Responding to User Selection
- [func broadcastActivityController(RPBroadcastActivityController, didFinishWith: RPBroadcastController?, error: (any Error)?)](rpbroadcastactivitycontrollerdelegate/broadcastactivitycontroller(_:didfinishwith:error:).md)
  Tells the delegate that a user selected a broadcast.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class RPBroadcastActivityViewController](rpbroadcastactivityviewcontroller.md)
  A view controller that displays a user interface where users choose a broadcast service.
- [class RPSystemBroadcastPickerView](rpsystembroadcastpickerview.md)
  A view displaying a broadcast button that, when tapped, shows a broadcast picker.
- [class RPBroadcastActivityController](rpbroadcastactivitycontroller.md)
  A controller object that presents the macOS broadcast picker.
- [class RPBroadcastConfiguration](rpbroadcastconfiguration.md)
  An object used to configure the movie clips produced during a live broadcast.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastactivitycontrollerdelegate)*