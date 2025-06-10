# saveBestRepresentation(for:to:contentType:completion:)

**Framework**: Quick Look Thumbnailing  
**Kind**: method

Saves the best representation of thumbnail for a specific request to the specified URL.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func saveBestRepresentation(for request: QLThumbnailGenerator.Request, to fileURL: URL, contentType: String) async throws
```

## Mentions

- [Creating Quick Look Thumbnails to Preview Files in Your App](creating-quick-look-thumbnails-to-preview-files-in-your-app.md)

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func saveBestRepresentation(for request: QLThumbnailGenerator.Request, to fileURL: URL, contentType: String) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

Creating high-quality thumbnails often involves compressing a [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) as a `PNG` or `JPEG` file in-process. This task requires more resources than are available in resource-constrained environments such as File Provider Extensions.

Use this method to create and save the thumbnail image outside of your process as it doesn’t impose the same constraints on memory usage.

## Parameters

- `request`: The request that you used to generate a thumbnail.
- `fileURL`: The destination to which you save the generated thumbnail.
- `contentType`: The content type of the thumbnail image that you want to save. Use a type that is supported by  , such as   or  .
- `completionHandler`: The handler to call when saving the thumbnail to disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailgenerator/savebestrepresentation(for:to:contenttype:completion:))*