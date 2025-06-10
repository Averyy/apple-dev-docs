# didSaveObjectIDsNotification

**Framework**: Core Data  
**Kind**: property

A notification that posts after a context finishes saving changes to its managed objects.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst ?+
- macOS 10.12+
- tvOS 10.2+
- visionOS ?+
- watchOS 3.2+

## Declaration

```swift
static let didSaveObjectIDsNotification: Notification.Name
```

#### Discussion

This notification’s `object` is the saved context. Don’t peform any asynchronous work or block the calling thread. [`NSManagedObjectContext`](nsmanagedobjectcontext.md) posts notifications to the same thread that creates it.

The `userInfo` dictionary contains the identifiers of the inserted, updated, deleted, and invalidated managed objects. For the keys to access those objects, see [`NSManagedObjectContext.NotificationKey`](nsmanagedobjectcontext/notificationkey.md). It’s safe to capture the dictionary’s contents.

Use this notification instead of [`didSaveObjectsNotification`](nsmanagedobjectcontext/didsaveobjectsnotification.md) if you intend to process the changed managed object on a different thread. It’s safe to pass instances of [`NSManagedObjectID`](nsmanagedobjectid.md) across thread boundaries.

## See Also

- [static let didChangeObjectsNotification: Notification.Name](nsmanagedobjectcontext/didchangeobjectsnotification.md)
  A notification that posts when a context makes changes to its registered objects.
- [static let NSManagedObjectContextObjectsDidChange: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/NSManagedObjectContextObjectsDidChange.md)
  A notification that posts when there are changes to context’s registered managed objects.
- [static let didSaveObjectsNotification: Notification.Name](nsmanagedobjectcontext/didsaveobjectsnotification.md)
  A notification that posts after a context completes a save.
- [static let NSManagedObjectContextDidSave: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/NSManagedObjectContextDidSave.md)
  A notification that posts after a context finishes writing unsaved changes.
- [static let willSaveObjectsNotification: Notification.Name](nsmanagedobjectcontext/willsaveobjectsnotification.md)
  A notification that posts before a context writes pending changes to disk.
- [static let NSManagedObjectContextWillSave: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/NSManagedObjectContextWillSave.md)
  A notification that posts before a context writes unsaved changes.
- [let NSInsertedObjectsKey: String](nsinsertedobjectskey.md)
  A key for the set of objects that were inserted into the context.
- [let NSUpdatedObjectsKey: String](nsupdatedobjectskey.md)
  A key for the set of objects that were updated.
- [let NSDeletedObjectsKey: String](nsdeletedobjectskey.md)
  A key for the set of objects that were marked for deletion during the previous event.
- [let NSRefreshedObjectsKey: String](nsrefreshedobjectskey.md)
  A key for the set of objects that were refreshed but were not dirtied in the scope of this context.
- [let NSInvalidatedObjectsKey: String](nsinvalidatedobjectskey.md)
  A key for the set of objects that were invalidated.
- [let NSInvalidatedAllObjectsKey: String](nsinvalidatedallobjectskey.md)
  A key that specifies that all objects in the context have been invalidated.
- [static let didMergeChangesObjectIDsNotification: Notification.Name](nsmanagedobjectcontext/didmergechangesobjectidsnotification.md)
  A notification that posts after a context finishes merging changes from another notification.
- [NSManagedObjectContext.NotificationKey](nsmanagedobjectcontext/notificationkey.md)
  Keys to access details in user info dictionaries of managed object context notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/didsaveobjectidsnotification)*