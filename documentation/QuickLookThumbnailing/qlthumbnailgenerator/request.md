# QLThumbnailGenerator.Request

**Framework**: Quick Look Thumbnailing  
**Kind**: class  
**Role**: Class

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

```objc
@interface QLThumbnailGenerationRequest : NSObject
```

## Topics

### Creating a Thumbail Request
- [init(fileAt: URL, size: CGSize, scale: CGFloat, representationTypes: QLThumbnailGenerator.Request.RepresentationTypes)](./request/init%28fileat,size,scale,representationtypes%29.md)
  Creates a new request for a thumbnail with the specified parameters for a file at a provided URL.
### Describing the Requested Thumbnail
- [var size: CGSize](./request/size.md)
  The size of the thumbnails.
- [var scale: CGFloat](./request/scale.md)
  The pixel density of the display on the intended device.
- [var contentType: UTType!](./request/contenttype.md)
  The content type of the source data for the thumbnail request.
- [var representationTypes: QLThumbnailGenerator.Request.RepresentationTypes](./request/representationtypes-swift.property.md)
  The thumbnail sizes that you provide for a thumbnail request.
- [var minimumDimension: CGFloat](./request/minimumdimension.md)
  The minimum height or width for a generated thumbnail.
- [var iconMode: Bool](./request/iconmode.md)
  A Boolean value indicating whether the generated thumbnail request should include icon decorations.
- [QLThumbnailGenerator.Request.RepresentationTypes](./request/representationtypes-swift.struct.md)
  The various types of thumbnails that you can request.
### Initializers
- [init?(coder: NSCoder)](./request/init%28coder%29.md)
- [init(fileAtURL: URL, size: CGSize, scale: CGFloat, representationTypes: QLThumbnailGenerator.Request.RepresentationTypes)](./request/init%28fileaturl,size,scale,representationtypes%29.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCoding](../../Foundation/nscoding.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../../Foundation/nssecurecoding.md)

## See Also

### Generating a Thumbnail
- [func generateBestRepresentation(for: QLThumbnailGenerator.Request, completion: (QLThumbnailRepresentation?, (any Error)?) -> Void)](./generatebestrepresentation%28for,completion%29.md)
  Generates the best possible thumbnail representation for a file and calls a handler upon completion.
- [func generateRepresentations(for: QLThumbnailGenerator.Request, update: ((QLThumbnailRepresentation?, QLThumbnailRepresentation.RepresentationType, (any Error)?) -> Void)?)](./generaterepresentations%28for,update%29.md)
  Generates various thumbnail representations for a file and calls the update handler for each thumbnail representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailgenerator/request)*