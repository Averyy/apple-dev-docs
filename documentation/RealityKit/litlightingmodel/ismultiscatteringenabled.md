# isMultiscatteringEnabled

**Framework**: RealityKit  
**Kind**: property

Whether to account for multiple scattering between microfacets.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var isMultiscatteringEnabled: Bool
```

#### Discussion

Improves accuracy at the cost of performance, particularly for rough surfaces.

## See Also

- [var isSubsurfaceScatteringEnabled: Bool](litlightingmodel/issubsurfacescatteringenabled.md)
  Whether to include subsurface scattering in the lighting calculation.
- [var isClearcoatEnabled: Bool](litlightingmodel/isclearcoatenabled.md)
  Whether to include a clearcoat layer in the lighting calculation.
- [var isBentNormalEnabled: Bool](litlightingmodel/isbentnormalenabled.md)
  Whether to apply bent normal maps to improve ambient occlusion accuracy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/litlightingmodel/ismultiscatteringenabled)*