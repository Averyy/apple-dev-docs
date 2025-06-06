# HMCameraStreamControlDelegate

**Framework**: HomeKit  
**Kind**: protocol

A protocol that gives the delegate updates on the camera stream.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
protocol HMCameraStreamControlDelegate : NSObjectProtocol
```

## Topics

### Observing stream activity
- [func cameraStreamControlDidStartStream(HMCameraStreamControl)](hmcamerastreamcontroldelegate/camerastreamcontroldidstartstream(_:).md)
  Tells the delegate that the camera stream has started.
- [func cameraStreamControl(HMCameraStreamControl, didStopStreamWithError: (any Error)?)](hmcamerastreamcontroldelegate/camerastreamcontrol(_:didstopstreamwitherror:).md)
  Tells the delegate that the camera stream has stopped.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any HMCameraStreamControlDelegate)?](hmcamerastreamcontrol/delegate.md)
  Delegate that receives updates as the camera stream changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcamerastreamcontroldelegate)*