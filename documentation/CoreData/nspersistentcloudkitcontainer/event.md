# NSPersistentCloudKitContainer.Event

**Framework**: Core Data  
**Kind**: class

An object that represents activity in a persistent CloudKit container.

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
class Event
```

## Topics

### Inspecting Event Properties
- [var type: NSPersistentCloudKitContainer.EventType](nspersistentcloudkitcontainer/event/type.md)
  The type of event, either setup, import, or export.
- [var identifier: UUID](nspersistentcloudkitcontainer/event/identifier.md)
  A unique identifier for the event in a container.
- [var storeIdentifier: String](nspersistentcloudkitcontainer/event/storeidentifier.md)
  The associated store identifier in the container for the event.
- [var succeeded: Bool](nspersistentcloudkitcontainer/event/succeeded.md)
  A Boolean value that indicates whether the operation the event represents is successful.
- [var startDate: Date](nspersistentcloudkitcontainer/event/startdate.md)
  The start date of the operation that the event represents.
- [var endDate: Date?](nspersistentcloudkitcontainer/event/enddate.md)
  The end date of the operation that the event represents.
- [var error: (any Error)?](nspersistentcloudkitcontainer/event/error.md)
  An error that indicates why an operation fails.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [NSPersistentCloudKitContainer.EventType](nspersistentcloudkitcontainer/eventtype.md)
  The type of event in a persistent CloudKit container, either setup, import, or export.
- [class NSPersistentCloudKitContainerEventRequest](nspersistentcloudkitcontainereventrequest.md)
  A request to fetch setup, import, or export events in a persistent CloudKit container.
- [class NSPersistentCloudKitContainerEventResult](nspersistentcloudkitcontainereventresult.md)
  The result of a request to fetch persistent CloudKit container events.
- [class let eventChangedNotification: NSNotification.Name](nspersistentcloudkitcontainer/eventchangednotification.md)
  A notification that contains details about an event in a persistent CloudKit container.
- [class let eventNotificationUserInfoKey: String](nspersistentcloudkitcontainer/eventnotificationuserinfokey.md)
  The user info dictionary key for the persistent CloudKit container event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/event)*