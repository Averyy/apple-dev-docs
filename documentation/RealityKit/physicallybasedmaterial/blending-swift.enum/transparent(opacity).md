# PhysicallyBasedMaterial.Blending.transparent(opacity:)

**Framework**: RealityKit  
**Kind**: case  
**Role**: Case

A surface that’s transparent.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
case transparent(opacity: PhysicallyBasedMaterial.Opacity)
```

#### Discussion

This enumeration case indicates that the material supports transparency.

## Parameters

- `opacity`: The opacity of the material.

## See Also

### Specifying opacity
- [PhysicallyBasedMaterial.Blending.opaque](./opaque.md)
  An opaque surface.
- [var opacityThreshold: Float?](../opacitythreshold.md)
  A threshold below which RealityKit ignores opacity.
- [PhysicallyBasedMaterial.Opacity](../opacity.md)
  An object that defines the opacity of an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/blending-swift.enum/transparent(opacity:))*