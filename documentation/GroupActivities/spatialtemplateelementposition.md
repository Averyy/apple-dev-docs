# SpatialTemplateElementPosition

**Framework**: Group Activities  
**Kind**: struct

A type that defines the position of an element in a spatial template.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct SpatialTemplateElementPosition
```

#### Overview

Use the `SpatialTemplateElementPosition` type to specify the position of an element along the x- and z-axes in the shared coordinate space. You place elements relative to the app’s content, which sits at the origin of the coordinate space. Specify distances in meters. The following example positions two participants one meter away from the app’s content, and on opposite sides of it:

```swift
struct BasicTemplate: SpatialTemplate {
    var elements: [any SpatialTemplateElement] = [
        .seat(position: .app.offsetBy(x: 0, z: 1)),
        .seat(position: .app.offsetBy(x: 0, z: -1)),
    ]
}
```

## Topics

### Getting the app’s position
- [static var app: SpatialTemplateElementPosition](spatialtemplateelementposition/app.md)
  The position of the app’s content in the shared coordinate space.
### Modifying a position
- [func offsetBy(x: Double, z: Double) -> SpatialTemplateElementPosition](spatialtemplateelementposition/offsetby(x:z:).md)
  Returns a new position at the specified distance from the origin of the shared coordinate space.
### Operators
- [static func == (SpatialTemplateElementPosition, SpatialTemplateElementPosition) -> Bool](spatialtemplateelementposition/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](spatialtemplateelementposition/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](spatialtemplateelementposition/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](spatialtemplateelementposition/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Building a guessing game for visionOS](building-a-guessing-game-for-visionos.md)
  Create a team-based guessing game for visionOS using Group Activities.
- [protocol SpatialTemplate](spatialtemplate.md)
  An interface you use to create custom arrangements of spatial Personas in a scene.
- [struct SpatialTemplateSeatElement](spatialtemplateseatelement.md)
  A spatial template element that represents a seat for a participant in the activity.
- [protocol SpatialTemplateElement](spatialtemplateelement.md)
  An interface that defines an element in your spatial template.
- [struct SpatialTemplateElementDirection](spatialtemplateelementdirection.md)
  The initial direction a participant faces when an activity starts.
- [protocol SpatialTemplateRole](spatialtemplaterole.md)
  An interface for defining roles that you assign to the participants of a group activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/spatialtemplateelementposition)*