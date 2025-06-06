# streamType

**Framework**: ScreenCaptureKit  
**Kind**: property

The type of the streaming content.

**Availability**:
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
var streamType: SCStreamType { get }
```

#### Discussion

> **Note**:  Use the [`style`](sccontentfilter/style.md) property instead, which provides additional information about the content.

 Use the [`style`](sccontentfilter/style.md) property instead, which provides additional information about the content.

## See Also

- [var contentRect: CGRect](sccontentfilter/contentrect.md)
  The size and location of the content to filter, in screen points.
- [var pointPixelScale: Float](sccontentfilter/pointpixelscale.md)
  The scaling factor used to translate screen points into pixels.
- [enum SCStreamType](scstreamtype.md)
  The display type of the presented stream.
- [var style: SCShareableContentStyle](sccontentfilter/style.md)
  The display style of the sharable content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentfilter/streamtype)*