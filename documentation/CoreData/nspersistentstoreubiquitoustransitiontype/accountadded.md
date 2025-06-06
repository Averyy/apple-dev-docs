# NSPersistentStoreUbiquitousTransitionType.accountAdded

**Framework**: Core Data  
**Kind**: case

This value indicates that a new iCloud account is available, and the persistent store in use will or did transition to the new account.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+

## Declaration

```swift
case accountAdded
```

#### Discussion

It is only possible to discern this state when the application is running, and therefore this transition type will only be posted if the account changes while the application is running or in the background.

## See Also

- [NSPersistentStoreUbiquitousTransitionType.accountRemoved](nspersistentstoreubiquitoustransitiontype/accountremoved.md)
  This value indicates that no iCloud account is available, and the persistent store in use will or did transition to the “local” store.
- [NSPersistentStoreUbiquitousTransitionType.contentRemoved](nspersistentstoreubiquitoustransitiontype/contentremoved.md)
  This value indicates that the user has wiped the contents of the iCloud account, usually using Delete All from Documents & Data in Settings.
- [NSPersistentStoreUbiquitousTransitionType.initialImportCompleted](nspersistentstoreubiquitoustransitiontype/initialimportcompleted.md)
  This value indicates that the Core Data integration has finished building a store file that is consistent with the contents of the iCloud account, and is ready to replace the fallback store with that file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitoustransitiontype/accountadded)*