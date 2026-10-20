# size

**Framework**: Quick Look Thumbnailing  
**Kind**: property  
**Role**: Instance Property

The size of the thumbnails.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var size: CGSize { get }
```

```objc
@property (nonatomic, readonly) CGSize size;
```

## See Also

### Describing the Requested Thumbnail
- [var scale: CGFloat](./scale.md)
  The pixel density of the display on the intended device.
- [var contentType: UTType!](./contenttype.md)
  The content type of the source data for the thumbnail request.
- [var representationTypes: QLThumbnailGenerator.Request.RepresentationTypes](./representationtypes-swift.property.md)
  The thumbnail sizes that you provide for a thumbnail request.
- [var minimumDimension: CGFloat](./minimumdimension.md)
  The minimum height or width for a generated thumbnail.
- [var iconMode: Bool](./iconmode.md)
  A Boolean value indicating whether the generated thumbnail request should include icon decorations.
- [QLThumbnailGenerator.Request.RepresentationTypes](./representationtypes-swift.struct.md)
  The various types of thumbnails that you can request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailgenerator/request/size)*