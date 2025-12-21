# AVCaptureSmartFramingMonitor

**Framework**: AVFoundation  
**Kind**: class

An object associated with a capture device that monitors the scene and suggests an optimal framing.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
class AVCaptureSmartFramingMonitor
```

## Mentions

- [Adopting smart framing in your camera app](adopting-smart-framing-in-your-camera-app.md)

#### Overview

A smart framing monitor observes its associated device for objects of interest entering and exiting the camera’s field of view and recommends an optimal framing for good photographic composition. This framing recommendation consists of an aspect ratio and zoom factor. You may respond to the device’s framing recommendation by calling [`setDynamicAspectRatio(_:completionHandler:)`](avcapturedevice/setdynamicaspectratio(_:completionhandler:).md) and setting [`videoZoomFactor`](avcapturedevice/videozoomfactor.md) on the associated device in whatever order best matches your animation between old and new framings.

## Topics

### Configuring framings
- [var supportedFramings: [AVCaptureFraming]](avcapturesmartframingmonitor/supportedframings.md)
  An array of framings supported by the monitor in its current configuration.
- [var enabledFramings: [AVCaptureFraming]](avcapturesmartframingmonitor/enabledframings.md)
  An array of framings that the monitor is allowed to suggest.
- [var recommendedFraming: AVCaptureFraming?](avcapturesmartframingmonitor/recommendedframing.md)
  The latest recommended framing from the monitor.
### Managing the life cycle
- [var isMonitoring: Bool](avcapturesmartframingmonitor/ismonitoring.md)
  Yes when the receiver is actively monitoring.
- [func startMonitoring() throws](avcapturesmartframingmonitor/startmonitoring.md)
  Begins monitoring the device’s active scene and making framing recommendations.
- [func stopMonitoring()](avcapturesmartframingmonitor/stopmonitoring.md)
  Stops monitoring the device’s active scene and making framing recommendations.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Observable](../Observation/Observable.md)

## See Also

- [var smartFramingMonitor: AVCaptureSmartFramingMonitor?](avcapturedevice/smartframingmonitor.md)
  A monitor owned by the device that recommends an optimal framing based on the content in the scene.
- [class AVCaptureFraming](avcaptureframing.md)
  A framing, consisting of an aspect ratio and a zoom factor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesmartframingmonitor)*