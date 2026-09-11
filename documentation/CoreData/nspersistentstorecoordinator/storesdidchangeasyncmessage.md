# NSPersistentStoreCoordinator.StoresDidChangeAsyncMessage

**Framework**: Core Data  
**Kind**: struct

Posted when stores are added to or removed from the persistent store coordinator on a background queue.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

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
- [NotificationCenter.AsyncMessage](../foundation/notificationcenter/asyncmessage.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/storesdidchangeasyncmessage)*