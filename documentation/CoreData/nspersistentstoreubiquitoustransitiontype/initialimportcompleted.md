# NSPersistentStoreUbiquitousTransitionType.initialImportCompleted

**Framework**: Core Data  
**Kind**: case  
**Role**: Case

This value indicates that the Core Data integration has finished building a store file that is consistent with the contents of the iCloud account, and is ready to replace the fallback store with that file.

**Availability**:
- iOS 7.0+ - Deprecated in 10.0
- iPadOS 7.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.9+ - Deprecated in 10.12
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Please see the release notes and Core Data documentation.

## Declaration

```swift
case initialImportCompleted
```

```c
NSPersistentStoreUbiquitousTransitionTypeInitialImportCompleted
```

## See Also

### Constants
- [NSPersistentStoreUbiquitousTransitionType.accountAdded](./accountadded.md)
  This value indicates that a new iCloud account is available, and the persistent store in use will or did transition to the new account.
- [NSPersistentStoreUbiquitousTransitionType.accountRemoved](./accountremoved.md)
  This value indicates that no iCloud account is available, and the persistent store in use will or did transition to the “local” store.
- [NSPersistentStoreUbiquitousTransitionType.contentRemoved](./contentremoved.md)
  This value indicates that the user has wiped the contents of the iCloud account, usually using Delete All from Documents & Data in Settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitoustransitiontype/initialimportcompleted)*