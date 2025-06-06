# SpatialTemplateSeatElement

**Framework**: Group Activities  
**Kind**: struct

A spatial template element that represents a seat for a participant in the activity.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct SpatialTemplateSeatElement
```

#### Overview

Add [`SpatialTemplateSeatElement`](spatialtemplateseatelement.md) types to a custom [`SpatialTemplate`](spatialtemplate.md) to specify the placement and orientation of participants in a group activity. When an activity starts, the system places participants into the shared coordinate space and orients them according to the seat information you provide. If you associate roles with one or more seats, participants must acquire the associated role before they can occupy the corresponding seat.

Create seat elements directly from this type and add them to the [`elements`](spatialtemplate/elements.md) property of your custom template. Alternatively, use the inherited [`seat(position:direction:role:)`](spatialtemplateseatelement/seat(position:direction:role:).md) function to create seats, as shown in the following example, which creates two seats on either side of the app’s content along the z-axis:

```swift
struct BasicTemplate: SpatialTemplate {
    var elements: [any SpatialTemplateElement] = [
        .seat(position: .app.offsetBy(x: 0, z: 1)),
        .seat(position: .app.offsetBy(x: 0, z: -1)),
    ]
}
```

## Topics

### Getting the element details
- [let position: SpatialTemplateElementPosition](spatialtemplateseatelement/position.md)
  The location of the element in the shared coordinate space.
- [let direction: SpatialTemplateElementDirection](spatialtemplateseatelement/direction.md)
  The initial orientation of the element in the shared coordinate space.
- [let role: (any SpatialTemplateRole)?](spatialtemplateseatelement/role.md)
  An optional role you associate with this element.
### Operators
- [static func == (SpatialTemplateSeatElement, SpatialTemplateSeatElement) -> Bool](spatialtemplateseatelement/==(_:_:).md)
  Returns a Boolean value that indicates whether two values are equal.
### Initializers
- [init(position: SpatialTemplateElementPosition, direction: SpatialTemplateElementDirection, role: (any SpatialTemplateRole)?)](spatialtemplateseatelement/init(position:direction:role:).md)
  Creates a seat element with the specified position, direction, and role information.
### Instance Properties
- [var hashValue: Int](spatialtemplateseatelement/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](spatialtemplateseatelement/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](spatialtemplateseatelement/equatable-implementations.md)
- [SpatialTemplateElement Implementations](spatialtemplateseatelement/spatialtemplateelement-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SpatialTemplateElement](spatialtemplateelement.md)

## See Also

- [Building a guessing game for visionOS](building-a-guessing-game-for-visionos.md)
  Create a team-based guessing game for visionOS using Group Activities.
- [protocol SpatialTemplate](spatialtemplate.md)
  An interface you use to create custom arrangements of spatial Personas in a scene.
- [protocol SpatialTemplateElement](spatialtemplateelement.md)
  An interface that defines an element in your spatial template.
- [struct SpatialTemplateElementPosition](spatialtemplateelementposition.md)
  A type that defines the position of an element in a spatial template.
- [struct SpatialTemplateElementDirection](spatialtemplateelementdirection.md)
  The initial direction a participant faces when an activity starts.
- [protocol SpatialTemplateRole](spatialtemplaterole.md)
  An interface for defining roles that you assign to the participants of a group activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/spatialtemplateseatelement)*