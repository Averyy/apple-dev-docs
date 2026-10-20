# init(levels:switchingAt:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a new Level of Detail component.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(levels: [LevelOfDetailComponent.DetailLevel], switchingAt strategy: LevelOfDetailComponent.SelectionStrategy)
```

## Parameters

- `levels`: Array of detail levels, where each level contains entities to show at that level.
- `strategy`: The selection strategy with threshold values.

## See Also

### Creating a component
- [static func addByCameraDistance(to: Entity, levels: [(entities: LevelOfDetailComponent.DetailLevel, maxDistance: Float)])](./addbycameradistance%28to,levels%29.md)
  Adds Level of Detail configuration using distance-based switching to an entity .
- [static func addByScreenArea(to: Entity, levels: [(entities: LevelOfDetailComponent.DetailLevel, minArea: Float)])](./addbyscreenarea%28to,levels%29.md)
  Adds Level of Detail configuration using screen area-based switching to an entity.
- [static func addByResolutionMetric(to: Entity, levels: [(entities: LevelOfDetailComponent.DetailLevel, switchingResolutions: LevelOfDetailComponent.SelectionStrategy.ResolutionMetric.DirectionalSwitchingResolutions)], boundingBox: BoundingBox)](./addbyresolutionmetric%28to,levels,boundingbox%29.md)
  Adds Level of Detail configuration using resolution metric-based switching to an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/levelofdetailcomponent/init(levels:switchingat:))*