# shareParticipants(for:)

**Framework**: CloudKit  
**Kind**: method

Fetches share participants matching the provided lookup infos.

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
func shareParticipants(for lookupInfos: [CKUserIdentity.LookupInfo]) async throws -> [CKUserIdentity.LookupInfo : Result<CKShare.Participant, any Error>]
```

#### Discussion

[`CKFetchShareParticipantsOperation`](ckfetchshareparticipantsoperation.md) is the more configurable, [`CKOperation`](ckoperation.md)-based alternative to this function


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/shareparticipants(for:))*