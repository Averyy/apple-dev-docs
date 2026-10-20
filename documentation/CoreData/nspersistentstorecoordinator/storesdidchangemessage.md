# NSPersistentStoreCoordinator.StoresDidChangeMessage

**Framework**: Core Data  
**Kind**: struct  
**Role**: Structure

Posted when stores are added to or removed from the persistent store coordinator on the main queue.

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
struct StoresDidChangeMessage
```

## Topics

### Instance Properties
- [var addedStores: [NSPersistentStore]](./storesdidchangemessage/addedstores.md)
  Stores that were added during this change.
- [let persistentStoreCoordinator: NSPersistentStoreCoordinator](./storesdidchangemessage/persistentstorecoordinator.md)
- [var removedStores: [NSPersistentStore]](./storesdidchangemessage/removedstores.md)
  Stores that were removed during this change.
- [var uuidChangedStores: (oldValue: NSPersistentStore, newValue: NSPersistentStore)?](./storesdidchangemessage/uuidchangedstores.md)

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../../Foundation/notificationcenter/mainactormessage.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/storesdidchangemessage)*