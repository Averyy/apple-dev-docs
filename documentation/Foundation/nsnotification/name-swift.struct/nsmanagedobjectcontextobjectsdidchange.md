# NSManagedObjectContextObjectsDidChange

**Framework**: Foundation  
**Kind**: property

A notification that posts when there are changes to context’s registered managed objects.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let NSManagedObjectContextObjectsDidChange: NSNotification.Name
```

#### Discussion

> **Note**:  This notification posts only when there are changes to the context’s registered managed objects. It doesn’t post when a fetch adds managed objects to the context.

This notification’s `object` property is the changed managed object context. Don’t peform any asynchronous work or block the calling thread. [`NSManagedObjectContext`](https://developer.apple.com/documentation/CoreData/NSManagedObjectContext) posts notifications to the same thread that creates it.

The `userInfo` dictionary contains the inserted, updated, deleted, and invalidated managed objects. For the keys to access those objects, see [`NSManagedObjectContext.NotificationKey`](https://developer.apple.com/documentation/CoreData/NSManagedObjectContext/NotificationKey). Don’t capture the dictionary’s contents.

## See Also

- [static let NSManagedObjectContextDidSave: NSNotification.Name](nsnotification/name-swift.struct/nsmanagedobjectcontextdidsave.md)
  A notification that posts after a context finishes writing unsaved changes.
- [static let NSManagedObjectContextWillSave: NSNotification.Name](nsnotification/name-swift.struct/nsmanagedobjectcontextwillsave.md)
  A notification that posts before a context writes unsaved changes.
- [static let NSPersistentStoreCoordinatorStoresDidChange: NSNotification.Name](nsnotification/name-swift.struct/nspersistentstorecoordinatorstoresdidchange.md)
  A notification that the coordinator posts after its registered stores change.
- [static let NSPersistentStoreCoordinatorStoresWillChange: NSNotification.Name](nsnotification/name-swift.struct/nspersistentstorecoordinatorstoreswillchange.md)
  A notification that posts before a coordinator changes its registered stores.
- [static let NSPersistentStoreCoordinatorWillRemoveStore: NSNotification.Name](nsnotification/name-swift.struct/nspersistentstorecoordinatorwillremovestore.md)
  A notification that posts before a coordinator removes a store.
- [static let NSCoreDataCoreSpotlightDelegateIndexDidUpdate: NSNotification.Name](nsnotification/name-swift.struct/nscoredatacorespotlightdelegateindexdidupdate.md)
  A notification that posts after Spotlight completes an index update.
- [static let NSManagedObjectContextDidMergeChangesObjectIDs: NSNotification.Name](nsnotification/name-swift.struct/nsmanagedobjectcontextdidmergechangesobjectids.md)
  A notification that posts after a context merges changes from a different notification.
- [static let NSManagedObjectContextDidSaveObjectIDs: NSNotification.Name](nsnotification/name-swift.struct/nsmanagedobjectcontextdidsaveobjectids.md)
  A notification that posts after a context finishes writing changes.
- [static let NSPersistentStoreRemoteChange: NSNotification.Name](nsnotification/name-swift.struct/nspersistentstoreremotechange.md)
  A notification that posts after another process writes to a persistent store.
- [static let NSPersistentStoreDidImportUbiquitousContentChanges: NSNotification.Name](nsnotification/name-swift.struct/nspersistentstoredidimportubiquitouscontentchanges.md)
  Posted after records are imported from the ubiquitous content store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nsmanagedobjectcontextobjectsdidchange)*