# SCShareableContentInfo

**Framework**: ScreenCaptureKit  
**Kind**: class

An instance that provides information for the content in a given stream.

**Availability**:
- Mac Catalyst 18.2+
- macOS 14.0+

## Declaration

```swift
class SCShareableContentInfo
```

## Topics

### Shared content properties
- [var contentRect: CGRect](scshareablecontentinfo/contentrect.md)
  The size and location of content for the stream.
- [var pointPixelScale: Float](scshareablecontentinfo/pointpixelscale.md)
  The scaling from points to output pixel resolution for the stream.
- [var style: SCShareableContentStyle](scshareablecontentinfo/style.md)
  The current presentation style of the stream.

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

- [class SCShareableContent](scshareablecontent.md)
  An instance that represents a set of displays, apps, and windows that your app can capture.
- [enum SCShareableContentStyle](scshareablecontentstyle.md)
  The style of content presented in a stream.
- [class SCDisplay](scdisplay.md)
  An instance that represents a display device.
- [class SCRunningApplication](scrunningapplication.md)
  An instance that represents an app running on a device.
- [class SCWindow](scwindow.md)
  An instance that represents an onscreen window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scshareablecontentinfo)*