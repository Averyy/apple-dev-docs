# canModifyManagedObjects(in:)

**Framework**: Core Data  
**Kind**: method

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

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the user can modify records in the persistent store’s CloudKit database; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Use this method to determine whether the user is able to write any records to the CloudKit database. To find out if the user can modify a specific object, use the [`canUpdateRecord(forManagedObjectWith:)`](nspersistentcloudkitcontainer/canupdaterecord(formanagedobjectwith:).md) and [`canDeleteRecord(forManagedObjectWith:)`](nspersistentcloudkitcontainer/candeleterecord(formanagedobjectwith:).md) methods instead.

This method always returns [`true`](https://developer.apple.com/documentation/Swift/true) for persistent stores that manage the user’s private CloudKit database.

## Parameters

- `store`: The persistent store.

## See Also

- [func canUpdateRecord(forManagedObjectWith: NSManagedObjectID) -> Bool](nspersistentcloudkitcontainer/canupdaterecord(formanagedobjectwith:).md)
  Returns a Boolean value that indicates whether the user can modify the managed object’s underlying CloudKit record.
- [func canDeleteRecord(forManagedObjectWith: NSManagedObjectID) -> Bool](nspersistentcloudkitcontainer/candeleterecord(formanagedobjectwith:).md)
  Returns a Boolean value that indicates whether the user can delete the managed object’s underlying CloudKit record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/canmodifymanagedobjects(in:))*