# LevelOfDetailComponent.SelectionStrategy.ResolutionMetric

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct ResolutionMetric
```

## Topics

### Creating a resolution metric
- [init(switchingResolutions: [LevelOfDetailComponent.SelectionStrategy.ResolutionMetric.DirectionalSwitchingResolutions], boundingBox: BoundingBox)](./resolutionmetric/init%28switchingresolutions,boundingbox%29.md)
  Creates a resolution metric for a level of detail component to switch with.
### Configuring the metric
- [var switchingResolutions: [LevelOfDetailComponent.SelectionStrategy.ResolutionMetric.DirectionalSwitchingResolutions]](./resolutionmetric/switchingresolutions.md)
- [LevelOfDetailComponent.SelectionStrategy.ResolutionMetric.DirectionalSwitchingResolutions](./resolutionmetric/directionalswitchingresolutions.md)
  A struct containing the ideal switching resolutions for a single detail level in a `LevelOfDetailComponent` when viewed from a specific direction. Note that switching may not actually occur at these resolutions depending on device performance.
- [let boundingBox: BoundingBox](./resolutionmetric/boundingbox.md)

## See Also

### Selecting by resolution metric
- [static func resolutionMetric(switchingResolutions: [LevelOfDetailComponent.SelectionStrategy.ResolutionMetric.DirectionalSwitchingResolutions], boundingBox: BoundingBox) -> LevelOfDetailComponent.SelectionStrategy](./resolutionmetric%28switchingresolutions,boundingbox%29.md)
  Creates a resolution metric for a level of detail component to switch with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/levelofdetailcomponent/selectionstrategy/resolutionmetric)*