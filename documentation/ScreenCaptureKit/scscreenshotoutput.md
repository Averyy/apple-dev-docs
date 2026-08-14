# SCScreenshotOutput

**Framework**: ScreenCaptureKit  
**Kind**: class

An object that contains all images requested by the client.

**Availability**:
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
class SCScreenshotOutput
```

## Topics

### Instance Properties
- [var fileURL: NSURL?](scscreenshotoutput/fileurl.md)
  A URL property that specifies the location of the saved image.
- [var hdrImage: CGImage?](scscreenshotoutput/hdrimage.md)
  An output property that specifies the high dynamic range version of the screenshot.
- [var sdrImage: CGImage?](scscreenshotoutput/sdrimage.md)
  An output property that specifies the standard dynamic range version of the screenshot.

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
- [class SCVideoEffectOutput](scvideoeffectoutput.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scscreenshotoutput)*