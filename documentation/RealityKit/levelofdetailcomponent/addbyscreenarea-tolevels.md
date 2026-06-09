# addByScreenArea(to:levels:)

**Framework**: RealityKit  
**Kind**: method

Adds Level of Detail configuration using screen area-based switching to an entity.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func addByScreenArea(to entity: Entity, levels: [(entities: LevelOfDetailComponent.DetailLevel, minArea: Float)])
```

#### Discussion

Each level pairs a set of entities with a minimum screen area threshold. Entities within a level are shown or hidden together. Thresholds must be in descending order and in the range [0.0, 1.0].

Each entity in the provided levels is added as a child of the entity the component will be added to. Children not included in any level are unaffected by LOD switching.

## Parameters

- `levels`: An array of levels, where each level specifies the entities to display and the minimum projected screen area (0.0-1.0) at which they are visible.

## See Also

- [init(levels: [LevelOfDetailComponent.DetailLevel], switchingAt: LevelOfDetailComponent.SelectionStrategy)](levelofdetailcomponent/init(levels:switchingat:).md)
  Creates a new Level of Detail component.
- [static func addByCameraDistance(to: Entity, levels: [(entities: LevelOfDetailComponent.DetailLevel, maxDistance: Float)])](levelofdetailcomponent/addbycameradistance(to:levels:).md)
  Adds Level of Detail configuration using distance-based switching to an entity .
- [static func addByResolutionMetric(to: Entity, levels: [(entities: LevelOfDetailComponent.DetailLevel, switchingResolutions: LevelOfDetailComponent.SelectionStrategy.ResolutionMetric.DirectionalSwitchingResolutions)], boundingBox: BoundingBox)](levelofdetailcomponent/addbyresolutionmetric(to:levels:boundingbox:).md)
  Adds Level of Detail configuration using resolution metric-based switching to an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/levelofdetailcomponent/addbyscreenarea(to:levels:))*