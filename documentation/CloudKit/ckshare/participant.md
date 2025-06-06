# CKShare.Participant

**Framework**: CloudKit  
**Kind**: class

An object that describes a user’s participation in a share.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class Participant
```

#### Overview

Participants are a key element of sharing in CloudKit. A participant provides information about an iCloud user and their participation in a share, including their identity, acceptance status, permissions, and role.

The acceptance status determines the participant’s visibilty of the shared records. Statuses are: `pending`, `accepted`, `removed`, and `unknown`. If the status is `pending`, use [`CKAcceptSharesOperation`](ckacceptsharesoperation.md) to accept the share. Upon acceptance, CloudKit makes the shared records available in the participant’s shared database. The records remain accessible for as long as the participant’s status is `accepted`.

You don’t create participants. Use the share’s [`participants`](ckshare/participants.md) property to access its existing participants. Use [`UICloudSharingController`](https://developer.apple.com/documentation/UIKit/UICloudSharingController) to manage the share’s participants and their permissions. Alternatively, you can generate participants using [`CKFetchShareParticipantsOperation`](ckfetchshareparticipantsoperation.md). Participants must have an active iCloud account.

Anyone with the URL of a public share can become a participant in that share. Participants of a public share assume the `publicUser` role. For private shares, the owner manages the participants. An owner is any participant with the `owner` role. A participant of a private share can’t accept the share unless the owner adds them first. Private share participants assume the `privateUser` role. CloudKit removes any pending participants if the owner changes the share’s [`publicPermission`](ckshare/publicpermission.md). CloudKit removes all participants if the new permission is `none`.

Participants with write permissions can modify or delete any record that you include in the share. However, only the owner can delete a shared hierarchy’s root record. If a participant attempts to delete the share, CloudKit removes the participant. The share remains active for all other participants.

## Topics

### Accessing the Participant’s Status
- [var acceptanceStatus: CKShare.ParticipantAcceptanceStatus](ckshare/participant/acceptancestatus-swift.property.md)
  The current state of the user’s acceptance of the share.
- [CKShare.Participant.AcceptanceStatus](ckshare/participant/acceptancestatus-swift.typealias.md)
  A type that represents the acceptance status of the participant.
- [CKShare.ParticipantAcceptanceStatus](ckshare/participantacceptancestatus.md)
  Constants that represent the status of a participant.
### Accessing the Participant’s Identity
- [var userIdentity: CKUserIdentity](ckshare/participant/useridentity.md)
  The identity of the participant.
### Managing the Participant’s Capabilites
- [var permission: CKShare.ParticipantPermission](ckshare/participant/permission-swift.property.md)
  The participant’s permission level for the share.
- [CKShare.Participant.Permission](ckshare/participant/permission-swift.typealias.md)
  A type that represents the permissions for a participant.
- [CKShare.ParticipantPermission](ckshare/participantpermission.md)
  Constants that represent the permissions to grant to a share participant.
- [var role: CKShare.ParticipantRole](ckshare/participant/role-swift.property.md)
  The participant’s role for the share.
- [CKShare.Participant.Role](ckshare/participant/role-swift.typealias.md)
  A type that represents the role for a participant.
- [CKShare.ParticipantRole](ckshare/participantrole.md)
  Constants that represent the role of a share’s participant.
### Deprecated
- [Deprecated Symbols](participant-deprecated-symbols.md)
  Review unsupported symbols and their replacements.
### Instance Properties
- [var participantID: CKShare.Participant.ID](ckshare/participant/participantid.md)
### Type Aliases
- [CKShare.Participant.ID](ckshare/participant/id.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class CKFetchShareParticipantsOperation](ckfetchshareparticipantsoperation.md)
  An operation that converts user identities into share participants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/participant)*