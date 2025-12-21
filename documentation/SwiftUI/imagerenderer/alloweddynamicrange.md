# allowedDynamicRange

**Framework**: SwiftUI  
**Kind**: property

The allowed dynamic range of the image, or nil to mark that the dynamic range of the image should be unrestricted. This property defaults to `sdr`, i.e. HDR content will be tone mapped to SDR.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
final var allowedDynamicRange: Image.DynamicRange? { get set }
```

## See Also

- [var proposedSize: ProposedViewSize](imagerenderer/proposedsize.md)
  The size proposed to the root view.
- [var scale: CGFloat](imagerenderer/scale.md)
  The scale at which to render the image.
- [var isOpaque: Bool](imagerenderer/isopaque.md)
  A Boolean value that indicates whether the alpha channel of the image is fully opaque.
- [var colorMode: ColorRenderingMode](imagerenderer/colormode.md)
  The working color space and storage format of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/imagerenderer/alloweddynamicrange)*