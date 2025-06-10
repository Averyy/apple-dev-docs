# SpatialTemplateRole

**Framework**: Group Activities  
**Kind**: protocol

An interface for defining roles that you assign to the participants of a group activity.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
protocol SpatialTemplateRole : Hashable, Sendable
```

#### Overview

Adopt the [`SpatialTemplateRole`](spatialtemplaterole.md) interface in a custom `enum` and use it with your custom spatial template. Roles are an optional way for you to assign a purpose to participants with a spatial Persona. For example, a spatial template for a game might define roles for the opposing teams. When a participant joins an activity, assign one of your custom roles to place them in a specific seat of your template. Seats in the template are available only to participants with spatial Personas.

The following example shows a spatial template for a table tennis game with two teams. The first four seats are for the players of the team, and the last seat is for a spectator. When participants request a role for the red or blue team, the template assigns them to the first available seat in the array with that role.

```swift
struct SimpleTableTennis: SpatialTemplate {
    enum Role: String, SpatialTemplateRole {
        case blueTeam
        case redTeam
    }

    var elements: [any SpatialTemplateElement] = [
        .seat(position: .app.offsetBy(x: -1, z: -3), role: Role.blueTeam),
        .seat(position: .app.offsetBy(x: -1, z:  3), role: Role.redTeam),

        .seat(position: .app.offsetBy(x:  1, z: -3), role: Role.blueTeam),
        .seat(position: .app.offsetBy(x:  1, z:  3), role: Role.redTeam),

        .seat(position: .app.offsetBy(x: -2, z:  0)),
    ]
}
```

## Topics

### Getting the role identifier
- [var roleIdentifier: String](spatialtemplaterole/roleidentifier.md)
  The unique identifier string for the role.

## Relationships

### Inherits From
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Building a guessing game for visionOS](building-a-guessing-game-for-visionos.md)
  Create a team-based guessing game for visionOS using Group Activities.
- [protocol SpatialTemplate](spatialtemplate.md)
  An interface you use to create custom arrangements of spatial Personas in a scene.
- [struct SpatialTemplatePreference](spatialtemplatepreference.md)
  A structure that specifies the preferred arrangement of participant spatial Personas in a shared simulation space.
- [struct SpatialTemplateSeatElement](spatialtemplateseatelement.md)
  A spatial template element that represents a seat for a participant in the activity.
- [protocol SpatialTemplateElement](spatialtemplateelement.md)
  An interface that defines an element in your spatial template.
- [struct SpatialTemplateElementPosition](spatialtemplateelementposition.md)
  A type that defines the position of an element in a spatial template.
- [struct SpatialTemplateElementDirection](spatialtemplateelementdirection.md)
  The initial direction a participant faces when an activity starts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/spatialtemplaterole)*