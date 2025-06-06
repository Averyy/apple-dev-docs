# opacityThreshold

**Framework**: Realitykit  
**Kind**: property

A threshold below which RealityKit ignores opacity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
var opacityThreshold: Float? { get set }
```

#### Discussion

When `opacityThreshold` is set, RealityKit discards pixels with opacity values less than the `opacityThreshold`, and renders opacity values greater than or equal to `opacityThreshold` fully opaque.

> **Note**: When the `opacityThreshold` property is set, the blend mode of the [`blending`](unlitmaterial/blending-swift.property.md) property is ignored and the renderer applies the masking behavior.

## See Also

- [var blending: UnlitMaterial.Blending](unlitmaterial/blending-swift.property.md)
  The transparency options for the material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/unlitmaterial/opacitythreshold)*