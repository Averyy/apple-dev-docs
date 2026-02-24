# generateRepresentations(for:update:)

**Framework**: Quick Look Thumbnailing  
**Kind**: method

Generates various thumbnail representations for a file and calls the update handler for each thumbnail representation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func generateRepresentations(for request: QLThumbnailGenerator.Request, update updateHandler: ((QLThumbnailRepresentation?, QLThumbnailRepresentation.RepresentationType, (any Error)?) -> Void)? = nil)
```

## Mentions

- [Creating Quick Look Thumbnails to Preview Files in Your App](creating-quick-look-thumbnails-to-preview-files-in-your-app.md)

#### Discussion

Use this method if you want to create a file icon or low-quality thumbnail quickly, and replace it with a higher quality thumbnail once it becomes available.

## Parameters

- `request`: The request that contains information about the thumbnail that you want to create.
- `updateHandler`: The handler to call successively for each requested representation of a thumbnail. QuickLookThumbnailing calls the `updateHandler` in order of lower quality to higher quality thumbnail types. If a better quality thumbnail becomes available before a lower quality one, the framework may skip the call to the `updateHandler` for the lower quality thumbnail. You can rely on QuickLookThumbnailing to call the `updateHandler` at least once by the time it finishes the creation of thumbnails with either the best requested thumbnail, or an error object. The handler takes the following parameters: - **`thumbnail`**: A thumbnail that is successfully generated or `nil` if `QLThumbnailGenerator` is unable to generate a thumbnail.
- **`type`**: The type of the generated thumbnail representation.
- **`error`**: An error object that indicates why the thumbnail generation failed, or `nil` if the thumbnail generation succeeded.

## See Also

- [func generateBestRepresentation(for: QLThumbnailGenerator.Request, completion: (QLThumbnailRepresentation?, (any Error)?) -> Void)](qlthumbnailgenerator/generatebestrepresentation(for:completion:).md)
  Generates the best possible thumbnail representation for a file and calls a handler upon completion.
- [QLThumbnailGenerator.Request](qlthumbnailgenerator/request.md)
  A request to generate a thumbnail for a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailgenerator/generaterepresentations(for:update:))*