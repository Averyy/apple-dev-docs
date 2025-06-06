# CKShare.ParticipantRole

**Framework**: CloudKit  
**Kind**: enum

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

## Topics

### Roles
- [CKShare.ParticipantRole.owner](ckshare/participantrole/owner.md)
  The participant is the share’s owner.
- [CKShare.ParticipantRole.privateUser](ckshare/participantrole/privateuser.md)
  The participant has the private role.
- [CKShare.ParticipantRole.publicUser](ckshare/participantrole/publicuser.md)
  The participant has the public role.
- [CKShare.ParticipantRole.unknown](ckshare/participantrole/unknown.md)
  The participant’s role is unknown.
### Initializers
- [init?(rawValue: Int)](ckshare/participantrole/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/participantrole)*