# provideThumbnail(for:_:)

**Framework**: Quick Look Thumbnailing  
**Kind**: method

Creates a thumbnail of a custom file type for a specific request.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func provideThumbnail(for request: QLFileThumbnailRequest, _ handler: @escaping (QLThumbnailReply?, (any Error)?) -> Void)
```

## Mentions

- [Providing Thumbnails of Your Custom File Types](providing-thumbnails-of-your-custom-file-types.md)

#### Discussion

To provide a thumbnail for a custom file type, subclass [`QLThumbnailProvider`](qlthumbnailprovider.md), implement this method, and return a [`QLThumbnailReply`](qlthumbnailreply.md) that either contains a drawing block or the URL to an image file.

## Parameters

- `request`: The request that contains information about the thumbnail that you need to provide, such as the URL to the file.
- `handler`: The completion handler to call when you finish creating a thumbnail. Call the completion handler with a [`QLThumbnailReply`](qlthumbnailreply.md) if you can provide a thumbnail or with an [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) if you can’t create a thumbnail. The platform doesn’t draw a thumbnail if you pass an `error` to the handler or the `reply` is `nil.` You can call the handler asynchronously after the method has returned. - **`reply`**: The object containing information about the  thumbnail image that the platform uses to draw the thumbnail.
- **`error`**: An error object that indicates why the thumbnail generation failed, or `nil` if the thumbnail generation succeeded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailprovider/providethumbnail(for:_:))*