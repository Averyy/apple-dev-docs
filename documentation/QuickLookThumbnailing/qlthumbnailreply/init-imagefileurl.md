# init(imageFileURL:)

**Framework**: Quick Look Thumbnailing  
**Kind**: init

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

#### Return Value

An initialized reply object for a requested thumbnail.

#### Discussion

The image is scaled down to fit the provided size by the [`QLFileThumbnailRequest`](qlfilethumbnailrequest.md) if necessary.

## Parameters

- `fileURL`: The URL to the file that is used as the thumbnail.

## See Also

- [convenience init(contextSize: CGSize, currentContextDrawing: () -> Bool)](qlthumbnailreply/init(contextsize:currentcontextdrawing:).md)
  Creates a new thumbnail for a custom file type in the current context.
- [convenience init(contextSize: CGSize, drawing: (CGContext) -> Bool)](qlthumbnailreply/init(contextsize:drawing:).md)
  Creates a new thumbnail for a custom file type in the given context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailreply/init(imagefileurl:))*