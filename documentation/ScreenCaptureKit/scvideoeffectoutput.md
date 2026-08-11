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

## See Also

- [class SCStream](scstream.md)
  An instance that represents a stream of shareable content.
- [class SCStreamConfiguration](scstreamconfiguration.md)
  An instance that provides the output configuration for a stream.
- [class SCContentFilter](sccontentfilter.md)
  An instance that filters the content a stream captures.
- [protocol SCStreamDelegate](scstreamdelegate.md)
  A delegate protocol your app implements to respond to stream events.
- [class SCScreenshotManager](scscreenshotmanager.md)
  An instance for the capture of single frames from a stream.
- [class SCScreenshotConfiguration](scscreenshotconfiguration.md)
  An object that contains screenshot properties such as output width, height, and image quality specifications.
- [class SCScreenshotOutput](scscreenshotoutput.md)
  An object that contains all images requested by the client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scvideoeffectoutput)*