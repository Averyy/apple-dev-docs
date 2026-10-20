# NSPersistentCloudKitContainer.Event

**Framework**: Core Data  
**Kind**: class  
**Role**: Class

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

```objc
@interface NSPersistentCloudKitContainerEvent : NSObject
```

## Topics

### Inspecting Event Properties
- [var type: NSPersistentCloudKitContainer.EventType](./event/type.md)
  The type of event, either setup, import, or export.
- [var identifier: UUID](./event/identifier.md)
  A unique identifier for the event in a container.
- [var storeIdentifier: String](./event/storeidentifier.md)
  The associated store identifier in the container for the event.
- [var succeeded: Bool](./event/succeeded.md)
  A Boolean value that indicates whether the operation the event represents is successful.
- [var startDate: Date](./event/startdate.md)
  The start date of the operation that the event represents.
- [var endDate: Date?](./event/enddate.md)
  The end date of the operation that the event represents.
- [var error: (any Error)?](./event/error.md)
  An error that indicates why an operation fails.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Monitoring Container Events
- [NSPersistentCloudKitContainer.EventType](./eventtype.md)
  The type of event in a persistent CloudKit container, either setup, import, or export.
- [class NSPersistentCloudKitContainerEventRequest](../nspersistentcloudkitcontainereventrequest.md)
  A request to fetch setup, import, or export events in a persistent CloudKit container.
- [class NSPersistentCloudKitContainerEventResult](../nspersistentcloudkitcontainereventresult.md)
  The result of a request to fetch persistent CloudKit container events.
- [class let eventChangedNotification: NSNotification.Name](./eventchangednotification.md)
  A notification that contains details about an event in a persistent CloudKit container.
- [class let eventNotificationUserInfoKey: String](./eventnotificationuserinfokey.md)
  The user info dictionary key for the persistent CloudKit container event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/event)*