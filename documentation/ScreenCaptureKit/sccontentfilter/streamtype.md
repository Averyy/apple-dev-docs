# streamType

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

The type of the streaming content.

**Availability**:
- Mac Catalyst 18.2+ - Deprecated in 18.2
- macOS 14.0+ - Deprecated in 14.2

> **Deprecated**: Use style instead

## Declaration

```swift
var streamType: SCStreamType { get }
```

```objc
@property (nonatomic, readonly) SCStreamType streamType;
```

## Discussion

> **Note**:  Use the [`style`](./style.md) property instead, which provides additional information about the content.

## See Also

### Filter properties
- [var contentRect: CGRect](./contentrect.md)
  The size and location of the content to filter, in screen points.
- [var pointPixelScale: Float](./pointpixelscale.md)
  The scaling factor used to translate screen points into pixels.
- [enum SCStreamType](../scstreamtype.md)
  The display type of the presented stream.
- [var style: SCShareableContentStyle](./style.md)
  The display style of the sharable content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentfilter/streamtype)*