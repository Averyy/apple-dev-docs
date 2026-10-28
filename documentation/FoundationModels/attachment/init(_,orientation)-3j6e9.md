# init(_:orientation:)

**Framework**: Foundation Models  
**Kind**: init  
**Role**: Initializer

Creates an attachment from a pixel buffer.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(_ pixelBuffer: CVPixelBuffer, orientation: CGImagePropertyOrientation? = nil)
```

Available when `Content` is `ImageAttachmentContent`.

**Other overloads**:

```swift
init(_ cgImage: CGImage, orientation: CGImagePropertyOrientation? = nil)
```

```swift
init(_ ciImage: CIImage, orientation: CGImagePropertyOrientation? = nil)
```

```swift
init(_ nsImage: NSImage, orientation: CGImagePropertyOrientation? = nil)
```

```swift
init(_ uiImage: UIImage, orientation: UIImage.Orientation? = nil)
```

## Parameters

- `pixelBuffer`: The pixel buffer to attach.
- `orientation`: The orientation to apply to the image. Pass `nil` to use the image’s natural orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/attachment/init(_:orientation:)-3j6e9)*