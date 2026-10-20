# NSPersistentStoreUbiquitousTransitionType

**Framework**: Core Data  
**Kind**: enum  
**Role**: Enumeration

These constants are used as the value corresponding to the [`NSPersistentStoreUbiquitousTransitionTypeKey`](./nspersistentstoreubiquitoustransitiontypekey.md) in the user info dictionary of [`NSPersistentStoreCoordinatorStoresWillChangeNotification`](./nspersistentstorecoordinatorstoreswillchangenotification.md) and [`NSPersistentStoreCoordinatorStoresDidChangeNotification`](./nspersistentstorecoordinatorstoresdidchangenotification.md) notifications to identify the type of event leading to a change.

**Availability**:
- iOS 7.0+ - Deprecated in 10.0
- iPadOS 7.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.9+ - Deprecated in 10.12
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Please see the release notes and Core Data documentation.

## Declaration

```swift
enum NSPersistentStoreUbiquitousTransitionType
```

```c
enum NSPersistentStoreUbiquitousTransitionType : NSUInteger;
```

## Topics

### Constants
- [NSPersistentStoreUbiquitousTransitionType.accountAdded](./nspersistentstoreubiquitoustransitiontype/accountadded.md)
  This value indicates that a new iCloud account is available, and the persistent store in use will or did transition to the new account.
- [NSPersistentStoreUbiquitousTransitionType.accountRemoved](./nspersistentstoreubiquitoustransitiontype/accountremoved.md)
  This value indicates that no iCloud account is available, and the persistent store in use will or did transition to the “local” store.
- [NSPersistentStoreUbiquitousTransitionType.contentRemoved](./nspersistentstoreubiquitoustransitiontype/contentremoved.md)
  This value indicates that the user has wiped the contents of the iCloud account, usually using Delete All from Documents & Data in Settings.
- [NSPersistentStoreUbiquitousTransitionType.initialImportCompleted](./nspersistentstoreubiquitoustransitiontype/initialimportcompleted.md)
  This value indicates that the Core Data integration has finished building a store file that is consistent with the contents of the iCloud account, and is ready to replace the fallback store with that file.
### Initializers
- [init?(rawValue: UInt)](./nspersistentstoreubiquitoustransitiontype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitoustransitiontype)*