# Notification keys

**Framework**: Core Data

The keys you use to retrieve values from a notification’s user info dictionary.

## Topics

### Constants
- [let NSAddedPersistentStoresKey: String](nsaddedpersistentstoreskey.md)
  Key for the array of stores that were added.
- [let NSRemovedPersistentStoresKey: String](nsremovedpersistentstoreskey.md)
  Key for the array of stores that were removed.
- [let NSUUIDChangedPersistentStoresKey: String](nsuuidchangedpersistentstoreskey.md)
  Key for an array containing the old and new stores.
- [let NSPersistentStoreConnectionPoolMaxSizeKey: String](nspersistentstoreconnectionpoolmaxsizekey.md)
  The maximum connection pool size to use on a store that supports concurrent request handling.
- [let NSPersistentStoreSaveConflictsErrorKey: String](nspersistentstoresaveconflictserrorkey.md)
  The key for the array of merge conflict objects (instances of [`NSMergeConflict`](nsmergeconflict.md)).
- [let NSPersistentStoreUbiquitousTransitionTypeKey: String](nspersistentstoreubiquitoustransitiontypekey.md)

## See Also

- [static let NSPersistentStoreCoordinatorStoresWillChange: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/NSPersistentStoreCoordinatorStoresWillChange.md)
  A notification that posts before a coordinator changes its registered stores.
- [static let NSPersistentStoreCoordinatorStoresDidChange: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/NSPersistentStoreCoordinatorStoresDidChange.md)
  A notification that the coordinator posts after its registered stores change.
- [static let NSPersistentStoreCoordinatorWillRemoveStore: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/NSPersistentStoreCoordinatorWillRemoveStore.md)
  A notification that posts before a coordinator removes a store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/notification-keys)*