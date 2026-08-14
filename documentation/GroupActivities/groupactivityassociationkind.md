# GroupActivityAssociationKind

**Framework**: Group Activities  
**Kind**: struct

An association a user-interface element can have with a SharePlay group activity.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct GroupActivityAssociationKind
```

## Mentions

- [Adding spatial Persona support to an activity](adding-spatial-persona-support-to-an-activity.md)

#### Overview

Use values of this type in conjunction with the `SwiftUI/View/groupActivityAssociation(_:)` view modifier or [`GroupActivityAssociationInteraction`](groupactivityassociationinteraction.md) UI interaction to set the scene associated with the current SharePlay activity.

## Topics

### Type Methods
- [static func primary(String) -> GroupActivityAssociationKind](groupactivityassociationkind/primary(_:).md)
  A primary association with a SharePlay group activity that is identified by a given string value.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Configure your visionOS app for sharing with people nearby](configure-your-app-for-sharing-with-people-nearby.md)
  Create shared experiences for people wearing Vision Pro in the same room and those on FaceTime.
- [Adding spatial Persona support to an activity](adding-spatial-persona-support-to-an-activity.md)
  Update your SharePlay activities to support spatial Personas and the shared context when running in visionOS.
- [Implementing SharePlay for immersive spaces in visionOS](../visionos/implementing-shareplay-for-immersive-spaces-in-visionos.md)
  Enable collaborative spatial experiences by using SharePlay to synchronize 3D content among participants.
- [class SystemCoordinator](systemcoordinator.md)
  A type you use to coordinate your interface’s behavior when an active SharePlay session supports spatial placement of content.
- [SystemCoordinator.ParticipantState](systemcoordinator/participantstate.md)
  A structure that tells you whether a participant supports a shared simulation space for the current activity.
- [func groupActivityAssociation(GroupActivityAssociationKind?) -> some View
](../swiftui/view/groupactivityassociation(_:).md)
  Specifies how a view should be associated with the current SharePlay group activity.
- [class GroupActivityAssociationInteraction](groupactivityassociationinteraction.md)
  An interaction configures a view’s association with the current SharePlay group activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivityassociationkind)*