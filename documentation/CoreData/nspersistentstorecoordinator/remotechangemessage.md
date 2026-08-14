# NSPersistentStoreCoordinator.RemoteChangeMessage

**Framework**: Core Data  
**Kind**: struct

Posted when a store receives a remote change notification from another process.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct RemoteChangeMessage
```

## Topics

### Instance Properties
- [let historyToken: NSPersistentHistoryToken?](nspersistentstorecoordinator/remotechangemessage/historytoken.md)
  The persistent history token representing the state after the remote change.
- [let persistentStoreCoordinator: NSPersistentStoreCoordinator](nspersistentstorecoordinator/remotechangemessage/persistentstorecoordinator.md)
- [let storeURL: URL](nspersistentstorecoordinator/remotechangemessage/storeurl.md)
  The URL of the store that changed.
- [let storeUUID: String](nspersistentstorecoordinator/remotechangemessage/storeuuid.md)
  The UUID of the store that changed.

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](../foundation/notificationcenter/asyncmessage.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/remotechangemessage)*