# SpatialTemplate

**Framework**: Group Activities  
**Kind**: protocol

An interface you use to create custom arrangements of spatial Personas in a scene.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
protocol SpatialTemplate : Sendable
```

## Mentions

- [Configure your visionOS app for sharing with people nearby](configure-your-app-for-sharing-with-people-nearby.md)

#### Overview

Use the [`SpatialTemplate`](spatialtemplate.md) protocol to specify an arrangement of participants for one of your app’s group activities in visionOS. A custom template can have any number of seats, with each seat occupying a precise location in the shared coordinate space. You can also assign roles to seats and use those roles to give participants a particular responsibility. For example, a game might divide participants into opposing teams using roles.

To specify the seat positions, implement the [`elements`](spatialtemplate/elements.md) property and return an array with all of the possible seats you support. Specify the location of each seat relative to the app’s content, which is at the origin of the shared coordinate space. You specify locations as the number of meters from the origin along the x- and z-axes. For example, the following code specifies two seats one meter from the app window in different directions along the z-axis:

```swift
struct BasicTemplate: SpatialTemplate {
    var elements: [any SpatialTemplateElement] = [
        .seat(position: .app.offsetBy(x: 0, z: 1)),
        .seat(position: .app.offsetBy(x: 0, z -1))
    ]
}
```

If a seat doesn’t have an assigned role, any participant can occupy it. If you add a role to a seat, the participant must specifically acquire that role to occupy the seat. For example, a game might assign a team-specific role to players when they join that team. Choose the roles that make sense for your activity and implement them using the [`SpatialTemplateRole`](spatialtemplaterole.md) protocol.

The system orients each participant’s spatial Persona to face your app’s content by default. To change the direction someone faces, include that information when you specify the seat. For example, the following template has a presenter role and up to four audience members. The inclusion of direction parameters causes the presenter to look at the audience and the audience to look at the presenter by default.

```swift
struct SimplePresentation: SpatialTemplate {
    enum Role: String, SpatialTemplateRole {
        case presenter
    }
     let configuration = SpatialTemplateConfiguration(defaultInitiatorRole: Role.presenter)
     var elements: [any SpatialTemplateElement] {
         let audienceCenterPoint = SpatialTemplateElementPosition.app.offsetBy(x: 0, z: 4)
         let presenter = SpatialTemplateSeatElement(
             position: .app.offsetBy(x: -3, z: 1),
             direction: .lookingAt(audienceCenterPoint),
             role: Role.presenter
         )
         let audience: [any SpatialTemplateElement] = [
            .seat(position: audienceCenterPoint.offsetBy(x: -0.5, z: 0), direction: .lookingAt(presenter)),
            .seat(position: audienceCenterPoint.offsetBy(x:  0.5, z: 0), direction: .lookingAt(presenter)),
            .seat(position: audienceCenterPoint.offsetBy(x: -1.0, z: 0), direction: .lookingAt(presenter)),
            .seat(position: audienceCenterPoint.offsetBy(x:  1.0, z: 0), direction: .lookingAt(presenter)),
         ]
         return [presenter] + audience
    }
}
```

## Topics

### Configuring the spatial template
- [var configuration: SpatialTemplateConfiguration](spatialtemplate/configuration.md)
  Information a spatial template uses to configure itself.
- [struct SpatialTemplateConfiguration](spatialtemplateconfiguration.md)
  A type that contains the configuration details for a spatial template.
### Placing the template seats
- [var elements: [any SpatialTemplateElement]](spatialtemplate/elements.md)
  The collection of spatial Persona seats this template contains.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Building a guessing game for visionOS](building-a-guessing-game-for-visionos.md)
  Create a team-based guessing game for visionOS using Group Activities.
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
- [protocol SpatialTemplateRole](spatialtemplaterole.md)
  An interface for defining roles that you assign to the participants of a group activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/spatialtemplate)*