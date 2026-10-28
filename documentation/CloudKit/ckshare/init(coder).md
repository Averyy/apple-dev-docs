# init(coder:)

**Framework**: CloudKit  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithCoder:(NSCoder *) aDecoder;
```

## Discussion

When saving a newly created [`CKShare`](../ckshare.md), you must save the share and its [`rootRecord`](./metadata/rootrecord.md) in the same [`CKModifyRecordsOperation`](../ckmodifyrecordsoperation.md) batch.

## Parameters

- `aDecoder`: The coder to use when deserializing the share.

## See Also

### Creating a Share
- [convenience init(rootRecord: CKRecord)](./init%28rootrecord%29.md)
  Creates a new share for the specified record.
- [init(rootRecord: CKRecord, shareID: CKRecord.ID)](./init%28rootrecord,shareid%29.md)
  Creates a new share for the specified record and record ID.
- [init(recordZoneID: CKRecordZone.ID)](./init%28recordzoneid%29.md)
  Creates a new share for the specified record zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/init(coder:))*