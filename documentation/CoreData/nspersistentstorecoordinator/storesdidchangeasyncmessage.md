# NSPersistentStoreCoordinator.StoresDidChangeAsyncMessage

**Framework**: Core Data  
**Kind**: struct

Posted when stores are added to or removed from the persistent store coordinator on a background queue.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct StoresDidChangeAsyncMessage
```

## Topics

### Instance Properties
- [var addedStores: [NSPersistentStore]](nspersistentstorecoordinator/storesdidchangeasyncmessage/addedstores.md)
  Stores that were added during this change.
- [let persistentStoreCoordinator: NSPersistentStoreCoordinator](nspersistentstorecoordinator/storesdidchangeasyncmessage/persistentstorecoordinator.md)
- [var removedStores: [NSPersistentStore]](nspersistentstorecoordinator/storesdidchangeasyncmessage/removedstores.md)
  Stores that were removed during this change.
- [var uuidChangedStores: (oldValue: NSPersistentStore, newValue: NSPersistentStore)?](nspersistentstorecoordinator/storesdidchangeasyncmessage/uuidchangedstores.md)

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](../Foundation/NotificationCenter/AsyncMessage.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/storesdidchangeasyncmessage)*