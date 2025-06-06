# RPBroadcastActivityViewControllerDelegate

**Framework**: ReplayKit  
**Kind**: protocol

The protocol you implement to respond to changes to a broadcast activity user interface.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
protocol RPBroadcastActivityViewControllerDelegate : NSObjectProtocol
```

#### Overview

Use this class to respond to changes to a broadcast activity user interface, represented by an [`RPBroadcastActivityViewController`](rpbroadcastactivityviewcontroller.md) object.

## Topics

### Connecting to a Service
- [func broadcastActivityViewController(RPBroadcastActivityViewController, didFinishWith: RPBroadcastController?, error: (any Error)?)](rpbroadcastactivityviewcontrollerdelegate/broadcastactivityviewcontroller(_:didfinishwith:error:).md)
  Indicates that the broadcast activity view controller is ready to be dismissed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any RPBroadcastActivityViewControllerDelegate)?](rpbroadcastactivityviewcontroller/delegate.md)
  The delegate for the broadcast activity view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastactivityviewcontrollerdelegate)*