# init(coder:)

**Framework**: CloudKit  
**Kind**: init

Creates a share from a serialized instance.

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
init(coder aDecoder: NSCoder)
```

#### Discussion

When saving a newly created [`CKShare`](ckshare.md), you must save the share and its [`rootRecord`](ckshare/metadata/rootrecord.md) in the same [`CKModifyRecordsOperation`](ckmodifyrecordsoperation.md) batch.

## Parameters

- `aDecoder`: The coder to use when deserializing the share.

## See Also

- [convenience init(rootRecord: CKRecord)](ckshare/init(rootrecord:).md)
  Creates a new share for the specified record.
- [init(rootRecord: CKRecord, shareID: CKRecord.ID)](ckshare/init(rootrecord:shareid:).md)
  Creates a new share for the specified record and record ID.
- [init(recordZoneID: CKRecordZone.ID)](ckshare/init(recordzoneid:).md)
  Creates a new share for the specified record zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/init(coder:))*