# NSCoreDataCoreSpotlightDelegate.IndexDidUpdateMessage

**Framework**: Core Data  
**Kind**: struct

Posted when the Core Spotlight index is updated on a private queue.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
struct IndexDidUpdateMessage
```

## Topics

### Instance Properties
- [let historyToken: NSPersistentHistoryToken?](nscoredatacorespotlightdelegate/indexdidupdatemessage/historytoken.md)
  The persistent history token representing the index state.
- [let storeUUID: String](nscoredatacorespotlightdelegate/indexdidupdatemessage/storeuuid.md)
  The UUID of the store that was indexed.

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](../Foundation/NotificationCenter/AsyncMessage.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nscoredatacorespotlightdelegate/indexdidupdatemessage)*