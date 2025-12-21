# shareParticipants(for:)

**Framework**: CloudKit  
**Kind**: method

Fetches share participants matching the provided lookup infos.

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
func shareParticipants(for lookupInfos: [CKUserIdentity.LookupInfo]) async throws -> [CKUserIdentity.LookupInfo : Result<CKShare.Participant, any Error>]
```

#### Discussion

[`CKFetchShareParticipantsOperation`](ckfetchshareparticipantsoperation.md) is the more configurable, [`CKOperation`](ckoperation.md)-based alternative to this function


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/shareparticipants(for:))*