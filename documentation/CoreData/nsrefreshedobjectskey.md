# NSRefreshedObjectsKey

**Framework**: Core Data  
**Kind**: var

A key for the set of objects that were refreshed but were not dirtied in the scope of this context.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let NSRefreshedObjectsKey: String
```

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

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsrefreshedobjectskey)*