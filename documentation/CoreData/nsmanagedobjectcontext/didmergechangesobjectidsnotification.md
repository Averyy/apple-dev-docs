# didMergeChangesObjectIDsNotification

**Framework**: Core Data  
**Kind**: property

A notification that posts after a context finishes merging changes from another notification.

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
static let didMergeChangesObjectIDsNotification: Notification.Name
```

#### Discussion

This notification’s `object` is the merged context. Don’t peform any asynchronous work or block the calling thread. [`NSManagedObjectContext`](nsmanagedobjectcontext.md) posts notifications to the same thread that creates it.

The `userInfo` dictionary contains the identifiers of the inserted, updated, deleted, refreshed, and invalidated managed objects. For the keys to access those objects, see [`NSManagedObjectContext.NotificationKey`](nsmanagedobjectcontext/notificationkey.md). It’s safe to capture the dictionary’s contents.

## See Also

- [static let didChangeObjectsNotification: Notification.Name](nsmanagedobjectcontext/didchangeobjectsnotification.md)
  A notification that posts when a context makes changes to its registered objects.
- [static let NSManagedObjectContextObjectsDidChange: NSNotification.Name](../foundation/nsnotification/name/1506884-nsmanagedobjectcontextobjectsdid.md)
  A notification that posts when there are changes to context’s registered managed objects.
- [static let didSaveObjectsNotification: Notification.Name](nsmanagedobjectcontext/didsaveobjectsnotification.md)
  A notification that posts after a context completes a save.
- [static let NSManagedObjectContextDidSave: NSNotification.Name](../foundation/nsnotification/name/1506380-nsmanagedobjectcontextdidsave.md)
  A notification that posts after a context finishes writing unsaved changes.
- [static let willSaveObjectsNotification: Notification.Name](nsmanagedobjectcontext/willsaveobjectsnotification.md)
  A notification that posts before a context writes pending changes to disk.
- [static let NSManagedObjectContextWillSave: NSNotification.Name](../foundation/nsnotification/name/1506816-nsmanagedobjectcontextwillsave.md)
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
- [static let didSaveObjectIDsNotification: Notification.Name](nsmanagedobjectcontext/didsaveobjectidsnotification.md)
  A notification that posts after a context finishes saving changes to its managed objects.
- [NSManagedObjectContext.NotificationKey](nsmanagedobjectcontext/notificationkey.md)
  Keys to access details in user info dictionaries of managed object context notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/didmergechangesobjectidsnotification)*