# SpatialTemplateElementAxis

**Framework**: Group Activities  
**Kind**: struct

An axis to use when aligning elements in a spatial template.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct SpatialTemplateElementAxis
```

#### Overview

When configuring the elements of a spatial template, you can specify directions that orient a participant with the x- or z-axis of the shared coordinate space. These alignments rotate the participant around the y-axis to face the specified axis.

## Topics

### Type Properties
- [static let x: SpatialTemplateElementAxis](spatialtemplateelementaxis/x.md)
  The x-axis of alignment.
- [static let z: SpatialTemplateElementAxis](spatialtemplateelementaxis/z.md)
  The z-axis of alignment.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static func alignedWith(appAxis: SpatialTemplateElementAxis) -> SpatialTemplateElementDirection](spatialtemplateelementdirection/alignedwith(appaxis:).md)
  Creates a direction that orients the participant to look along the specified axis in the direction of the app’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/spatialtemplateelementaxis)*