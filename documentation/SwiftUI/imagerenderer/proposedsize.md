# proposedSize

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The size proposed to the root view.

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
final var proposedSize: ProposedViewSize { get set }
```

#### Discussion

The default value of this property, [`unspecified`](../proposedviewsize/unspecified.md), produces an image that matches the original view size. You can provide a custom [`ProposedViewSize`](../proposedviewsize.md) to override the view’s size in one or both dimensions.

## See Also

### Accessing renderer properties
- [var scale: CGFloat](./scale.md)
  The scale at which to render the image.
- [var isOpaque: Bool](./isopaque.md)
  A Boolean value that indicates whether the alpha channel of the image is fully opaque.
- [var colorMode: ColorRenderingMode](./colormode.md)
  The working color space and storage format of the image.
- [var allowedDynamicRange: Image.DynamicRange?](./alloweddynamicrange.md)
  The allowed dynamic range of the image, or nil to mark that the dynamic range of the image should be unrestricted. This property defaults to `sdr`, i.e. HDR content will be tone mapped to SDR.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/imagerenderer/proposedsize)*