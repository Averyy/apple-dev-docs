# resolutionMetric(switchingResolutions:boundingBox:)

**Framework**: RealityKit  
**Kind**: method

Creates a resolution metric for a level of detail component to switch with.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func resolutionMetric(switchingResolutions: [LevelOfDetailComponent.SelectionStrategy.ResolutionMetric.DirectionalSwitchingResolutions], boundingBox: BoundingBox) -> LevelOfDetailComponent.SelectionStrategy
```

#### Return Value

A configured resolution metric selection strategy.

## Parameters

- `switchingResolutions`: An array of `ResolutionMetric.DirectionalSwitchingResolutions`. The `ResolutionMetric.DirectionalSwitchingResolutions` at index `i` corresponds to the LOD level `i + 1`.
- `boundingBox`: The bounding box of the entity used when calculating the switching resolutions .

## See Also

- [LevelOfDetailComponent.SelectionStrategy.ResolutionMetric](levelofdetailcomponent/selectionstrategy/resolutionmetric.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/levelofdetailcomponent/selectionstrategy/resolutionmetric(switchingresolutions:boundingbox:))*