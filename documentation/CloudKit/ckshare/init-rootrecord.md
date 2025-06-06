# init(rootRecord:)

**Framework**: CloudKit  
**Kind**: init

Creates a new share for the specified record.

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
convenience init(rootRecord: CKRecord)
```

#### Discussion

When saving a newly created [`CKShare`](ckshare.md), you must save the share and its [`rootRecord`](ckshare/metadata/rootrecord.md) in the same [`CKModifyRecordsOperation`](ckmodifyrecordsoperation.md) batch.

## Parameters

- `rootRecord`: The record to share.

## See Also

- [init(coder: NSCoder)](ckshare/init(coder:).md)
  Creates a share from a serialized instance.
- [init(rootRecord: CKRecord, shareID: CKRecord.ID)](ckshare/init(rootrecord:shareid:).md)
  Creates a new share for the specified record and record ID.
- [init(recordZoneID: CKRecordZone.ID)](ckshare/init(recordzoneid:).md)
  Creates a new share for the specified record zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/init(rootrecord:))*