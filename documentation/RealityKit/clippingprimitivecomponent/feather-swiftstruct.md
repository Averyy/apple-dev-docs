# ClippingPrimitiveComponent.Feather

**Framework**: RealityKit  
**Kind**: struct

Configuration for feathering the clipping boundaries.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Feather
```

#### Overview

Feathering is defined separately for positive and negative edges of each axis, providing fine-grained control over how content fades out near the clipping bounds.

## Topics

### Configuring the feather effect
- [var falloff: ClippingPrimitiveComponent.Feather.Falloff](clippingprimitivecomponent/feather-swift.struct/falloff-swift.property.md)
  The falloff function used for the feathering computation.
- [ClippingPrimitiveComponent.Feather.Falloff](clippingprimitivecomponent/feather-swift.struct/falloff-swift.enum.md)
- [var fractionPerPositiveEdge: SIMD3<Float>](clippingprimitivecomponent/feather-swift.struct/fractionperpositiveedge.md)
  Feather interval over which opacity lerps to 0 for positive edges (i.e +X, +Y, +Z) of the clip bounds. Expressed as a fraction of the smallest dimension of the clipping volume Values range from `0.0` to `1.0`:
- [var fractionPerNegativeEdge: SIMD3<Float>](clippingprimitivecomponent/feather-swift.struct/fractionpernegativeedge.md)
  Feather interval over which opacity lerps to 0 for negative edges (i.e -X, -Y, -Z) of the clip bounds. Expressed as a fraction of the smallest dimension of the clipping volume Values range from `0.0` to `1.0`:
### Initializers
- [init()](clippingprimitivecomponent/feather-swift.struct/init.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [var feather: ClippingPrimitiveComponent.Feather](clippingprimitivecomponent/feather-swift.property.md)
  The feathering configuration for the clipping boundaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clippingprimitivecomponent/feather-swift.struct)*