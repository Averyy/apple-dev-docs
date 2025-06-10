# participantLookupInfo

**Framework**: CloudKit  
**Kind**: property

Convenience method to get the requester’s lookup info. This lookup info can be used in [`CKFetchShareParticipantsOperation`](ckfetchshareparticipantsoperation.md) to approve the requester by fetching the corresponding participant and adding the participant to the share.

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
@NSCopying
var participantLookupInfo: CKUserIdentity.LookupInfo { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/accessrequester/participantlookupinfo)*