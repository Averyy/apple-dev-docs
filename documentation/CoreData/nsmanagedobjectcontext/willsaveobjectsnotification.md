# willSaveObjectsNotification

**Framework**: Core Data  
**Kind**: property

A notification that posts before a context writes pending changes to disk.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst ?+
- macOS 10.5+
- tvOS 3.0+
- visionOS ?+
- watchOS 1.0+

## Declaration

```swift
static let willSaveObjectsNotification: Notification.Name
```

#### Discussion

This notification’s `object` is the context that’s about to save. Only use the notification to operate on the in-process save operation. For example, to insert additional managed objects. Don’t peform any asynchronous work or block the calling thread. [`NSManagedObjectContext`](nsmanagedobjectcontext.md) posts notifications to the same thread that creates it.

There is no `userInfo` dictionary.

## See Also

- [static let didChangeObjectsNotification: Notification.Name](nsmanagedobjectcontext/didchangeobjectsnotification.md)
  A notification that posts when a context makes changes to its registered objects.
- [static let NSManagedObjectContextObjectsDidChange: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/NSManagedObjectContextObjectsDidChange.md)
  A notification that posts when there are changes to context’s registered managed objects.
- [static let didSaveObjectsNotification: Notification.Name](nsmanagedobjectcontext/didsaveobjectsnotification.md)
  A notification that posts after a context completes a save.
- [static let NSManagedObjectContextDidSave: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/NSManagedObjectContextDidSave.md)
  A notification that posts after a context finishes writing unsaved changes.
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
- [static let didSaveObjectIDsNotification: Notification.Name](nsmanagedobjectcontext/didsaveobjectidsnotification.md)
  A notification that posts after a context finishes saving changes to its managed objects.
- [NSManagedObjectContext.NotificationKey](nsmanagedobjectcontext/notificationkey.md)
  Keys to access details in user info dictionaries of managed object context notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/willsaveobjectsnotification)*