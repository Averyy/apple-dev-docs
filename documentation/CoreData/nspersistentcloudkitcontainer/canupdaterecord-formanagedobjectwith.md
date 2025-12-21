# canUpdateRecord(forManagedObjectWith:)

**Framework**: Core Data  
**Kind**: method

Returns a Boolean value that indicates whether the user can modify the managed object’s underlying CloudKit record.

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
func canUpdateRecord(forManagedObjectWith objectID: NSManagedObjectID) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the user can modify the CloudKit record; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

This method returns [`true`](https://developer.apple.com/documentation/Swift/true) if [`canModifyManagedObjects(in:)`](nspersistentcloudkitcontainer/canmodifymanagedobjects(in:).md) returns [`true`](https://developer.apple.com/documentation/Swift/true) and any of the following conditions are true:

- `objectID` is a temporary object identifier.
- The persistent store that contains the managed object isn’t using CloudKit.
- The persistent store manages the user’s private database.
- The persistent store manages the public database, and the user owns the underlying record or Core Data has yet to save the managed object to iCloud.
- The persistent store manages the shared database, and the user has the necessary permissions to update the managed object’s underlying record. For more information, see [`CKShare.ParticipantPermission`](https://developer.apple.com/documentation/CloudKit/CKShare/ParticipantPermission).

## Parameters

- `objectID`: The ID of the managed object.

## See Also

- [func canDeleteRecord(forManagedObjectWith: NSManagedObjectID) -> Bool](nspersistentcloudkitcontainer/candeleterecord(formanagedobjectwith:).md)
  Returns a Boolean value that indicates whether the user can delete the managed object’s underlying CloudKit record.
- [func canModifyManagedObjects(in: NSPersistentStore) -> Bool](nspersistentcloudkitcontainer/canmodifymanagedobjects(in:).md)
  Returns a Boolean value that indicates whether the user can modify the specified persistent store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/canupdaterecord(formanagedobjectwith:))*