# minimumDimension

**Framework**: Quick Look Thumbnailing  
**Kind**: property  
**Role**: Instance Property

The minimum height or width for a generated thumbnail.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var minimumDimension: CGFloat { get set }
```

```objc
@property (nonatomic, assign) CGFloat minimumDimension;
```

## Discussion

This property defines a minimum dimension for a generated thumbnail, returning a thumbnail with a width or height greater or equal to the value of `minimumDimension` * [`scale`](./scale.md).

The default value for this property is `0`.

If you set this property, and the system can’t generate a thumbnail of `minimumDimension` for any of the requested types represented by [`QLThumbnailGenerator.Request.RepresentationTypes`](./representationtypes-swift.struct.md), then [`QLThumbnailGenerator`](../../qlthumbnailgenerator.md) doesn’t generate a thumbnail.

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
- [var iconMode: Bool](./iconmode.md)
  A Boolean value indicating whether the generated thumbnail request should include icon decorations.
- [QLThumbnailGenerator.Request.RepresentationTypes](./representationtypes-swift.struct.md)
  The various types of thumbnails that you can request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailgenerator/request/minimumdimension)*