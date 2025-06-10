# NSPersistentStoreUbiquitousTransitionTypeKey

**Framework**: Core Data  
**Kind**: var

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+

## Declaration

```swift
let NSPersistentStoreUbiquitousTransitionTypeKey: String
```

#### Description

In the [`NSPersistentStoreCoordinatorStoresWillChange`](https://developer.apple.com/documentation/Foundation/NSNotification/Name-swift.struct/NSPersistentStoreCoordinatorStoresWillChange) and [`NSPersistentStoreCoordinatorStoresDidChange`](https://developer.apple.com/documentation/Foundation/NSNotification/Name-swift.struct/NSPersistentStoreCoordinatorStoresDidChange) userInfo dictionaries, this identifies the type of event. The corresponding value is one of the [`NSPersistentStoreUbiquitousTransitionType`](nspersistentstoreubiquitoustransitiontype.md) enum values as an `NSNumber` object.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitoustransitiontypekey)*