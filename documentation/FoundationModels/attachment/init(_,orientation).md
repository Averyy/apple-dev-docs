# init(_:orientation:)

**Framework**: Foundation Models  
**Kind**: init  
**Role**: Initializer

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

Available when `Content` is `ImageAttachmentContent`.

**Other overloads**:

```swift
init(_ ciImage: CIImage, orientation: CGImagePropertyOrientation? = nil)
```

```swift
init(_ nsImage: NSImage, orientation: CGImagePropertyOrientation? = nil)
```

```swift
init(_ pixelBuffer: CVPixelBuffer, orientation: CGImagePropertyOrientation? = nil)
```

```swift
init(_ uiImage: UIImage, orientation: UIImage.Orientation? = nil)
```

## Parameters

- `cgImage`: The image to attach.
- `orientation`: The orientation to apply to the image. Pass `nil` to use the image’s natural orientation.

## See Also

### Creating an attachment instance
- [init(imageURL: URL, orientation: CGImagePropertyOrientation?)](./init%28imageurl,orientation%29.md)
  Creates an attachment from a file URL pointing to an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/attachment/init(_:orientation:))*