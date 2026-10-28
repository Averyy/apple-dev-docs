# init(recordZoneID:)

**Framework**: CloudKit  
**Kind**: init  
**Role**: Initializer

Creates a new share for the specified record zone.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init(recordZoneID: CKRecordZone.ID)
```

```objc
- (instancetype) initWithRecordZoneID:(CKRecordZoneID *) recordZoneID;
```

## Discussion

A shared record zone must have the [`zoneWideSharing`](../ckrecordzone/capabilities-swift.struct/zonewidesharing.md) capability. Custom record zones that you create in the user’s private database have this capability by default. A record zone, and the records it contains, can take part in only a single share.

After accepting a share invite, CloudKit adds the records of the shared record zone to a new zone in the participant’s shared database. Use [`CKFetchDatabaseChangesOperation`](../ckfetchdatabasechangesoperation.md) to fetch the ID of the new record zone. Then configure [`CKFetchRecordZoneChangesOperation`](../ckfetchrecordzonechangesoperation.md) with that record zone ID and execute the operation to fetch the records.

If you use [`CKFetchShareMetadataOperation`](../ckfetchsharemetadataoperation.md) to fetch the metadata for a shared record zone, the operation ignores the [`shouldFetchRootRecord`](../ckfetchsharemetadataoperation/shouldfetchrootrecord.md) and [`rootRecordDesiredKeys`](../ckfetchsharemetadataoperation/rootrecorddesiredkeys-3xrex.md) properties because, unlike a shared record hierarchy, a record zone doesn’t have a nominated root record.

## Parameters

- `recordZoneID`: The ID of the record zone to share.

## See Also

### Creating a Share
- [init(coder: NSCoder)](./init%28coder%29.md)
  Creates a share from a serialized instance.
- [convenience init(rootRecord: CKRecord)](./init%28rootrecord%29.md)
  Creates a new share for the specified record.
- [init(rootRecord: CKRecord, shareID: CKRecord.ID)](./init%28rootrecord,shareid%29.md)
  Creates a new share for the specified record and record ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/init(recordzoneid:))*