# CKShare.ParticipantPermission

**Framework**: CloudKit  
**Kind**: enum

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

## Topics

### Permissions
- [CKShare.ParticipantPermission.none](ckshare/participantpermission/none.md)
  The participant doesn’t have any permissions for the share.
- [CKShare.ParticipantPermission.readOnly](ckshare/participantpermission/readonly.md)
  The participant has read-only permissions for the share.
- [CKShare.ParticipantPermission.readWrite](ckshare/participantpermission/readwrite.md)
  The participant has read-and-write permissions for the share.
- [CKShare.ParticipantPermission.unknown](ckshare/participantpermission/unknown.md)
  The participant’s permissions are unknown.
### Initializers
- [init?(rawValue: Int)](ckshare/participantpermission/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var permission: CKShare.ParticipantPermission](ckshare/participant/permission-swift.property.md)
  The participant’s permission level for the share.
- [CKShare.Participant.Permission](ckshare/participant/permission-swift.typealias.md)
  A type that represents the permissions for a participant.
- [var role: CKShare.ParticipantRole](ckshare/participant/role-swift.property.md)
  The participant’s role for the share.
- [CKShare.Participant.Role](ckshare/participant/role-swift.typealias.md)
  A type that represents the role for a participant.
- [CKShare.ParticipantRole](ckshare/participantrole.md)
  Constants that represent the role of a share’s participant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/participantpermission)*