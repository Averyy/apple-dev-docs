# representationTypes

**Framework**: Quick Look Thumbnailing  
**Kind**: property  
**Role**: Instance Property

The thumbnail sizes that you provide for a thumbnail request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var representationTypes: QLThumbnailGenerator.Request.RepresentationTypes { get }
```

```objc
@property (nonatomic, readonly) QLThumbnailGenerationRequestRepresentationTypes representationTypes;
```

#### Discussion

The representation types provide access to icon, low-quality, and high-quality thumbnails so you can request and show a lower-quality thumbnail quickly while computing a higher-quality thumbnail in the background.

## See Also

### Describing the Requested Thumbnail
- [var size: CGSize](./size.md)
  The size of the thumbnails.
- [var scale: CGFloat](./scale.md)
  The pixel density of the display on the intended device.
- [var contentType: UTType!](./contenttype.md)
  The content type of the source data for the thumbnail request.
- [var minimumDimension: CGFloat](./minimumdimension.md)
  The minimum height or width for a generated thumbnail.
- [var iconMode: Bool](./iconmode.md)
  A Boolean value indicating whether the generated thumbnail request should include icon decorations.
- [QLThumbnailGenerator.Request.RepresentationTypes](./representationtypes-swift.struct.md)
  The various types of thumbnails that you can request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailgenerator/request/representationtypes-swift.property)*