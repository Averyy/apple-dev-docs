# permission

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The participant’s permission level for the share.

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
var permission: CKShare.ParticipantPermission { get set }
```

```objc
@property (assign) CKShareParticipantPermission permission;
```

## Discussion

This property controls the permissions that the participant has for the share. For a list of possible values, see [`CKShare.ParticipantPermission`](../participantpermission.md).

## See Also

### Managing the Participant’s Capabilites
- [CKShare.Participant.Permission](./permission-swift.typealias.md)
  A type that represents the permissions for a participant.
- [CKShare.ParticipantPermission](../participantpermission.md)
  Constants that represent the permissions to grant to a share participant.
- [var role: CKShare.ParticipantRole](./role-swift.property.md)
  The participant’s role for the share.
- [CKShare.Participant.Role](./role-swift.typealias.md)
  A type that represents the role for a participant.
- [CKShare.ParticipantRole](../participantrole.md)
  Constants that represent the role of a share’s participant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/participant/permission-swift.property)*