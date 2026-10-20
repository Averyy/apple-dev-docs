# RPBroadcastActivityControllerDelegate

**Framework**: ReplayKit  
**Kind**: protocol  
**Role**: Protocol

A protocol that defines the methods to implement to respond to selection events from a broadcast activity controller.

**Availability**:
- macOS 11.0+ - Deprecated in 27.0

> **Deprecated**: No longer supported

## Declaration

```swift
protocol RPBroadcastActivityControllerDelegate : NSObjectProtocol
```

```objc
@protocol RPBroadcastActivityControllerDelegate <NSObject>
```

## Topics

### Responding to User Selection
- [func broadcastActivityController(RPBroadcastActivityController, didFinishWith: RPBroadcastController?, error: (any Error)?)](./rpbroadcastactivitycontrollerdelegate/broadcastactivitycontroller%28_,didfinishwith,error%29.md)
  Tells the delegate that a user selected a broadcast.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Live Broadcast Implementation
- [class RPBroadcastActivityViewController](./rpbroadcastactivityviewcontroller.md)
  A view controller that displays a user interface where users choose a broadcast service.
- [class RPSystemBroadcastPickerView](./rpsystembroadcastpickerview.md)
  A view displaying a broadcast button that, when tapped, shows a broadcast picker.
- [class RPBroadcastActivityController](./rpbroadcastactivitycontroller.md)
  A controller object that presents the macOS broadcast picker.
- [class RPBroadcastConfiguration](./rpbroadcastconfiguration.md)
  An object used to configure the movie clips produced during a live broadcast.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastactivitycontrollerdelegate)*