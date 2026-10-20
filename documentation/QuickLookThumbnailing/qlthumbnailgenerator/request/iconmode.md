# iconMode

**Framework**: Quick Look Thumbnailing  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, assign) BOOL iconMode;
```

#### Discussion

Set this property to [`true`](../../../Swift/true.md) to generate a thumbnail that’s appropriate to use as a file icon. Depending on the platform, the thumbnail may be embedded in a frame, show a curled corner, or display a background or drop shadow. If this property’s value is [`false`](../../../Swift/false.md), [`QLThumbnailGenerator`](../../qlthumbnailgenerator.md) generates a raw, undecorated thumbnail.

The default value of this property is [`false`](../../../Swift/false.md).

## See Also

### Describing the Requested Thumbnail
- [var size: CGSize](./size.md)
  The size of the thumbnails.
- [var scale: CGFloat](./scale.md)
  The pixel density of the display on the intended device.
- [var contentType: UTType!](./contenttype.md)
  The content type of the source data for the thumbnail request.
- [var representationTypes: QLThumbnailGenerator.Request.RepresentationTypes](./representationtypes-swift.property.md)
  The thumbnail sizes that you provide for a thumbnail request.
- [var minimumDimension: CGFloat](./minimumdimension.md)
  The minimum height or width for a generated thumbnail.
- [QLThumbnailGenerator.Request.RepresentationTypes](./representationtypes-swift.struct.md)
  The various types of thumbnails that you can request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailgenerator/request/iconmode)*