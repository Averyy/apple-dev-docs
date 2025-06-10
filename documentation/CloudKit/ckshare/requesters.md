# requesters

**Framework**: CloudKit  
**Kind**: property

A list of all uninvited users who have requested access to this share.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var requesters: [CKShare.AccessRequester] { get }
```

#### Discussion

When share access requests are allowed, uninvited users can attempt to join the share by sending an access request. Those pending requests appear in this array. Share owners or administrators can approve the requester or use [`denyRequesters(_:)`](ckshare/denyrequesters(_:).md) to respond to these access requests. Requesters are always returned with name components and either an email or phone number. Requesters can be approved by running [`CKFetchShareParticipantsOperation`](ckfetchshareparticipantsoperation.md) with the requester’s [`participantLookupInfo`](ckshare/accessrequester/participantlookupinfo.md) and adding the resulting participant to the share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/requesters)*