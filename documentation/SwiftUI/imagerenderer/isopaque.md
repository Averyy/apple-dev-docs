# isOpaque

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the alpha channel of the image is fully opaque.

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
final var isOpaque: Bool { get set }
```

#### Discussion

Setting this value to `true`, meaning the alpha channel is opaque, may improve performance. Don’t render non-opaque pixels to a renderer declared as opaque. This property defaults to `false`.

## See Also

### Accessing renderer properties
- [var proposedSize: ProposedViewSize](./proposedsize.md)
  The size proposed to the root view.
- [var scale: CGFloat](./scale.md)
  The scale at which to render the image.
- [var colorMode: ColorRenderingMode](./colormode.md)
  The working color space and storage format of the image.
- [var allowedDynamicRange: Image.DynamicRange?](./alloweddynamicrange.md)
  The allowed dynamic range of the image, or nil to mark that the dynamic range of the image should be unrestricted. This property defaults to `sdr`, i.e. HDR content will be tone mapped to SDR.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/imagerenderer/isopaque)*