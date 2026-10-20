# role

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The participant’s role for the share.

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
var role: CKShare.ParticipantRole { get set }
```

```objc
@property (assign) CKShareParticipantRole role;
```

## See Also

### Managing the Participant’s Capabilites
- [var permission: CKShare.ParticipantPermission](./permission-swift.property.md)
  The participant’s permission level for the share.
- [CKShare.Participant.Permission](./permission-swift.typealias.md)
  A type that represents the permissions for a participant.
- [CKShare.ParticipantPermission](../participantpermission.md)
  Constants that represent the permissions to grant to a share participant.
- [CKShare.Participant.Role](./role-swift.typealias.md)
  A type that represents the role for a participant.
- [CKShare.ParticipantRole](../participantrole.md)
  Constants that represent the role of a share’s participant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/participant/role-swift.property)*