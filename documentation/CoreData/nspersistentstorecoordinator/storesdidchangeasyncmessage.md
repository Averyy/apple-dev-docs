# NSPersistentStoreCoordinator.StoresDidChangeAsyncMessage

**Framework**: Core Data  
**Kind**: struct  
**Role**: Structure

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
- [var addedStores: [NSPersistentStore]](./storesdidchangeasyncmessage/addedstores.md)
  Stores that were added during this change.
- [let persistentStoreCoordinator: NSPersistentStoreCoordinator](./storesdidchangeasyncmessage/persistentstorecoordinator.md)
- [var removedStores: [NSPersistentStore]](./storesdidchangeasyncmessage/removedstores.md)
  Stores that were removed during this change.
- [var uuidChangedStores: (oldValue: NSPersistentStore, newValue: NSPersistentStore)?](./storesdidchangeasyncmessage/uuidchangedstores.md)

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](../../Foundation/notificationcenter/asyncmessage.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/storesdidchangeasyncmessage)*