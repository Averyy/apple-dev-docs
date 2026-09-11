# init(_:orientation:)

**Framework**: Foundation Models  
**Kind**: init

Creates an attachment from a Core Graphics image.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(_ cgImage: CGImage, orientation: CGImagePropertyOrientation? = nil)
```

## Parameters

- `cgImage`: The image to attach.
- `orientation`: The orientation to apply to the image. Pass `nil` to use the image’s natural orientation.

## See Also

- [init(imageURL: URL, orientation: CGImagePropertyOrientation?)](attachment/init(imageurl:orientation:).md)
  Creates an attachment from a file URL pointing to an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/attachment/init(_:orientation:))*