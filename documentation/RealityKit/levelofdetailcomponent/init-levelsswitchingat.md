# init(levels:switchingAt:)

**Framework**: RealityKit  
**Kind**: init

Creates a new Level of Detail component.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(levels: [LevelOfDetailComponent.DetailLevel], switchingAt strategy: LevelOfDetailComponent.SelectionStrategy)
```

## Parameters

- `levels`: Array of detail levels, where each level contains entities to show at that level.
- `strategy`: The selection strategy with threshold values.

## See Also

- [static func addByCameraDistance(to: Entity, levels: [(entities: LevelOfDetailComponent.DetailLevel, maxDistance: Float)])](levelofdetailcomponent/addbycameradistance(to:levels:).md)
  Adds Level of Detail configuration using distance-based switching to an entity .
- [static func addByScreenArea(to: Entity, levels: [(entities: LevelOfDetailComponent.DetailLevel, minArea: Float)])](levelofdetailcomponent/addbyscreenarea(to:levels:).md)
  Adds Level of Detail configuration using screen area-based switching to an entity.
- [static func addByResolutionMetric(to: Entity, levels: [(entities: LevelOfDetailComponent.DetailLevel, switchingResolutions: LevelOfDetailComponent.SelectionStrategy.ResolutionMetric.DirectionalSwitchingResolutions)], boundingBox: BoundingBox)](levelofdetailcomponent/addbyresolutionmetric(to:levels:boundingbox:).md)
  Adds Level of Detail configuration using resolution metric-based switching to an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/levelofdetailcomponent/init(levels:switchingat:))*