# falloff

**Framework**: RealityKit  
**Kind**: property

The falloff function used for the feathering computation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var falloff: ClippingPrimitiveComponent.Feather.Falloff
```

## See Also

- [ClippingPrimitiveComponent.Feather.Falloff](clippingprimitivecomponent/feather-swift.struct/falloff-swift.enum.md)
- [var fractionPerPositiveEdge: SIMD3<Float>](clippingprimitivecomponent/feather-swift.struct/fractionperpositiveedge.md)
  Feather interval over which opacity lerps to 0 for positive edges (i.e +X, +Y, +Z) of the clip bounds. Expressed as a fraction of the smallest dimension of the clipping volume Values range from `0.0` to `1.0`:
- [var fractionPerNegativeEdge: SIMD3<Float>](clippingprimitivecomponent/feather-swift.struct/fractionpernegativeedge.md)
  Feather interval over which opacity lerps to 0 for negative edges (i.e -X, -Y, -Z) of the clip bounds. Expressed as a fraction of the smallest dimension of the clipping volume Values range from `0.0` to `1.0`:


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clippingprimitivecomponent/feather-swift.struct/falloff-swift.property)*