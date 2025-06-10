# GroupActivityAssociationKind

**Framework**: Group Activities  
**Kind**: struct

An association a user-interface element can have with a SharePlay group activity.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct GroupActivityAssociationKind
```

#### Overview

Use values of this type in conjunction with the `SwiftUI/View/groupActivityAssociation(_:)` view modifier or [`GroupActivityAssociationInteraction`](groupactivityassociationinteraction.md) UI interaction to set the scene associated with the current SharePlay activity.

## Topics

### Operators
- [static func == (GroupActivityAssociationKind, GroupActivityAssociationKind) -> Bool](groupactivityassociationkind/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](groupactivityassociationkind/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](groupactivityassociationkind/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Methods
- [static func primary(String) -> GroupActivityAssociationKind](groupactivityassociationkind/primary(_:).md)
  A primary association with a SharePlay group activity that is identified by a given string value.
### Default Implementations
- [Equatable Implementations](groupactivityassociationkind/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Configure your visionOS app for sharing with people nearby](configure-your-app-for-sharing-with-people-nearby.md)
  Create shared experiences for people wearing Vision Pro in the same room and those on FaceTime.
- [Adding spatial Persona support to an activity](adding-spatial-persona-support-to-an-activity.md)
  Update your SharePlay activities to support spatial Personas and the shared context when running in visionOS.
- [class SystemCoordinator](systemcoordinator.md)
  A type you use to coordinate your interface’s behavior when an active SharePlay session supports spatial placement of content.
- [SystemCoordinator.ParticipantState](systemcoordinator/participantstate.md)
  A structure that tells you whether a participant supports a shared simulation space for the current activity.
- [nonisolated func groupActivityAssociation(_ kind: GroupActivityAssociationKind?) -> some View
](../SwiftUI/View/groupActivityAssociation(_:).md)
  Specifies how a view should be associated with the current SharePlay group activity.
- [class GroupActivityAssociationInteraction](groupactivityassociationinteraction.md)
  An interaction configures a view’s association with the current SharePlay group activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivityassociationkind)*