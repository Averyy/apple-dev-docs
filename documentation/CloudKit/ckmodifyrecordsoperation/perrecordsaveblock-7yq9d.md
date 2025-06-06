# perRecordSaveBlock

**Framework**: CloudKit  
**Kind**: property

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
var perRecordSaveBlock: ((CKRecord.ID, Result<CKRecord, any Error>) -> Void)? { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/perrecordsaveblock-7yq9d)*