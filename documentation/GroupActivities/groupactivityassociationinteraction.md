# GroupActivityAssociationInteraction

**Framework**: Group Activities  
**Kind**: class

An interaction configures a view’s association with the current SharePlay group activity.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
@MainActor
@objc class GroupActivityAssociationInteraction
```

#### Overview

When a group of people join a SharePlay activity with their spatial Personas, the system selects a common, primary scene to arrange their spatial Personas around. This association between the group activity and a scene in your app creates a shared space for the spatial Personas to interact in; enabling participants to gesture at the associated scene and understand each other. For more information about spatial Personas and SharePlay on visionOS, see [`Adding spatial Persona support to an activity`](adding-spatial-persona-support-to-an-activity.md).

By default, the system uses your scene’s activation conditions in concert with your activity’s [`SceneAssociationBehavior`](sceneassociationbehavior.md) to select a primary scene to associate with the activity. You can specify a different scene or dynamically change the primary associated scene by adding this interaction to a view and specifying that view as the `GroupActivityAssociationKind/primary` group activity association.

> 💡 **Tip**:  When building a custom [`SpatialTemplate`](spatialtemplate.md), the primary associated scene is the [`app`](spatialtemplateelementposition/app.md) that each seat’s position is relative to.

To add the interaction to a view, use [`addInteraction(_:)`](https://developer.apple.com/documentation/UIKit/UIView/addInteraction(_:)).

```swift
// Create and store the scene association interaction
private let groupActivityAssociationInteraction = GroupActivityAssociationInteraction(
    associationKind: .primary("content-view")
)

override func viewDidLoad() {
    super.viewDidLoad()

    // Add the interaction to the view
    view.addInteraction(groupActivityAssociationInteraction)
}
```

If there are multiple scenes that are simultaneously configured with the primary group activity association, the most recently associated scene will be used. For example, if your app defines two windows and both contain views with the primary association kind, the most recently opened one will be used as the primary scene. If that second window is subsequently closed, the original window will be used again.

You can dynamically disable the group activity association of a view by setting the optional `associationKind` property to `nil`. You can later re-associate it by setting the `associationKind` to `.primary`.

```swift
func removeGroupActivityAssociation() {
   groupActivityAssociationInteraction.associationKind = nil
}
```

## Topics

### Initializers
- [init(associationKind: GroupActivityAssociationKind?)](groupactivityassociationinteraction/init(associationkind:).md)
  Creates a group activity association interaction.
### Instance Properties
- [var associationKind: GroupActivityAssociationKind?](groupactivityassociationinteraction/associationkind.md)
  An optional value that indicates the kind of group activity association, if any.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIInteraction](../UIKit/UIInteraction.md)

## See Also

- [Configure your visionOS app for sharing with people nearby](configure-your-app-for-sharing-with-people-nearby.md)
  Create shared experiences for people wearing Vision Pro in the same room and those on FaceTime.
- [Adding spatial Persona support to an activity](adding-spatial-persona-support-to-an-activity.md)
  Update your SharePlay activities to support spatial Personas and the shared context when running in visionOS.
- [class SystemCoordinator](systemcoordinator.md)
  A type you use to coordinate your interface’s behavior when an active SharePlay session supports spatial placement of content.
- [SystemCoordinator.ParticipantState](systemcoordinator/participantstate.md)
  A structure that tells you whether a participant supports a shared simulation space for the current activity.
- [func groupActivityAssociation(GroupActivityAssociationKind?) -> some View](../SwiftUI/View/groupActivityAssociation(_:).md)
  Specifies how a view should be associated with the current SharePlay group activity.
- [struct GroupActivityAssociationKind](groupactivityassociationkind.md)
  An association a user-interface element can have with a SharePlay group activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivityassociationinteraction)*