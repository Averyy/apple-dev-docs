# generateBestRepresentation(for:completion:)

**Framework**: Quick Look Thumbnailing  
**Kind**: method

Generates the best possible thumbnail representation for a file and calls a handler upon completion.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func generateBestRepresentation(for request: QLThumbnailGenerator.Request) async throws -> QLThumbnailRepresentation
```

## Mentions

- [Creating Quick Look Thumbnails to Preview Files in Your App](creating-quick-look-thumbnails-to-preview-files-in-your-app.md)

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func generateBestRepresentation(for request: QLThumbnailGenerator.Request) async throws -> QLThumbnailRepresentation
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `request`: The request that contains information about the thumbnail that you want to create.
- `completionHandler`: The completion handler takes the following parameters:

## See Also

- [func generateRepresentations(for: QLThumbnailGenerator.Request, update: ((QLThumbnailRepresentation?, QLThumbnailRepresentation.RepresentationType, (any Error)?) -> Void)?)](qlthumbnailgenerator/generaterepresentations(for:update:).md)
  Generates various thumbnail representations for a file and calls the update handler for each thumbnail representation.
- [QLThumbnailGenerator.Request](qlthumbnailgenerator/request.md)
  A request to generate a thumbnail for a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailgenerator/generatebestrepresentation(for:completion:))*