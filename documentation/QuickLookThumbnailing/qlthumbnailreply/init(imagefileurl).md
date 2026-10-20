# init(imageFileURL:)

**Framework**: Quick Look Thumbnailing  
**Kind**: init  
**Role**: Initializer

Creates a new thumbnail for a custom file type using a file at the given URL.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
convenience init(imageFileURL fileURL: URL)
```

```objc
+ (instancetype) replyWithImageFileURL:(NSURL *) fileURL;
```

#### Return Value

An initialized reply object for a requested thumbnail.

#### Discussion

The image is scaled down to fit the provided size by the [`QLFileThumbnailRequest`](../qlfilethumbnailrequest.md) if necessary.

## Parameters

- `fileURL`: The URL to the file that is used as the thumbnail.

## See Also

### Creating a Thumbnail
- [convenience init(contextSize: CGSize, currentContextDrawing: () -> Bool)](./init%28contextsize,currentcontextdrawing%29.md)
  Creates a new thumbnail for a custom file type in the current context.
- [convenience init(contextSize: CGSize, drawing: (CGContext) -> Bool)](./init%28contextsize,drawing%29.md)
  Creates a new thumbnail for a custom file type in the given context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailreply/init(imagefileurl:))*