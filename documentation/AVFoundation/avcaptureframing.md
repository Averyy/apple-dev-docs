# AVCaptureFraming

**Framework**: AVFoundation  
**Kind**: class

A framing, consisting of an aspect ratio and a zoom factor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
class AVCaptureFraming
```

#### Overview

An [`AVCaptureSmartFramingMonitor`](avcapturesmartframingmonitor.md) provides framing recommendations using this object.

## Topics

### Inspecting a framing
- [var aspectRatio: AVCaptureDevice.AspectRatio](avcaptureframing/aspectratio.md)
  An aspect ratio.
- [var zoomFactor: Float](avcaptureframing/zoomfactor.md)
  A zoom factor.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [var smartFramingMonitor: AVCaptureSmartFramingMonitor?](avcapturedevice/smartframingmonitor.md)
  A monitor owned by the device that recommends an optimal framing based on the content in the scene.
- [class AVCaptureSmartFramingMonitor](avcapturesmartframingmonitor.md)
  An object associated with a capture device that monitors the scene and suggests an optimal framing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureframing)*