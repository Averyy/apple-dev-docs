# finishDeferredLightweightMigration()

**Framework**: Core Data  
**Kind**: method

Executes all remaining tasks of a deferred lightweight migration.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func finishDeferredLightweightMigration() throws
```

#### Discussion

> **Note**:  Enable deferred lightweight migrations before using this method. For more information, see [`NSPersistentStoreDeferredLightweightMigrationOptionKey`](nspersistentstoredeferredlightweightmigrationoptionkey.md).

 Enable deferred lightweight migrations before using this method. For more information, see [`NSPersistentStoreDeferredLightweightMigrationOptionKey`](nspersistentstoredeferredlightweightmigrationoptionkey.md).

## See Also

- [let NSPersistentStoreDeferredLightweightMigrationOptionKey: String](nspersistentstoredeferredlightweightmigrationoptionkey.md)
  The key for enabling deferred lightweight migrations.
- [func finishDeferredLightweightMigrationTask() throws](nspersistentstorecoordinator/finishdeferredlightweightmigrationtask.md)
  Executes a single pending task of a deferred lightweight migration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/finishdeferredlightweightmigration())*