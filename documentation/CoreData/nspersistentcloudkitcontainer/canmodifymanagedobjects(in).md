# canModifyManagedObjects(in:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the user can modify the specified persistent store.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func canModifyManagedObjects(in store: NSPersistentStore) -> Bool
```

```objc
- (BOOL) canModifyManagedObjectsInStore:(NSPersistentStore *) store;
```

#### Return Value

[`true`](../../Swift/true.md) if the user can modify records in the persistent store’s CloudKit database; otherwise, [`false`](../../Swift/false.md).

#### Discussion

Use this method to determine whether the user is able to write any records to the CloudKit database. To find out if the user can modify a specific object, use the [`canUpdateRecord(forManagedObjectWith:)`](./canupdaterecord%28formanagedobjectwith%29.md) and [`canDeleteRecord(forManagedObjectWith:)`](./candeleterecord%28formanagedobjectwith%29.md) methods instead.

This method always returns [`true`](../../Swift/true.md) for persistent stores that manage the user’s private CloudKit database.

## Parameters

- `store`: The persistent store.

## See Also

### Checking Permissions
- [func canUpdateRecord(forManagedObjectWith: NSManagedObjectID) -> Bool](./canupdaterecord%28formanagedobjectwith%29.md)
  Returns a Boolean value that indicates whether the user can modify the managed object’s underlying CloudKit record.
- [func canDeleteRecord(forManagedObjectWith: NSManagedObjectID) -> Bool](./candeleterecord%28formanagedobjectwith%29.md)
  Returns a Boolean value that indicates whether the user can delete the managed object’s underlying CloudKit record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/canmodifymanagedobjects(in:))*