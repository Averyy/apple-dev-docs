# NSCoreDataCoreSpotlightDelegate.IndexDidUpdateMessage

**Framework**: Core Data  
**Kind**: struct  
**Role**: Structure

Posted when the Core Spotlight index is updated on a private queue.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS

## Declaration

```swift
struct IndexDidUpdateMessage
```

## Topics

### Instance Properties
- [let historyToken: NSPersistentHistoryToken?](./indexdidupdatemessage/historytoken.md)
  The persistent history token representing the index state.
- [let storeUUID: String](./indexdidupdatemessage/storeuuid.md)
  The UUID of the store that was indexed.

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](../../Foundation/notificationcenter/asyncmessage.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nscoredatacorespotlightdelegate/indexdidupdatemessage)*