# NSPersistentStoreUbiquitousTransitionType.contentRemoved

**Framework**: Core Data  
**Kind**: case

This value indicates that the user has wiped the contents of the iCloud account, usually using Delete All from Documents & Data in Settings.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+

## Declaration

```swift
case contentRemoved
```

#### Discussion

The Core Data integration will transition to an empty store file as a result of this event.

## See Also

- [NSPersistentStoreUbiquitousTransitionType.accountAdded](nspersistentstoreubiquitoustransitiontype/accountadded.md)
  This value indicates that a new iCloud account is available, and the persistent store in use will or did transition to the new account.
- [NSPersistentStoreUbiquitousTransitionType.accountRemoved](nspersistentstoreubiquitoustransitiontype/accountremoved.md)
  This value indicates that no iCloud account is available, and the persistent store in use will or did transition to the “local” store.
- [NSPersistentStoreUbiquitousTransitionType.initialImportCompleted](nspersistentstoreubiquitoustransitiontype/initialimportcompleted.md)
  This value indicates that the Core Data integration has finished building a store file that is consistent with the contents of the iCloud account, and is ready to replace the fallback store with that file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitoustransitiontype/contentremoved)*