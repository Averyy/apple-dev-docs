# contentRect

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

The size and location of the content to filter, in screen points.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 14.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var contentRect: CGRect { get }
```

```objc
@property (nonatomic, readonly) CGRect contentRect;
```

## See Also

### Filter properties
- [var pointPixelScale: Float](./pointpixelscale.md)
  The scaling factor used to translate screen points into pixels.
- [var streamType: SCStreamType](./streamtype.md)
  The type of the streaming content.
- [enum SCStreamType](../scstreamtype.md)
  The display type of the presented stream.
- [var style: SCShareableContentStyle](./style.md)
  The display style of the sharable content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentfilter/contentrect)*