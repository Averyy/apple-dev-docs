# colorMode

**Framework**: SwiftUI  
**Kind**: property

The working color space and storage format of the image.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@MainActor
final var colorMode: ColorRenderingMode { get set }
```

## See Also

- [var proposedSize: ProposedViewSize](imagerenderer/proposedsize.md)
  The size proposed to the root view.
- [var scale: CGFloat](imagerenderer/scale.md)
  The scale at which to render the image.
- [var isOpaque: Bool](imagerenderer/isopaque.md)
  A Boolean value that indicates whether the alpha channel of the image is fully opaque.
- [var allowedDynamicRange: Image.DynamicRange?](imagerenderer/alloweddynamicrange.md)
  The allowed dynamic range of the image, or nil to mark that the dynamic range of the image should be unrestricted. This property defaults to `sdr`, i.e. HDR content will be tone mapped to SDR.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/imagerenderer/colormode)*