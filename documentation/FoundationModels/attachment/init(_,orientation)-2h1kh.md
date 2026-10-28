# init(_:orientation:)

**Framework**: Foundation Models  
**Kind**: init  
**Role**: Initializer

Creates an attachment from a Core Image image.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(_ ciImage: CIImage, orientation: CGImagePropertyOrientation? = nil)
```

Available when `Content` is `ImageAttachmentContent`.

**Other overloads**:

```swift
init(_ cgImage: CGImage, orientation: CGImagePropertyOrientation? = nil)
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

- `ciImage`: The image to attach.
- `orientation`: The orientation to apply to the image. Pass `nil` to use the image’s natural orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/attachment/init(_:orientation:)-2h1kh)*