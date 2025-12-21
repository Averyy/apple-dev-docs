# opacityThreshold

**Framework**: RealityKit  
**Kind**: property

A threshold below which RealityKit ignores opacity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
var opacityThreshold: Float? { get set }
```

## Mentions

- [Applying realistic material and lighting effects to entities](applying-realistic-material-and-lighting-effects-to-entities.md)

#### Discussion

When `opacityThreshold` is set, RealityKit discards pixels with opacity values less than the `opacityThreshold`, and renders opacity values greater than or equal to `opacityThreshold` fully opaque.

> **Note**: When the `opacityThreshold` property is set, the blend mode of the [`blending`](physicallybasedmaterial/blending-swift.property.md) property is ignored and the renderer applies the masking behavior.

## See Also

- [PhysicallyBasedMaterial.Blending.opaque](physicallybasedmaterial/blending-swift.enum/opaque.md)
  An opaque surface.
- [case transparent(opacity: PhysicallyBasedMaterial.Opacity)](physicallybasedmaterial/blending-swift.enum/transparent(opacity:).md)
  A surface that’s transparent.
- [PhysicallyBasedMaterial.Opacity](physicallybasedmaterial/opacity.md)
  An object that defines the opacity of an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/opacitythreshold)*