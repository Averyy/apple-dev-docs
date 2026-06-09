# LevelOfDetailComponent.SelectionStrategy

**Framework**: RealityKit  
**Kind**: struct

The strategy used to select which detail level to display.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct SelectionStrategy
```

## Topics

### Creating a strategy
- [static func screenArea([Float]) -> LevelOfDetailComponent.SelectionStrategy](levelofdetailcomponent/selectionstrategy/screenarea(_:).md)
  Switch levels based on projected screen area (0.0 = invisible, 1.0 = fills screen).
- [static func cameraDistance([Float]) -> LevelOfDetailComponent.SelectionStrategy](levelofdetailcomponent/selectionstrategy/cameradistance(_:).md)
  Switch levels based on distance from the camera.
### Selecting by resolution metric
- [static func resolutionMetric(switchingResolutions: [LevelOfDetailComponent.SelectionStrategy.ResolutionMetric.DirectionalSwitchingResolutions], boundingBox: BoundingBox) -> LevelOfDetailComponent.SelectionStrategy](levelofdetailcomponent/selectionstrategy/resolutionmetric(switchingresolutions:boundingbox:).md)
  Creates a resolution metric for a level of detail component to switch with.
- [LevelOfDetailComponent.SelectionStrategy.ResolutionMetric](levelofdetailcomponent/selectionstrategy/resolutionmetric.md)

## See Also

- [var strategy: LevelOfDetailComponent.SelectionStrategy](levelofdetailcomponent/strategy.md)
- [var levelSelection: LevelOfDetailComponent.LevelSelection](levelofdetailcomponent/levelselection-swift.property.md)
  The level selection mode. Defaults to automatic selection based on the strategy.
- [LevelOfDetailComponent.LevelSelection](levelofdetailcomponent/levelselection-swift.struct.md)
  Controls whether LOD selection is automatic or manually overridden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/levelofdetailcomponent/selectionstrategy)*