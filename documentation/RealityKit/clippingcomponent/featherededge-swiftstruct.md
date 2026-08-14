# ClippingComponent.FeatheredEdge

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
struct FeatheredEdge
```

#### Overview

Feathering is defined separately for positive and negative edges of each axis, providing fine-grained control over how content fades out near the clipping bounds.

## Topics

### Creating a feathered edge
- [init(symmetricEdgeInset: SIMD3<Float>, falloff: ClippingComponent.FeatheredEdge.Falloff)](clippingcomponent/featherededge-swift.struct/init(symmetricedgeinset:falloff:).md)
  Initializes both [`positiveEdgeInset`](clippingcomponent/featherededge-swift.struct/positiveedgeinset.md) and [`negativeEdgeInset`](clippingcomponent/featherededge-swift.struct/negativeedgeinset.md) with the same symmetric value.
### Configuring edge insets
- [var positiveEdgeInset: SIMD3<Float>](clippingcomponent/featherededge-swift.struct/positiveedgeinset.md)
  The distance from each positive edge (+X, +Y, +Z) of the clip bounds over which opacity fades to 0, expressed in local coordinate space units.
- [var negativeEdgeInset: SIMD3<Float>](clippingcomponent/featherededge-swift.struct/negativeedgeinset.md)
  The distance from each negative edge (-X, -Y, -Z) of the clip bounds over which opacity fades to 0, expressed in local coordinate space units.
### Controlling the falloff
- [var falloff: ClippingComponent.FeatheredEdge.Falloff](clippingcomponent/featherededge-swift.struct/falloff-swift.property.md)
  The falloff function used for the feathered edge computation.
- [ClippingComponent.FeatheredEdge.Falloff](clippingcomponent/featherededge-swift.struct/falloff-swift.enum.md)
### Type Properties
- [static var none: ClippingComponent.FeatheredEdge](clippingcomponent/featherededge-swift.struct/none.md)

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)

## See Also

- [var featheredEdge: ClippingComponent.FeatheredEdge](clippingcomponent/featherededge-swift.property.md)
  The feathering configuration for the clipping boundaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clippingcomponent/featherededge-swift.struct)*