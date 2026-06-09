# fractionPerNegativeEdge

**Framework**: RealityKit  
**Kind**: property

Feather interval over which opacity lerps to 0 for negative edges (i.e -X, -Y, -Z) of the clip bounds. Expressed as a fraction of the smallest dimension of the clipping volume Values range from `0.0` to `1.0`:

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var fractionPerNegativeEdge: SIMD3<Float>
```

#### Discussion

- `0.0` means no feathering on that edge
- `0.1` means fade across 10% of the bounding box dimension in the negative axes
- `1.0` means the feather zone extends across the entire negative box dimension

## See Also

- [var falloff: ClippingPrimitiveComponent.Feather.Falloff](clippingprimitivecomponent/feather-swift.struct/falloff-swift.property.md)
  The falloff function used for the feathering computation.
- [ClippingPrimitiveComponent.Feather.Falloff](clippingprimitivecomponent/feather-swift.struct/falloff-swift.enum.md)
- [var fractionPerPositiveEdge: SIMD3<Float>](clippingprimitivecomponent/feather-swift.struct/fractionperpositiveedge.md)
  Feather interval over which opacity lerps to 0 for positive edges (i.e +X, +Y, +Z) of the clip bounds. Expressed as a fraction of the smallest dimension of the clipping volume Values range from `0.0` to `1.0`:


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clippingprimitivecomponent/feather-swift.struct/fractionpernegativeedge)*