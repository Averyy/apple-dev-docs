# NSManagedObjectContext.NotificationKey

**Framework**: Core Data  
**Kind**: enum

Keys to access details in user info dictionaries of managed object context notifications.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst ?+
- macOS 10.4+
- tvOS 3.0+
- visionOS ?+
- watchOS 1.0+

## Declaration

```swift
enum NotificationKey
```

## Topics

### Constants
- [NSManagedObjectContext.NotificationKey.deletedObjectIDs](nsmanagedobjectcontext/notificationkey/deletedobjectids.md)
  A key for the set of deleted object identifiers.
- [NSManagedObjectContext.NotificationKey.deletedObjects](nsmanagedobjectcontext/notificationkey/deletedobjects.md)
  A key for the context’s set of deleted objects.
- [NSManagedObjectContext.NotificationKey.insertedObjectIDs](nsmanagedobjectcontext/notificationkey/insertedobjectids.md)
  A key for the set of inserted object identifiers.
- [NSManagedObjectContext.NotificationKey.insertedObjects](nsmanagedobjectcontext/notificationkey/insertedobjects.md)
  A key for the context’s set of inserted objects.
- [NSManagedObjectContext.NotificationKey.invalidatedAllObjects](nsmanagedobjectcontext/notificationkey/invalidatedallobjects.md)
  A key for the context’s set of all invalidated objects.
- [NSManagedObjectContext.NotificationKey.invalidatedObjectIDs](nsmanagedobjectcontext/notificationkey/invalidatedobjectids.md)
  A key for the set of invalidated object identifiers.
- [NSManagedObjectContext.NotificationKey.invalidatedObjects](nsmanagedobjectcontext/notificationkey/invalidatedobjects.md)
  A key for the context’s set of invalidated objects.
- [NSManagedObjectContext.NotificationKey.queryGeneration](nsmanagedobjectcontext/notificationkey/querygeneration.md)
  A key for the token that indicates which generation of the persistent store Core Data is accessing
- [NSManagedObjectContext.NotificationKey.refreshedObjectIDs](nsmanagedobjectcontext/notificationkey/refreshedobjectids.md)
  A key for the set of refreshed object identifiers.
- [NSManagedObjectContext.NotificationKey.refreshedObjects](nsmanagedobjectcontext/notificationkey/refreshedobjects.md)
  A key for the context’s set of refreshed objects.
- [NSManagedObjectContext.NotificationKey.updatedObjectIDs](nsmanagedobjectcontext/notificationkey/updatedobjectids.md)
  A key for the set of updated object identifiers.
- [NSManagedObjectContext.NotificationKey.updatedObjects](nsmanagedobjectcontext/notificationkey/updatedobjects.md)
  A key for the context’s set of updated objects.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

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
- [static let didSaveObjectIDsNotification: Notification.Name](nsmanagedobjectcontext/didsaveobjectidsnotification.md)
  A notification that posts after a context finishes saving changes to its managed objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/notificationkey)*