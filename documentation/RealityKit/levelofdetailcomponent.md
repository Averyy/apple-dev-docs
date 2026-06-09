# LevelOfDetailComponent

**Framework**: RealityKit  
**Kind**: struct

A component that enables Level of Detail (LOD) optimization for entities with multiple detail levels.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct LevelOfDetailComponent
```

#### Overview

The component allows entities to automatically show/hide child entities based on viewing conditions, reducing rendering complexity for distant or small objects.

## Topics

### Creating a component
- [init(levels: [LevelOfDetailComponent.DetailLevel], switchingAt: LevelOfDetailComponent.SelectionStrategy)](levelofdetailcomponent/init(levels:switchingat:).md)
  Creates a new Level of Detail component.
- [static func addByCameraDistance(to: Entity, levels: [(entities: LevelOfDetailComponent.DetailLevel, maxDistance: Float)])](levelofdetailcomponent/addbycameradistance(to:levels:).md)
  Adds Level of Detail configuration using distance-based switching to an entity .
- [static func addByScreenArea(to: Entity, levels: [(entities: LevelOfDetailComponent.DetailLevel, minArea: Float)])](levelofdetailcomponent/addbyscreenarea(to:levels:).md)
  Adds Level of Detail configuration using screen area-based switching to an entity.
- [static func addByResolutionMetric(to: Entity, levels: [(entities: LevelOfDetailComponent.DetailLevel, switchingResolutions: LevelOfDetailComponent.SelectionStrategy.ResolutionMetric.DirectionalSwitchingResolutions)], boundingBox: BoundingBox)](levelofdetailcomponent/addbyresolutionmetric(to:levels:boundingbox:).md)
  Adds Level of Detail configuration using resolution metric-based switching to an entity.
### Configuring detail levels
- [var levels: [LevelOfDetailComponent.DetailLevel]](levelofdetailcomponent/levels.md)
- [LevelOfDetailComponent.DetailLevel](levelofdetailcomponent/detaillevel.md)
  An array of entities representing a single detail level. Entities within a level are shown or hidden together based on LOD selection.
### Choosing a level
- [var strategy: LevelOfDetailComponent.SelectionStrategy](levelofdetailcomponent/strategy.md)
- [LevelOfDetailComponent.SelectionStrategy](levelofdetailcomponent/selectionstrategy.md)
  The strategy used to select which detail level to display.
- [var levelSelection: LevelOfDetailComponent.LevelSelection](levelofdetailcomponent/levelselection-swift.property.md)
  The level selection mode. Defaults to automatic selection based on the strategy.
- [LevelOfDetailComponent.LevelSelection](levelofdetailcomponent/levelselection-swift.struct.md)
  Controls whether LOD selection is automatic or manually overridden.

## Relationships

### Conforms To
- [Component](component.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/levelofdetailcomponent)*