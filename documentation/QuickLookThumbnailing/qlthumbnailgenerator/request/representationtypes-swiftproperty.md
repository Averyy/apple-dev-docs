# representationTypes

**Framework**: Quick Look Thumbnailing  
**Kind**: property

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

#### Discussion

The representation types provide access to icon, low-quality, and high-quality thumbnails so you can request and show a lower-quality thumbnail quickly while computing a higher-quality thumbnail in the background.

## See Also

- [var size: CGSize](qlthumbnailgenerator/request/size.md)
  The size of the thumbnails.
- [var scale: CGFloat](qlthumbnailgenerator/request/scale.md)
  The pixel density of the display on the intended device.
- [var contentType: UTType!](qlthumbnailgenerator/request/contenttype.md)
  The content type of the source data for the thumbnail request.
- [var minimumDimension: CGFloat](qlthumbnailgenerator/request/minimumdimension.md)
  The minimum height or width for a generated thumbnail.
- [var iconMode: Bool](qlthumbnailgenerator/request/iconmode.md)
  A Boolean value indicating whether the generated thumbnail request should include icon decorations.
- [QLThumbnailGenerator.Request.RepresentationTypes](qlthumbnailgenerator/request/representationtypes-swift.struct.md)
  The various types of thumbnails that you can request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailgenerator/request/representationtypes-swift.property)*