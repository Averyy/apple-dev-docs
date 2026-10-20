# LevelOfDetailComponent.SelectionStrategy.ResolutionMetric.DirectionalSwitchingResolutions

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A struct containing the ideal switching resolutions for a single detail level in a `LevelOfDetailComponent` when viewed from a specific direction. Note that switching may not actually occur at these resolutions depending on device performance.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct DirectionalSwitchingResolutions
```

## Topics

### Creating switching resolutions
- [init(positiveX: Float, negativeX: Float, positiveY: Float, negativeY: Float, positiveZ: Float, negativeZ: Float)](./directionalswitchingresolutions/init%28positivex,negativex,positivey,negativey,positivez,negativez%29.md)
### Setting axis resolutions
- [var positiveX: Float](./directionalswitchingresolutions/positivex.md)
- [var negativeX: Float](./directionalswitchingresolutions/negativex.md)
- [var positiveY: Float](./directionalswitchingresolutions/positivey.md)
- [var negativeY: Float](./directionalswitchingresolutions/negativey.md)
- [var positiveZ: Float](./directionalswitchingresolutions/positivez.md)
- [var negativeZ: Float](./directionalswitchingresolutions/negativez.md)
### Initializers
- [init()](./directionalswitchingresolutions/init%28%29.md)
  Creates an empty `DirectionalSwitchingResolutions` for the base level.

## See Also

### Configuring the metric
- [var switchingResolutions: [LevelOfDetailComponent.SelectionStrategy.ResolutionMetric.DirectionalSwitchingResolutions]](./switchingresolutions.md)
- [let boundingBox: BoundingBox](./boundingbox.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/levelofdetailcomponent/selectionstrategy/resolutionmetric/directionalswitchingresolutions)*