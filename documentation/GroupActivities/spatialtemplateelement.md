# SpatialTemplateElement

**Framework**: Group Activities  
**Kind**: protocol

An interface that defines an element in your spatial template.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
protocol SpatialTemplateElement : Hashable, Sendable
```

#### Overview

A type that adopts the [`SpatialTemplateElement`](spatialtemplateelement.md) protocol defines the location and orientation of a participant in a group activity. You don’t adopt this protocol directly in your custom types. Instead, you use types that adopt this protocol to retrieve the corresponding details.

## Topics

### Creating a seat position
- [static func seat(position: SpatialTemplateElementPosition, direction: SpatialTemplateElementDirection, role: (any SpatialTemplateRole)?) -> Self](spatialtemplateelement/seat(position:direction:role:).md)
  Creates a seat element with the specified position, direction, and role information.
### Getting the element details
- [var position: SpatialTemplateElementPosition](spatialtemplateelement/position.md)
  The location of the element in the shared coordinate space.
- [var direction: SpatialTemplateElementDirection](spatialtemplateelement/direction.md)
  The initial orientation of the element in the shared coordinate space.
- [var role: (any SpatialTemplateRole)?](spatialtemplateelement/role.md)
  An optional role you associate with this element.

## Relationships

### Inherits From
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [SpatialTemplateSeatElement](spatialtemplateseatelement.md)

## See Also

- [Building a guessing game for visionOS](building-a-guessing-game-for-visionos.md)
  Create a team-based guessing game for visionOS using Group Activities.
- [protocol SpatialTemplate](spatialtemplate.md)
  An interface you use to create custom arrangements of spatial Personas in a scene.
- [struct SpatialTemplatePreference](spatialtemplatepreference.md)
  A structure that specifies the preferred arrangement of participant spatial Personas in a shared simulation space.
- [struct SpatialTemplateSeatElement](spatialtemplateseatelement.md)
  A spatial template element that represents a seat for a participant in the activity.
- [struct SpatialTemplateElementPosition](spatialtemplateelementposition.md)
  A type that defines the position of an element in a spatial template.
- [struct SpatialTemplateElementDirection](spatialtemplateelementdirection.md)
  The initial direction a participant faces when an activity starts.
- [protocol SpatialTemplateRole](spatialtemplaterole.md)
  An interface for defining roles that you assign to the participants of a group activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/spatialtemplateelement)*