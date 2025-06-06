# SCStreamType

**Framework**: ScreenCaptureKit  
**Kind**: enum

The display type of the presented stream.

**Availability**:
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
enum SCStreamType
```

## Topics

### Client presentation
- [SCStreamType.display](scstreamtype/display.md)
  The stream is currently on a complete display.
- [SCStreamType.window](scstreamtype/window.md)
  The stream is currently presented as a window.
### Initializers
- [init?(rawValue: Int)](scstreamtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var contentRect: CGRect](sccontentfilter/contentrect.md)
  The size and location of the content to filter, in screen points.
- [var pointPixelScale: Float](sccontentfilter/pointpixelscale.md)
  The scaling factor used to translate screen points into pixels.
- [var streamType: SCStreamType](sccontentfilter/streamtype.md)
  The type of the streaming content.
- [var style: SCShareableContentStyle](sccontentfilter/style.md)
  The display style of the sharable content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamtype)*