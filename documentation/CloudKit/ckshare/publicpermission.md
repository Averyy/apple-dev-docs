# publicPermission

**Framework**: CloudKit  
**Kind**: property

The permission for anyone with access to the share’s URL.

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
var publicPermission: CKShare.ParticipantPermission { get set }
```

#### Discussion

Setting this property’s value to be more permissive than [`CKShare.ParticipantPermission.none`](ckshare/participantpermission/none.md) allows any user with the share’s URL to join. CloudKit removes all public participants when you save the share if you set the property’s value to [`CKShare.ParticipantPermission.none`](ckshare/participantpermission/none.md).

The default value is [`CKShare.ParticipantPermission.none`](ckshare/participantpermission/none.md)

## See Also

- [func addParticipant(CKShare.Participant)](ckshare/addparticipant(_:).md)
  Adds a participant to the share.
- [func removeParticipant(CKShare.Participant)](ckshare/removeparticipant(_:).md)
  Removes a participant from the share.
- [CKShare.Participant](ckshare/participant.md)
  An object that describes a user’s participation in a share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/publicpermission)*