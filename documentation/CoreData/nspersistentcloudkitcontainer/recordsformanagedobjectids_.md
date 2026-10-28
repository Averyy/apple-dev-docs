# recordsForManagedObjectIDs:

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Returns a dictionary that contains the CloudKit records for the specified managed object IDs.

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
- (NSDictionary<NSManagedObjectID *,CKRecord *> *) recordsForManagedObjectIDs:(NSArray<NSManagedObjectID *> *) managedObjectIDs;
```

## Mentions

- [Reading CloudKit Records for Core Data](../reading-cloudkit-records-for-core-data.md)

## Return Value

A dictionary that uses `managedObjectIDs` as its keys, and each object’s underlying [`CKRecord`](../../CloudKit/ckrecord.md) as its values. The dictionary excludes IDs that don’t have a CloudKit record.

## Parameters

- `managedObjectIDs`: An array of managed object IDs.

## See Also

### Accessing Records
- [- recordForManagedObjectID:](./recordformanagedobjectid_.md)
  Returns the CloudKit record for the specified managed object ID.
- [- recordIDForManagedObjectID:](./recordidformanagedobjectid_.md)
  Returns the CloudKit record ID for the specified managed object ID.
- [- recordIDsForManagedObjectIDs:](./recordidsformanagedobjectids_.md)
  Returns a dictionary that contains the CloudKit record IDs for the specified managed object IDs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/recordsformanagedobjectids:)*