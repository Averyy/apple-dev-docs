# NSPersistentCloudKitContainer.EventType

**Framework**: Core Data  
**Kind**: enum

The type of event in a persistent CloudKit container, either setup, import, or export.

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
enum EventType
```

## Topics

### Event Types
- [NSPersistentCloudKitContainer.EventType.setup](nspersistentcloudkitcontainer/eventtype/setup.md)
  An event the persistent CloudKit container generates when setting up a store.
- [NSPersistentCloudKitContainer.EventType.import](nspersistentcloudkitcontainer/eventtype/import.md)
  An event the persistent CloudKit container generates when importing records into a store.
- [NSPersistentCloudKitContainer.EventType.export](nspersistentcloudkitcontainer/eventtype/export.md)
  An event the persistent CloudKit container generates when exporting managed objects from a store.
### Initializers
- [init?(rawValue: Int)](nspersistentcloudkitcontainer/eventtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [NSPersistentCloudKitContainer.Event](nspersistentcloudkitcontainer/event.md)
  An object that represents activity in a persistent CloudKit container.
- [class NSPersistentCloudKitContainerEventRequest](nspersistentcloudkitcontainereventrequest.md)
  A request to fetch setup, import, or export events in a persistent CloudKit container.
- [class NSPersistentCloudKitContainerEventResult](nspersistentcloudkitcontainereventresult.md)
  The result of a request to fetch persistent CloudKit container events.
- [class let eventChangedNotification: NSNotification.Name](nspersistentcloudkitcontainer/eventchangednotification.md)
  A notification that contains details about an event in a persistent CloudKit container.
- [class let eventNotificationUserInfoKey: String](nspersistentcloudkitcontainer/eventnotificationuserinfokey.md)
  The user info dictionary key for the persistent CloudKit container event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/eventtype)*