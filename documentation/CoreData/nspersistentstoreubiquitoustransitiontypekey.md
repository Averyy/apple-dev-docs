# NSPersistentStoreUbiquitousTransitionTypeKey

**Framework**: Core Data  
**Kind**: var  
**Role**: Global Variable

**Availability**:
- iOS 7.0+ - Deprecated in 10.0
- iPadOS 7.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.9+ - Deprecated in 10.12
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Please see the release notes and Core Data documentation.

## Declaration

```swift
let NSPersistentStoreUbiquitousTransitionTypeKey: String
```

```c
extern NSString * const NSPersistentStoreUbiquitousTransitionTypeKey;
```

## Description

In the [`NSPersistentStoreCoordinatorStoresWillChange`](../Foundation/nsnotification/name-swift.struct/nspersistentstorecoordinatorstoreswillchange.md) and [`NSPersistentStoreCoordinatorStoresDidChange`](../Foundation/nsnotification/name-swift.struct/nspersistentstorecoordinatorstoresdidchange.md) userInfo dictionaries, this identifies the type of event. The corresponding value is one of the [`NSPersistentStoreUbiquitousTransitionType`](./nspersistentstoreubiquitoustransitiontype.md) enum values as an `NSNumber` object.

## See Also

### Constants
- [let NSAddedPersistentStoresKey: String](./nsaddedpersistentstoreskey.md)
  Key for the array of stores that were added.
- [let NSRemovedPersistentStoresKey: String](./nsremovedpersistentstoreskey.md)
  Key for the array of stores that were removed.
- [let NSUUIDChangedPersistentStoresKey: String](./nsuuidchangedpersistentstoreskey.md)
  Key for an array containing the old and new stores.
- [let NSPersistentStoreConnectionPoolMaxSizeKey: String](./nspersistentstoreconnectionpoolmaxsizekey.md)
  The maximum connection pool size to use on a store that supports concurrent request handling.
- [let NSPersistentStoreSaveConflictsErrorKey: String](./nspersistentstoresaveconflictserrorkey.md)
  The key for the array of merge conflict objects (instances of [`NSMergeConflict`](./nsmergeconflict.md)).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitoustransitiontypekey)*