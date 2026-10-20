# color

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The material’s base color.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
var color: UnlitMaterial.BaseColor { get set }
```

#### Discussion

> **Note**: The blending mode of `UnlitMaterial` materials should be configured explicitly with the [`blending`](./blending-swift.property.md) property for transparent or translucent surfaces.  The `opaque` mode is used when unset.

## See Also

### Configuring base color
- [var baseColor: MaterialColorParameter](./basecolor-swift.property.md)
  The base color of the material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/unlitmaterial/color)*