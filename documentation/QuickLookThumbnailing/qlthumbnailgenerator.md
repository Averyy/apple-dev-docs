# QLThumbnailGenerator

**Framework**: Quick Look Thumbnailing  
**Kind**: class

An object that generates thumbnail images based on provided requirements.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class QLThumbnailGenerator
```

## Mentions

- [Creating Quick Look Thumbnails to Preview Files in Your App](creating-quick-look-thumbnails-to-preview-files-in-your-app.md)
- [Providing Thumbnails of Your Custom File Types](providing-thumbnails-of-your-custom-file-types.md)

## Topics

### Getting the Generator Instance
- [class var shared: QLThumbnailGenerator](qlthumbnailgenerator/shared.md)
  The singleton thumbnail generator instance.
### Generating a Thumbnail
- [func generateBestRepresentation(for: QLThumbnailGenerator.Request, completion: (QLThumbnailRepresentation?, (any Error)?) -> Void)](qlthumbnailgenerator/generatebestrepresentation(for:completion:).md)
  Generates the best possible thumbnail representation for a file and calls a handler upon completion.
- [func generateRepresentations(for: QLThumbnailGenerator.Request, update: ((QLThumbnailRepresentation?, QLThumbnailRepresentation.RepresentationType, (any Error)?) -> Void)?)](qlthumbnailgenerator/generaterepresentations(for:update:).md)
  Generates various thumbnail representations for a file and calls the update handler for each thumbnail representation.
- [QLThumbnailGenerator.Request](qlthumbnailgenerator/request.md)
  A request to generate a thumbnail for a file.
### Saving a Thumbnail
- [func saveBestRepresentation(for: QLThumbnailGenerator.Request, to: URL, contentType: String, completion: ((any Error)?) -> Void)](qlthumbnailgenerator/savebestrepresentation(for:to:contenttype:completion:).md)
  Saves the best representation of thumbnail for a specific request to the specified URL.
### Canceling
- [func cancel(QLThumbnailGenerator.Request)](qlthumbnailgenerator/cancel(_:).md)
  Cancels the generation of a thumbnail for a given request.
### Instance Methods
- [func saveBestRepresentation(for: QLThumbnailGenerator.Request, to: URL, as: UTType, completion: ((any Error)?) -> Void)](qlthumbnailgenerator/savebestrepresentation(for:to:as:completion:).md)
  Saves a thumbnail for the request on disk at fileURL. The file saved at fileURL has to be deleted when it is not used anymore. This is primarily intended for file provider extensions which need to upload thumbnails and have a small memory limit.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Creating Quick Look Thumbnails to Preview Files in Your App](creating-quick-look-thumbnails-to-preview-files-in-your-app.md)
  Generate thumbnails of images, text files, PDFs, audio files, videos, and more.
- [class QLThumbnailRepresentation](qlthumbnailrepresentation.md)
  Information about the thumbnail that the thumbnail generator returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailgenerator)*