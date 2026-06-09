# SCVideoEffectOutput

**Framework**: ScreenCaptureKit  
**Kind**: class

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
class SCVideoEffectOutput
```

#### Overview

SCVideoEffectOutput

SCVideoEffectOutput represents a camera video effect session on a SCStream. Create an instance and add it to a stream using addVideoEffectOutput:error: to start the camera video effect. The camera preview is framework-managed and automatically added to the application’s key window. Callbacks for video effect lifecycle events are delivered through the SCStreamDelegate protocol.

## Topics

### Initializers
- [init(cameraDevice: AVCaptureDevice)](scvideoeffectoutput/init(cameradevice:).md)
### Instance Properties
- [var cameraDevice: AVCaptureDevice](scvideoeffectoutput/cameradevice.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scvideoeffectoutput)*