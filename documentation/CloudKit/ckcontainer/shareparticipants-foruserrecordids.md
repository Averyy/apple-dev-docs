# shareParticipants(forUserRecordIDs:)

**Framework**: CloudKit  
**Kind**: method

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
func shareParticipants(forUserRecordIDs userRecordIDs: [CKRecord.ID]) async throws -> [CKRecord.ID : Result<CKShare.Participant, any Error>]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/shareparticipants(foruserrecordids:))*