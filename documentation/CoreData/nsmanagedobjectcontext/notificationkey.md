# NSManagedObjectContext.NotificationKey

**Framework**: Core Data  
**Kind**: enum  
**Role**: Enumeration

Keys to access details in user info dictionaries of managed object context notifications.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 3.0+
- macOS 10.4+
- tvOS 3.0+
- visionOS
- watchOS 1.0+

## Declaration

```swift
enum NotificationKey
```

## Topics

### Constants
- [NSManagedObjectContext.NotificationKey.deletedObjectIDs](./notificationkey/deletedobjectids.md)
  A key for the set of deleted object identifiers.
- [NSManagedObjectContext.NotificationKey.deletedObjects](./notificationkey/deletedobjects.md)
  A key for the context’s set of deleted objects.
- [NSManagedObjectContext.NotificationKey.insertedObjectIDs](./notificationkey/insertedobjectids.md)
  A key for the set of inserted object identifiers.
- [NSManagedObjectContext.NotificationKey.insertedObjects](./notificationkey/insertedobjects.md)
  A key for the context’s set of inserted objects.
- [NSManagedObjectContext.NotificationKey.invalidatedAllObjects](./notificationkey/invalidatedallobjects.md)
  A key for the context’s set of all invalidated objects.
- [NSManagedObjectContext.NotificationKey.invalidatedObjectIDs](./notificationkey/invalidatedobjectids.md)
  A key for the set of invalidated object identifiers.
- [NSManagedObjectContext.NotificationKey.invalidatedObjects](./notificationkey/invalidatedobjects.md)
  A key for the context’s set of invalidated objects.
- [NSManagedObjectContext.NotificationKey.queryGeneration](./notificationkey/querygeneration.md)
  A key for the token that indicates which generation of the persistent store Core Data is accessing
- [NSManagedObjectContext.NotificationKey.refreshedObjectIDs](./notificationkey/refreshedobjectids.md)
  A key for the set of refreshed object identifiers.
- [NSManagedObjectContext.NotificationKey.refreshedObjects](./notificationkey/refreshedobjects.md)
  A key for the context’s set of refreshed objects.
- [NSManagedObjectContext.NotificationKey.updatedObjectIDs](./notificationkey/updatedobjectids.md)
  A key for the set of updated object identifiers.
- [NSManagedObjectContext.NotificationKey.updatedObjects](./notificationkey/updatedobjects.md)
  A key for the context’s set of updated objects.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)

## See Also

### Managing notifications
- [static let didChangeObjectsNotification: Notification.Name](./didchangeobjectsnotification.md)
  A notification that posts when a context makes changes to its registered objects.
- [static let NSManagedObjectContextObjectsDidChange: NSNotification.Name](../../Foundation/nsnotification/name-swift.struct/nsmanagedobjectcontextobjectsdidchange.md)
  A notification that posts when there are changes to context’s registered managed objects.
- [static let didSaveObjectsNotification: Notification.Name](./didsaveobjectsnotification.md)
  A notification that posts after a context completes a save.
- [static let NSManagedObjectContextDidSave: NSNotification.Name](../../Foundation/nsnotification/name-swift.struct/nsmanagedobjectcontextdidsave.md)
  A notification that posts after a context finishes writing unsaved changes.
- [static let willSaveObjectsNotification: Notification.Name](./willsaveobjectsnotification.md)
  A notification that posts before a context writes pending changes to disk.
- [static let NSManagedObjectContextWillSave: NSNotification.Name](../../Foundation/nsnotification/name-swift.struct/nsmanagedobjectcontextwillsave.md)
  A notification that posts before a context writes unsaved changes.
- [let NSInsertedObjectsKey: String](../nsinsertedobjectskey.md)
  A key for the set of objects that were inserted into the context.
- [let NSUpdatedObjectsKey: String](../nsupdatedobjectskey.md)
  A key for the set of objects that were updated.
- [let NSDeletedObjectsKey: String](../nsdeletedobjectskey.md)
  A key for the set of objects that were marked for deletion during the previous event.
- [let NSRefreshedObjectsKey: String](../nsrefreshedobjectskey.md)
  A key for the set of objects that were refreshed but were not dirtied in the scope of this context.
- [let NSInvalidatedObjectsKey: String](../nsinvalidatedobjectskey.md)
  A key for the set of objects that were invalidated.
- [let NSInvalidatedAllObjectsKey: String](../nsinvalidatedallobjectskey.md)
  A key that specifies that all objects in the context have been invalidated.
- [static let didMergeChangesObjectIDsNotification: Notification.Name](./didmergechangesobjectidsnotification.md)
  A notification that posts after a context finishes merging changes from another notification.
- [static let didSaveObjectIDsNotification: Notification.Name](./didsaveobjectidsnotification.md)
  A notification that posts after a context finishes saving changes to its managed objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/notificationkey)*