# contentType

**Framework**: Quick Look Thumbnailing  
**Kind**: property

The content type of the source data for the thumbnail request.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var contentType: UTType! { get set }
```

#### Discussion

Quick Look Thumbnailing uses the content type of the source data to determine the provider of the thumbnail and the icon styles it applies when you request [`iconMode`](qlthumbnailgenerator/request/iconmode.md).

If you don’t set this property, Quick Look Thumbnailing derives the content from the file extension. When the file doesn’t have a meaningful extension and you know the content type, set the property directly.

## See Also

- [var size: CGSize](qlthumbnailgenerator/request/size.md)
  The size of the thumbnails.
- [var scale: CGFloat](qlthumbnailgenerator/request/scale.md)
  The pixel density of the display on the intended device.
- [var representationTypes: QLThumbnailGenerator.Request.RepresentationTypes](qlthumbnailgenerator/request/representationtypes-swift.property.md)
  The thumbnail sizes that you provide for a thumbnail request.
- [var minimumDimension: CGFloat](qlthumbnailgenerator/request/minimumdimension.md)
  The minimum height or width for a generated thumbnail.
- [var iconMode: Bool](qlthumbnailgenerator/request/iconmode.md)
  A Boolean value indicating whether the generated thumbnail request should include icon decorations.
- [QLThumbnailGenerator.Request.RepresentationTypes](qlthumbnailgenerator/request/representationtypes-swift.struct.md)
  The various types of thumbnails that you can request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailgenerator/request/contenttype)*