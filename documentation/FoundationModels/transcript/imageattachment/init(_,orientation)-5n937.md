# init(_:orientation:)

**Framework**: Foundation Models  
**Kind**: init  
**Role**: Initializer

Creates an image attachment from a Core Image image.

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

**Other overloads**:

```swift
init(_ cgImage: CGImage, orientation: CGImagePropertyOrientation? = nil)
```

```swift
init(_ pixelBuffer: CVPixelBuffer, orientation: CGImagePropertyOrientation? = nil)
```

## Parameters

- `ciImage`: The Core Image image to attach.
- `orientation`: The display orientation to apply to the image, or empty to use the image’s default orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/imageattachment/init(_:orientation:)-5n937)*