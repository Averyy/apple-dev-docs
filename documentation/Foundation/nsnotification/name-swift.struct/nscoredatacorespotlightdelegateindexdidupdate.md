# NSCoreDataCoreSpotlightDelegateIndexDidUpdate

**Framework**: Foundation  
**Kind**: property

A notification that posts after Spotlight completes an index update.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static let NSCoreDataCoreSpotlightDelegateIndexDidUpdate: NSNotification.Name
```

#### Discussion

This notification’s `object` is the Core Spotlight delegate. The framework posts the notification to a private thread. Move to a known thread before peforming any work.

The `userInfo` dictionary contains the persistent store’s unique identifier and the most recent history token, which you access with the [`NSStoreUUIDKey`](https://developer.apple.com/documentation/CoreData/NSStoreUUIDKey) and [`NSPersistentHistoryTokenKey`](https://developer.apple.com/documentation/CoreData/NSPersistentHistoryTokenKey) keys. It’s safe to capture the dictionary’s contents.

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
- [static let NSManagedObjectContextDidMergeChangesObjectIDs: NSNotification.Name](nsnotification/name-swift.struct/nsmanagedobjectcontextdidmergechangesobjectids.md)
  A notification that posts after a context merges changes from a different notification.
- [static let NSManagedObjectContextDidSaveObjectIDs: NSNotification.Name](nsnotification/name-swift.struct/nsmanagedobjectcontextdidsaveobjectids.md)
  A notification that posts after a context finishes writing changes.
- [static let NSPersistentStoreRemoteChange: NSNotification.Name](nsnotification/name-swift.struct/nspersistentstoreremotechange.md)
  A notification that posts after another process writes to a persistent store.
- [static let NSPersistentStoreDidImportUbiquitousContentChanges: NSNotification.Name](nsnotification/name-swift.struct/nspersistentstoredidimportubiquitouscontentchanges.md)
  Posted after records are imported from the ubiquitous content store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nscoredatacorespotlightdelegateindexdidupdate)*