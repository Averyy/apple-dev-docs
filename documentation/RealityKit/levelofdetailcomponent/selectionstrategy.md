# LevelOfDetailComponent.SelectionStrategy

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The strategy used to select which detail level to display.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct SelectionStrategy
```

## Topics

### Creating a strategy
- [static func screenArea([Float]) -> LevelOfDetailComponent.SelectionStrategy](./selectionstrategy/screenarea%28_%29.md)
  Switch levels based on projected screen area (0.0 = invisible, 1.0 = fills screen).
- [static func cameraDistance([Float]) -> LevelOfDetailComponent.SelectionStrategy](./selectionstrategy/cameradistance%28_%29.md)
  Switch levels based on distance from the camera.
### Selecting by resolution metric
- [static func resolutionMetric(switchingResolutions: [LevelOfDetailComponent.SelectionStrategy.ResolutionMetric.DirectionalSwitchingResolutions], boundingBox: BoundingBox) -> LevelOfDetailComponent.SelectionStrategy](./selectionstrategy/resolutionmetric%28switchingresolutions,boundingbox%29.md)
  Creates a resolution metric for a level of detail component to switch with.
- [LevelOfDetailComponent.SelectionStrategy.ResolutionMetric](./selectionstrategy/resolutionmetric.md)

## See Also

### Choosing a level
- [var strategy: LevelOfDetailComponent.SelectionStrategy](./strategy.md)
- [var levelSelection: LevelOfDetailComponent.LevelSelection](./levelselection-swift.property.md)
  The level selection mode. Defaults to automatic selection based on the strategy.
- [LevelOfDetailComponent.LevelSelection](./levelselection-swift.struct.md)
  Controls whether LOD selection is automatic or manually overridden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/levelofdetailcomponent/selectionstrategy)*