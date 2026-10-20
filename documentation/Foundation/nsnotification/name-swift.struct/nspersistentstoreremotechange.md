# NSPersistentStoreRemoteChange

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A notification that posts after another process writes to a persistent store.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
static let NSPersistentStoreRemoteChange: NSNotification.Name
```

#### Discussion

This notification’s `object` is the changed store coordinator. The framework posts the notification to a private thread. Move to a known thread before peforming any work.

The `userInfo` dictionary contains the store’s URL, the store’s unique identifier, and the transaction’s history token, which you access with the [`NSPersistentStoreURLKey`](../../../CoreData/nspersistentstoreurlkey.md), [`NSStoreUUIDKey`](../../../CoreData/nsstoreuuidkey.md), and [`NSPersistentHistoryTokenKey`](../../../CoreData/nspersistenthistorytokenkey.md) keys. It’s safe to capture the dictionary’s contents.

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
- [static let NSPersistentStoreDidImportUbiquitousContentChanges: NSNotification.Name](./nspersistentstoredidimportubiquitouscontentchanges.md)
  Posted after records are imported from the ubiquitous content store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nspersistentstoreremotechange)*