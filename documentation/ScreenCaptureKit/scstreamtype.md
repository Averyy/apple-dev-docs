# SCStreamType

**Framework**: ScreenCaptureKit  
**Kind**: enum  
**Role**: Enumeration

The display type of the presented stream.

**Availability**:
- Mac Catalyst 18.2+ - Deprecated in 18.2
- macOS 14.0+ - Deprecated in 15.0

> **Deprecated**: Use SCShareableContentStyle instead

## Declaration

```swift
enum SCStreamType
```

```c
enum SCStreamType : NSInteger;
```

## Topics

### Client presentation
- [SCStreamType.display](./scstreamtype/display.md)
  The stream is currently on a complete display.
- [SCStreamType.window](./scstreamtype/window.md)
  The stream is currently presented as a window.
### Initializers
- [init?(rawValue: Int)](./scstreamtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Filter properties
- [var contentRect: CGRect](./sccontentfilter/contentrect.md)
  The size and location of the content to filter, in screen points.
- [var pointPixelScale: Float](./sccontentfilter/pointpixelscale.md)
  The scaling factor used to translate screen points into pixels.
- [var streamType: SCStreamType](./sccontentfilter/streamtype.md)
  The type of the streaming content.
- [var style: SCShareableContentStyle](./sccontentfilter/style.md)
  The display style of the sharable content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamtype)*