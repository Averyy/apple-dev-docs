# participantLookupInfo

**Framework**: CloudKit  
**Kind**: property

Lookup information for the requester.

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
@NSCopying
var participantLookupInfo: CKUserIdentity.LookupInfo { get }
```

#### Discussion

Use this lookup info with [`CKFetchShareParticipantsOperation`](ckfetchshareparticipantsoperation.md) to fetch the corresponding participant. Once fetched, add the participant to the share to approve the requester.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/accessrequester/participantlookupinfo)*