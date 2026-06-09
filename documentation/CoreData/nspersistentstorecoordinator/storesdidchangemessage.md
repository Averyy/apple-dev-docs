# NSPersistentStoreCoordinator.StoresDidChangeMessage

**Framework**: Core Data  
**Kind**: struct

Posted when stores are added to or removed from the persistent store coordinator on the main queue.

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
struct StoresDidChangeMessage
```

## Topics

### Instance Properties
- [var addedStores: [NSPersistentStore]](nspersistentstorecoordinator/storesdidchangemessage/addedstores.md)
  Stores that were added during this change.
- [let persistentStoreCoordinator: NSPersistentStoreCoordinator](nspersistentstorecoordinator/storesdidchangemessage/persistentstorecoordinator.md)
- [var removedStores: [NSPersistentStore]](nspersistentstorecoordinator/storesdidchangemessage/removedstores.md)
  Stores that were removed during this change.
- [var uuidChangedStores: (oldValue: NSPersistentStore, newValue: NSPersistentStore)?](nspersistentstorecoordinator/storesdidchangemessage/uuidchangedstores.md)

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../Foundation/NotificationCenter/MainActorMessage.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/storesdidchangemessage)*