# recordIDForManagedObjectID:

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Returns the CloudKit record ID for the specified managed object ID.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```objc
- (CKRecordID *) recordIDForManagedObjectID:(NSManagedObjectID *) managedObjectID;
```

## Mentions

- [Reading CloudKit Records for Core Data](../reading-cloudkit-records-for-core-data.md)

#### Return Value

An instance of [`CKRecord.ID`](../../CloudKit/ckrecord/id.md) if the managed object has an underlying CloudKit record; otherwise, `nil`.

## Parameters

- `managedObjectID`: The ID of the managed object.

## See Also

### Accessing Records
- [- recordForManagedObjectID:](./recordformanagedobjectid_.md)
  Returns the CloudKit record for the specified managed object ID.
- [- recordsForManagedObjectIDs:](./recordsformanagedobjectids_.md)
  Returns a dictionary that contains the CloudKit records for the specified managed object IDs.
- [- recordIDsForManagedObjectIDs:](./recordidsformanagedobjectids_.md)
  Returns a dictionary that contains the CloudKit record IDs for the specified managed object IDs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/recordidformanagedobjectid:)*