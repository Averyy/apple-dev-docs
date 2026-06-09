# addByResolutionMetric(to:levels:boundingBox:)

**Framework**: RealityKit  
**Kind**: method

Adds Level of Detail configuration using resolution metric-based switching to an entity.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func addByResolutionMetric(to entity: Entity, levels: [(entities: LevelOfDetailComponent.DetailLevel, switchingResolutions: LevelOfDetailComponent.SelectionStrategy.ResolutionMetric.DirectionalSwitchingResolutions)], boundingBox: BoundingBox)
```

#### Discussion

Each level pairs a set of entities with a directional switching resolutions struct. Level 0 should have an empty directional switching resolutions struct. Entities within a level are shown or hidden together.

Each entity in the provided levels is added as a child of the entity the component will be added to. Children not included in any level are unaffected by LOD switching.

## Parameters

- `levels`: An array of levels, where each level specifies the entities to display and the level’s associated directional switching resolutions.
- `boundingBox`: The bounding box of the entity used when calculating the switching resolutions .

## See Also

- [init(levels: [LevelOfDetailComponent.DetailLevel], switchingAt: LevelOfDetailComponent.SelectionStrategy)](levelofdetailcomponent/init(levels:switchingat:).md)
  Creates a new Level of Detail component.
- [static func addByCameraDistance(to: Entity, levels: [(entities: LevelOfDetailComponent.DetailLevel, maxDistance: Float)])](levelofdetailcomponent/addbycameradistance(to:levels:).md)
  Adds Level of Detail configuration using distance-based switching to an entity .
- [static func addByScreenArea(to: Entity, levels: [(entities: LevelOfDetailComponent.DetailLevel, minArea: Float)])](levelofdetailcomponent/addbyscreenarea(to:levels:).md)
  Adds Level of Detail configuration using screen area-based switching to an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/levelofdetailcomponent/addbyresolutionmetric(to:levels:boundingbox:))*