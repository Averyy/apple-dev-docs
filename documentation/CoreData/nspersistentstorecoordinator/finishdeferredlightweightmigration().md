# finishDeferredLightweightMigration()

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) finishDeferredLightweightMigration:(NSError **) error;
```

#### Discussion

> **Note**:  Enable deferred lightweight migrations before using this method. For more information, see [`NSPersistentStoreDeferredLightweightMigrationOptionKey`](../nspersistentstoredeferredlightweightmigrationoptionkey.md).

## See Also

### Deferring a store’s migrations
- [let NSPersistentStoreDeferredLightweightMigrationOptionKey: String](../nspersistentstoredeferredlightweightmigrationoptionkey.md)
  The key for enabling deferred lightweight migrations.
- [func finishDeferredLightweightMigrationTask() throws](./finishdeferredlightweightmigrationtask%28%29.md)
  Executes a single pending task of a deferred lightweight migration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/finishdeferredlightweightmigration())*