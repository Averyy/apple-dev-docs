# QLThumbnailGenerator.Request

**Framework**: Quick Look Thumbnailing  
**Kind**: class

A request to generate a thumbnail for a file.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class Request
```

## Topics

### Creating a Thumbail Request
- [init(fileAt: URL, size: CGSize, scale: CGFloat, representationTypes: QLThumbnailGenerator.Request.RepresentationTypes)](qlthumbnailgenerator/request/init(fileat:size:scale:representationtypes:).md)
  Creates a new request for a thumbnail with the specified parameters for a file at a provided URL.
### Describing the Requested Thumbnail
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
- [var iconMode: Bool](qlthumbnailgenerator/request/iconmode.md)
  A Boolean value indicating whether the generated thumbnail request should include icon decorations.
- [QLThumbnailGenerator.Request.RepresentationTypes](qlthumbnailgenerator/request/representationtypes-swift.struct.md)
  The various types of thumbnails that you can request.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [func generateBestRepresentation(for: QLThumbnailGenerator.Request, completion: (QLThumbnailRepresentation?, (any Error)?) -> Void)](qlthumbnailgenerator/generatebestrepresentation(for:completion:).md)
  Generates the best possible thumbnail representation for a file and calls a handler upon completion.
- [func generateRepresentations(for: QLThumbnailGenerator.Request, update: ((QLThumbnailRepresentation?, QLThumbnailRepresentation.RepresentationType, (any Error)?) -> Void)?)](qlthumbnailgenerator/generaterepresentations(for:update:).md)
  Generates various thumbnail representations for a file and calls the update handler for each thumbnail representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailgenerator/request)*