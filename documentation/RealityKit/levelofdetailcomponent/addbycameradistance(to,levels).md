# addByCameraDistance(to:levels:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Adds Level of Detail configuration using distance-based switching to an entity .

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static func addByCameraDistance(to entity: Entity, levels: [(entities: LevelOfDetailComponent.DetailLevel, maxDistance: Float)])
```

## Discussion

Each level pairs a set of entities with a maximum camera distance threshold. Entities within a level are shown or hidden together. Thresholds must be in ascending order; the last threshold is typically `.infinity`.

Each entity in the provided levels is added as a child of the entity the component will be added to. Children not included in any level are unaffected by LOD switching.

## Parameters

- `levels`: An array of levels, where each level specifies the entities to display and the maximum camera distance at which they are visible.

## See Also

### Creating a component
- [init(levels: [LevelOfDetailComponent.DetailLevel], switchingAt: LevelOfDetailComponent.SelectionStrategy)](./init%28levels,switchingat%29.md)
  Creates a new Level of Detail component.
- [static func addByScreenArea(to: Entity, levels: [(entities: LevelOfDetailComponent.DetailLevel, minArea: Float)])](./addbyscreenarea%28to,levels%29.md)
  Adds Level of Detail configuration using screen area-based switching to an entity.
- [static func addByResolutionMetric(to: Entity, levels: [(entities: LevelOfDetailComponent.DetailLevel, switchingResolutions: LevelOfDetailComponent.SelectionStrategy.ResolutionMetric.DirectionalSwitchingResolutions)], boundingBox: BoundingBox)](./addbyresolutionmetric%28to,levels,boundingbox%29.md)
  Adds Level of Detail configuration using resolution metric-based switching to an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/levelofdetailcomponent/addbycameradistance(to:levels:))*