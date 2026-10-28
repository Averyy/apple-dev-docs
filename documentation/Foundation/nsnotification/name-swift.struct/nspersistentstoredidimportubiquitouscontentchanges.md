# NSPersistentStoreDidImportUbiquitousContentChanges

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Posted after records are imported from the ubiquitous content store.

**Availability**:
- iOS 5.0+ - Deprecated in 10.0
- iPadOS 5.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.7+ - Deprecated in 10.12
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Please see the release notes and Core Data documentation.

## Declaration

```swift
static let NSPersistentStoreDidImportUbiquitousContentChanges: NSNotification.Name
```

## Discussion

The notification’s `object` is set to the `NSPersistentStoreCoordinator` instance which registered the store. The notification’s `userInfo` dictionary contains the same keys as the [`NSManagedObjectContextObjectsDidChange`](./nsmanagedobjectcontextobjectsdidchange.md) notification ([`NSInsertedObjectsKey`](../../../CoreData/nsinsertedobjectskey.md), [`NSUpdatedObjectsKey`](../../../CoreData/nsupdatedobjectskey.md)[`NSDeletedObjectsKey`](../../../CoreData/nsdeletedobjectskey.md)), however the values are sets of [`NSManagedObjectID`](../../../CoreData/nsmanagedobjectid.md) objects rather than sets of [`NSManagedObject`](../../../CoreData/nsmanagedobject.md) objects.

## See Also

### Core Data
- [static let NSManagedObjectContextDidSave: NSNotification.Name](./nsmanagedobjectcontextdidsave.md)
  A notification that posts after a context finishes writing unsaved changes.
- [static let NSManagedObjectContextObjectsDidChange: NSNotification.Name](./nsmanagedobjectcontextobjectsdidchange.md)
  A notification that posts when there are changes to context’s registered managed objects.
- [static let NSManagedObjectContextWillSave: NSNotification.Name](./nsmanagedobjectcontextwillsave.md)
  A notification that posts before a context writes unsaved changes.
- [static let NSPersistentStoreCoordinatorStoresDidChange: NSNotification.Name](./nspersistentstorecoordinatorstoresdidchange.md)
  A notification that the coordinator posts after its registered stores change.
- [static let NSPersistentStoreCoordinatorStoresWillChange: NSNotification.Name](./nspersistentstorecoordinatorstoreswillchange.md)
  A notification that posts before a coordinator changes its registered stores.
- [static let NSPersistentStoreCoordinatorWillRemoveStore: NSNotification.Name](./nspersistentstorecoordinatorwillremovestore.md)
  A notification that posts before a coordinator removes a store.
- [static let NSCoreDataCoreSpotlightDelegateIndexDidUpdate: NSNotification.Name](./nscoredatacorespotlightdelegateindexdidupdate.md)
  A notification that posts after Spotlight completes an index update.
- [static let NSManagedObjectContextDidMergeChangesObjectIDs: NSNotification.Name](./nsmanagedobjectcontextdidmergechangesobjectids.md)
  A notification that posts after a context merges changes from a different notification.
- [static let NSManagedObjectContextDidSaveObjectIDs: NSNotification.Name](./nsmanagedobjectcontextdidsaveobjectids.md)
  A notification that posts after a context finishes writing changes.
- [static let NSPersistentStoreRemoteChange: NSNotification.Name](./nspersistentstoreremotechange.md)
  A notification that posts after another process writes to a persistent store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nspersistentstoredidimportubiquitouscontentchanges)*