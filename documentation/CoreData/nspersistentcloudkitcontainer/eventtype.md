# NSPersistentCloudKitContainer.EventType

**Framework**: Core Data  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum NSPersistentCloudKitContainerEventType : NSInteger;
```

## Topics

### Event Types
- [NSPersistentCloudKitContainer.EventType.setup](./eventtype/setup.md)
  An event the persistent CloudKit container generates when setting up a store.
- [NSPersistentCloudKitContainer.EventType.import](./eventtype/import.md)
  An event the persistent CloudKit container generates when importing records into a store.
- [NSPersistentCloudKitContainer.EventType.export](./eventtype/export.md)
  An event the persistent CloudKit container generates when exporting managed objects from a store.
### Initializers
- [init?(rawValue: Int)](./eventtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Monitoring Container Events
- [NSPersistentCloudKitContainer.Event](./event.md)
  An object that represents activity in a persistent CloudKit container.
- [class NSPersistentCloudKitContainerEventRequest](../nspersistentcloudkitcontainereventrequest.md)
  A request to fetch setup, import, or export events in a persistent CloudKit container.
- [class NSPersistentCloudKitContainerEventResult](../nspersistentcloudkitcontainereventresult.md)
  The result of a request to fetch persistent CloudKit container events.
- [class let eventChangedNotification: NSNotification.Name](./eventchangednotification.md)
  A notification that contains details about an event in a persistent CloudKit container.
- [class let eventNotificationUserInfoKey: String](./eventnotificationuserinfokey.md)
  The user info dictionary key for the persistent CloudKit container event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/eventtype)*