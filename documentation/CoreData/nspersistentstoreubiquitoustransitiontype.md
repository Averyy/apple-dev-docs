# NSPersistentStoreUbiquitousTransitionType

**Framework**: Core Data  
**Kind**: enum

These constants are used as the value corresponding to the [`NSPersistentStoreUbiquitousTransitionTypeKey`](nspersistentstoreubiquitoustransitiontypekey.md) in the user info dictionary of [`NSPersistentStoreCoordinatorStoresWillChangeNotification`](nspersistentstorecoordinatorstoreswillchangenotification.md) and [`NSPersistentStoreCoordinatorStoresDidChangeNotification`](nspersistentstorecoordinatorstoresdidchangenotification.md) notifications to identify the type of event leading to a change.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+

## Declaration

```swift
enum NSPersistentStoreUbiquitousTransitionType
```

## Topics

### Constants
- [NSPersistentStoreUbiquitousTransitionType.accountAdded](nspersistentstoreubiquitoustransitiontype/accountadded.md)
  This value indicates that a new iCloud account is available, and the persistent store in use will or did transition to the new account.
- [NSPersistentStoreUbiquitousTransitionType.accountRemoved](nspersistentstoreubiquitoustransitiontype/accountremoved.md)
  This value indicates that no iCloud account is available, and the persistent store in use will or did transition to the “local” store.
- [NSPersistentStoreUbiquitousTransitionType.contentRemoved](nspersistentstoreubiquitoustransitiontype/contentremoved.md)
  This value indicates that the user has wiped the contents of the iCloud account, usually using Delete All from Documents & Data in Settings.
- [NSPersistentStoreUbiquitousTransitionType.initialImportCompleted](nspersistentstoreubiquitoustransitiontype/initialimportcompleted.md)
  This value indicates that the Core Data integration has finished building a store file that is consistent with the contents of the iCloud account, and is ready to replace the fallback store with that file.
### Initializers
- [init?(rawValue: UInt)](nspersistentstoreubiquitoustransitiontype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitoustransitiontype)*