# init(switchingResolutions:boundingBox:)

**Framework**: RealityKit  
**Kind**: init

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
init(switchingResolutions: [LevelOfDetailComponent.SelectionStrategy.ResolutionMetric.DirectionalSwitchingResolutions], boundingBox: BoundingBox)
```

## Parameters

- `switchingResolutions`: An array of `DirectionalSwitchingResolutions`. The `DirectionalSwitchingResolutions` at index `i` corresponds to the LOD level `i + 1`.
- `boundingBox`: The bounding box of the entity used when calculating the switching resolutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/levelofdetailcomponent/selectionstrategy/resolutionmetric/init(switchingresolutions:boundingbox:))*