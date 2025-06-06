# addParticipant(_:)

**Framework**: CloudKit  
**Kind**: method

Adds a participant to the share.

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
func addParticipant(_ participant: CKShare.Participant)
```

#### Discussion

If a participant with a matching [`userIdentity`](ckshare/participant/useridentity.md) already exists in the share, the system updates the existing participant’s properties and doesn’t add a new participant.

To modify the list of participants, a share’s [`publicPermission`](ckshare/publicpermission.md) must be [`CKShare.ParticipantPermission.none`](ckshare/participantpermission/none.md). You can’t mix and match public and private users in the same share. You can only add certain participant types with this API. See [`CKShare.Participant`](ckshare/participant.md) for more information.

## Parameters

- `participant`: The participant to add to the share.

## See Also

- [var publicPermission: CKShare.ParticipantPermission](ckshare/publicpermission.md)
  The permission for anyone with access to the share’s URL.
- [func removeParticipant(CKShare.Participant)](ckshare/removeparticipant(_:).md)
  Removes a participant from the share.
- [CKShare.Participant](ckshare/participant.md)
  An object that describes a user’s participation in a share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/addparticipant(_:))*