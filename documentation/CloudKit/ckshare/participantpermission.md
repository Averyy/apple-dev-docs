# CKShare.ParticipantPermission

**Framework**: CloudKit  
**Kind**: enum  
**Role**: Enumeration

Constants that represent the permissions to grant to a share participant.

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
enum ParticipantPermission
```

```c
enum CKShareParticipantPermission : NSInteger;
```

## Topics

### Permissions
- [CKShare.ParticipantPermission.none](./participantpermission/none.md)
  The participant doesn’t have any permissions for the share.
- [CKShare.ParticipantPermission.readOnly](./participantpermission/readonly.md)
  The participant has read-only permissions for the share.
- [CKShare.ParticipantPermission.readWrite](./participantpermission/readwrite.md)
  The participant has read-and-write permissions for the share.
- [CKShare.ParticipantPermission.unknown](./participantpermission/unknown.md)
  The participant’s permissions are unknown.
### Initializers
- [init?(rawValue: Int)](./participantpermission/init%28rawvalue%29.md)

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
- [var role: CKShare.ParticipantRole](./participant/role-swift.property.md)
  The participant’s role for the share.
- [CKShare.Participant.Role](./participant/role-swift.typealias.md)
  A type that represents the role for a participant.
- [CKShare.ParticipantRole](./participantrole.md)
  Constants that represent the role of a share’s participant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/participantpermission)*