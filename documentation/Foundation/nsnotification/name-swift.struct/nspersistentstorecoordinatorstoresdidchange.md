# NSPersistentStoreCoordinatorStoresDidChange

**Framework**: Foundation  
**Kind**: property

A notification that the coordinator posts after its registered stores change.

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
static let NSPersistentStoreCoordinatorStoresDidChange: NSNotification.Name
```

#### Discussion

This notification’s `object` is the changed store coordinator. The framework posts the notification to an internal thread. Move to a known thread before peforming any work.

The `userInfo` dictionary contains information about the added, updated, and removed persistent stores, which you access with the [`NSAddedPersistentStoresKey`](https://developer.apple.com/documentation/CoreData/NSAddedPersistentStoresKey), [`NSUUIDChangedPersistentStoresKey`](https://developer.apple.com/documentation/CoreData/NSUUIDChangedPersistentStoresKey), and [`NSRemovedPersistentStoresKey`](https://developer.apple.com/documentation/CoreData/NSRemovedPersistentStoresKey) keys. Don’t capture the dictionary’s contents.

## See Also

- [static let NSManagedObjectContextDidSave: NSNotification.Name](nsnotification/name-swift.struct/nsmanagedobjectcontextdidsave.md)
  A notification that posts after a context finishes writing unsaved changes.
- [static let NSManagedObjectContextObjectsDidChange: NSNotification.Name](nsnotification/name-swift.struct/nsmanagedobjectcontextobjectsdidchange.md)
  A notification that posts when there are changes to context’s registered managed objects.
- [static let NSManagedObjectContextWillSave: NSNotification.Name](nsnotification/name-swift.struct/nsmanagedobjectcontextwillsave.md)
  A notification that posts before a context writes unsaved changes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nspersistentstorecoordinatorstoresdidchange)*