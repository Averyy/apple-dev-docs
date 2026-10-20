# NSPersistentStoreCoordinator.RemoteChangeMessage

**Framework**: Core Data  
**Kind**: struct  
**Role**: Structure

Posted when a store receives a remote change notification from another process.

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
struct RemoteChangeMessage
```

## Topics

### Instance Properties
- [let historyToken: NSPersistentHistoryToken?](./remotechangemessage/historytoken.md)
  The persistent history token representing the state after the remote change.
- [let persistentStoreCoordinator: NSPersistentStoreCoordinator](./remotechangemessage/persistentstorecoordinator.md)
- [let storeURL: URL](./remotechangemessage/storeurl.md)
  The URL of the store that changed.
- [let storeUUID: String](./remotechangemessage/storeuuid.md)
  The UUID of the store that changed.

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](../../Foundation/notificationcenter/asyncmessage.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/remotechangemessage)*