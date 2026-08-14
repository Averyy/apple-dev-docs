# iconMode

**Framework**: Quick Look Thumbnailing  
**Kind**: property

A Boolean value indicating whether the generated thumbnail request should include icon decorations.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var iconMode: Bool { get set }
```

#### Discussion

Set this property to [`true`](https://developer.apple.com/documentation/swift/true) to generate a thumbnail that’s appropriate to use as a file icon. Depending on the platform, the thumbnail may be embedded in a frame, show a curled corner, or display a background or drop shadow. If this property’s value is [`false`](https://developer.apple.com/documentation/swift/false), [`QLThumbnailGenerator`](qlthumbnailgenerator.md) generates a raw, undecorated thumbnail.

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var size: CGSize](qlthumbnailgenerator/request/size.md)
  The size of the thumbnails.
- [var scale: CGFloat](qlthumbnailgenerator/request/scale.md)
  The pixel density of the display on the intended device.
- [var contentType: UTType!](qlthumbnailgenerator/request/contenttype.md)
  The content type of the source data for the thumbnail request.
- [var representationTypes: QLThumbnailGenerator.Request.RepresentationTypes](qlthumbnailgenerator/request/representationtypes-swift.property.md)
  The thumbnail sizes that you provide for a thumbnail request.
- [var minimumDimension: CGFloat](qlthumbnailgenerator/request/minimumdimension.md)
  The minimum height or width for a generated thumbnail.
- [QLThumbnailGenerator.Request.RepresentationTypes](qlthumbnailgenerator/request/representationtypes-swift.struct.md)
  The various types of thumbnails that you can request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailgenerator/request/iconmode)*