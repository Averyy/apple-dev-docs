# recordIDsForManagedObjectIDs:

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Returns a dictionary that contains the CloudKit record IDs for the specified managed object IDs.

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
- (NSDictionary<NSManagedObjectID *,CKRecordID *> *) recordIDsForManagedObjectIDs:(NSArray<NSManagedObjectID *> *) managedObjectIDs;
```

#### Return Value

A dictionary that uses `managedObjectIDs` as its keys, and the [`CKRecord.ID`](../../CloudKit/ckrecord/id.md) of each object’s underlying CloudKit record as its values. The dictionary excludes IDs that don’t have a CloudKit record.

## Parameters

- `managedObjectIDs`: An array of the managed object IDs.

## See Also

### Accessing Records
- [- recordForManagedObjectID:](./recordformanagedobjectid_.md)
  Returns the CloudKit record for the specified managed object ID.
- [- recordsForManagedObjectIDs:](./recordsformanagedobjectids_.md)
  Returns a dictionary that contains the CloudKit records for the specified managed object IDs.
- [- recordIDForManagedObjectID:](./recordidformanagedobjectid_.md)
  Returns the CloudKit record ID for the specified managed object ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/recordidsformanagedobjectids:)*