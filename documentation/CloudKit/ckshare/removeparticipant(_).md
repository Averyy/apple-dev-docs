# removeParticipant(_:)

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Removes a participant from the share.

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
func removeParticipant(_ participant: CKShare.Participant)
```

```objc
- (void) removeParticipant:(CKShareParticipant *) participant;
```

## Discussion

To modify the list of participants, a share’s [`publicPermission`](./publicpermission.md) must be [`CKShare.ParticipantPermission.none`](./participantpermission/none.md). You can’t mix and match public and private users in the same share. You can only add certain participant types with this API. See [`CKShare.Participant`](./participant.md) for more information.

## Parameters

- `participant`: The participant to remove from the share.

## See Also

### Configuring the Share
- [var publicPermission: CKShare.ParticipantPermission](./publicpermission.md)
  The permission for anyone with access to the share’s URL.
- [func addParticipant(CKShare.Participant)](./addparticipant%28_%29.md)
  Adds a participant to the share.
- [CKShare.Participant](./participant.md)
  An object that describes a user’s participation in a share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/removeparticipant(_:))*