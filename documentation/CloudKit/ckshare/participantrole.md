# CKShare.ParticipantRole

**Framework**: CloudKit  
**Kind**: enum  
**Role**: Enumeration

Constants that represent the role of a share’s participant.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
enum ParticipantRole
```

```c
enum CKShareParticipantRole : NSInteger;
```

## Topics

### Roles
- [CKShare.ParticipantRole.owner](./participantrole/owner.md)
  The participant is the share’s owner.
- [CKShare.ParticipantRole.privateUser](./participantrole/privateuser.md)
  The participant has the private role.
- [CKShare.ParticipantRole.publicUser](./participantrole/publicuser.md)
  The participant has the public role.
- [CKShare.ParticipantRole.unknown](./participantrole/unknown.md)
  The participant’s role is unknown.
### Enumeration Cases
- [CKShare.ParticipantRole.administrator](./participantrole/administrator.md)
  The participant has the administrator role.
### Initializers
- [init?(rawValue: Int)](./participantrole/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing the Participant’s Capabilites
- [var permission: CKShare.ParticipantPermission](./participant/permission-swift.property.md)
  The participant’s permission level for the share.
- [CKShare.Participant.Permission](./participant/permission-swift.typealias.md)
  A type that represents the permissions for a participant.
- [CKShare.ParticipantPermission](./participantpermission.md)
  Constants that represent the permissions to grant to a share participant.
- [var role: CKShare.ParticipantRole](./participant/role-swift.property.md)
  The participant’s role for the share.
- [CKShare.Participant.Role](./participant/role-swift.typealias.md)
  A type that represents the role for a participant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/participantrole)*