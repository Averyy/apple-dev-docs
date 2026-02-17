# requesters

**Framework**: CloudKit  
**Kind**: property

A list of all uninvited users who have requested access to this share.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var requesters: [CKShare.AccessRequester] { get }
```

#### Discussion

When an originator or administrator allows share access requests, uninvited users can request to join the share. All pending access requests appear in this array. CloudKit returns each requester with name components and either an email or phone number.

Either share owners or administrators can respond to these access requests.

##### Responding to Access Requests

- - Fetch the participant information by running [`CKFetchShareParticipantsOperation`](ckfetchshareparticipantsoperation.md) with the requester’s [`participantLookupInfo`](ckshare/accessrequester/participantlookupinfo.md).
- Add the resulting participant to the share.
- - Use [`denyRequesters(_:)`](ckshare/denyrequesters(_:).md) to remove the requester from the requesters list.
- - Use [`blockRequesters(_:)`](ckshare/blockrequesters(_:).md) to block requesters.
- Blocking a requester prevents them from sending future access requests to the share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/requesters)*