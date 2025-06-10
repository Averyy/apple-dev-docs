# NSPersistentStoreDidImportUbiquitousContentChanges

**Framework**: Foundation  
**Kind**: property

Posted after records are imported from the ubiquitous content store.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
static let NSPersistentStoreDidImportUbiquitousContentChanges: NSNotification.Name
```

#### Discussion

The notification’s `object` is set to the `NSPersistentStoreCoordinator` instance which registered the store. The notification’s `userInfo` dictionary contains the same keys as the [`NSManagedObjectContextObjectsDidChange`](nsnotification/name-swift.struct/nsmanagedobjectcontextobjectsdidchange.md) notification ([`NSInsertedObjectsKey`](https://developer.apple.com/documentation/CoreData/NSInsertedObjectsKey), [`NSUpdatedObjectsKey`](https://developer.apple.com/documentation/CoreData/NSUpdatedObjectsKey)[`NSDeletedObjectsKey`](https://developer.apple.com/documentation/CoreData/NSDeletedObjectsKey)), however the values are sets of [`NSManagedObjectID`](https://developer.apple.com/documentation/CoreData/NSManagedObjectID) objects rather than sets of [`NSManagedObject`](https://developer.apple.com/documentation/CoreData/NSManagedObject) objects.

## See Also

- [static let NSManagedObjectContextDidSave: NSNotification.Name](nsnotification/name-swift.struct/nsmanagedobjectcontextdidsave.md)
  A notification that posts after a context finishes writing unsaved changes.
- [static let NSManagedObjectContextObjectsDidChange: NSNotification.Name](nsnotification/name-swift.struct/nsmanagedobjectcontextobjectsdidchange.md)
  A notification that posts when there are changes to context’s registered managed objects.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nspersistentstoredidimportubiquitouscontentchanges)*