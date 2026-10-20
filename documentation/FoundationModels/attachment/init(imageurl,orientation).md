# init(imageURL:orientation:)

**Framework**: Foundation Models  
**Kind**: init  
**Role**: Initializer

Creates an attachment from a file URL pointing to an image.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(imageURL: URL, orientation: CGImagePropertyOrientation? = nil)
```

Available when `Content` is `ImageAttachmentContent`.

## Parameters

- `imageURL`: A URL to the image file to attach.
- `orientation`: The orientation to apply to the image. Pass `nil` to use the image’s natural orientation.

## See Also

### Creating an attachment instance
- [init(_:orientation:)](./init%28_,orientation%29.md)
  Creates an attachment from a Core Graphics image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/attachment/init(imageurl:orientation:))*