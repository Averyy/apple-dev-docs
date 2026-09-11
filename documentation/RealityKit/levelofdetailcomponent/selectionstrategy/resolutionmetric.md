# LevelOfDetailComponent.SelectionStrategy.ResolutionMetric

**Framework**: RealityKit  
**Kind**: struct

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
- [init(switchingResolutions: [LevelOfDetailComponent.SelectionStrategy.ResolutionMetric.DirectionalSwitchingResolutions], boundingBox: BoundingBox)](levelofdetailcomponent/selectionstrategy/resolutionmetric/init(switchingresolutions:boundingbox:).md)
  Creates a resolution metric for a level of detail component to switch with.
### Configuring the metric
- [var switchingResolutions: [LevelOfDetailComponent.SelectionStrategy.ResolutionMetric.DirectionalSwitchingResolutions]](levelofdetailcomponent/selectionstrategy/resolutionmetric/switchingresolutions.md)
- [LevelOfDetailComponent.SelectionStrategy.ResolutionMetric.DirectionalSwitchingResolutions](levelofdetailcomponent/selectionstrategy/resolutionmetric/directionalswitchingresolutions.md)
  A struct containing the ideal switching resolutions for a single detail level in a `LevelOfDetailComponent` when viewed from a specific direction. Note that switching may not actually occur at these resolutions depending on device performance.
- [let boundingBox: BoundingBox](levelofdetailcomponent/selectionstrategy/resolutionmetric/boundingbox.md)

## See Also

- [static func resolutionMetric(switchingResolutions: [LevelOfDetailComponent.SelectionStrategy.ResolutionMetric.DirectionalSwitchingResolutions], boundingBox: BoundingBox) -> LevelOfDetailComponent.SelectionStrategy](levelofdetailcomponent/selectionstrategy/resolutionmetric(switchingresolutions:boundingbox:).md)
  Creates a resolution metric for a level of detail component to switch with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/levelofdetailcomponent/selectionstrategy/resolutionmetric)*