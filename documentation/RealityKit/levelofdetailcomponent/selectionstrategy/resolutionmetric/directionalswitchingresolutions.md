# LevelOfDetailComponent.SelectionStrategy.ResolutionMetric.DirectionalSwitchingResolutions

**Framework**: RealityKit  
**Kind**: struct

A struct containing the ideal switching resolutions for a single detail level in a `LevelOfDetailComponent` when viewed from a specific direction. Note that switching may not actually occur at these resolutions depending on device performance.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct DirectionalSwitchingResolutions
```

## Topics

### Creating switching resolutions
- [init(positiveX: Float, negativeX: Float, positiveY: Float, negativeY: Float, positiveZ: Float, negativeZ: Float)](levelofdetailcomponent/selectionstrategy/resolutionmetric/directionalswitchingresolutions/init(positivex:negativex:positivey:negativey:positivez:negativez:).md)
### Setting axis resolutions
- [var positiveX: Float](levelofdetailcomponent/selectionstrategy/resolutionmetric/directionalswitchingresolutions/positivex.md)
- [var negativeX: Float](levelofdetailcomponent/selectionstrategy/resolutionmetric/directionalswitchingresolutions/negativex.md)
- [var positiveY: Float](levelofdetailcomponent/selectionstrategy/resolutionmetric/directionalswitchingresolutions/positivey.md)
- [var negativeY: Float](levelofdetailcomponent/selectionstrategy/resolutionmetric/directionalswitchingresolutions/negativey.md)
- [var positiveZ: Float](levelofdetailcomponent/selectionstrategy/resolutionmetric/directionalswitchingresolutions/positivez.md)
- [var negativeZ: Float](levelofdetailcomponent/selectionstrategy/resolutionmetric/directionalswitchingresolutions/negativez.md)
### Initializers
- [init()](levelofdetailcomponent/selectionstrategy/resolutionmetric/directionalswitchingresolutions/init.md)
  Creates an empty `DirectionalSwitchingResolutions` for the base level.

## See Also

- [var switchingResolutions: [LevelOfDetailComponent.SelectionStrategy.ResolutionMetric.DirectionalSwitchingResolutions]](levelofdetailcomponent/selectionstrategy/resolutionmetric/switchingresolutions.md)
- [let boundingBox: BoundingBox](levelofdetailcomponent/selectionstrategy/resolutionmetric/boundingbox.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/levelofdetailcomponent/selectionstrategy/resolutionmetric/directionalswitchingresolutions)*