# eventChangedNotification

**Framework**: Core Data  
**Kind**: property

A notification that contains details about an event in a persistent CloudKit container.

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
class let eventChangedNotification: NSNotification.Name
```

## See Also

- [NSPersistentCloudKitContainer.Event](nspersistentcloudkitcontainer/event.md)
  An object that represents activity in a persistent CloudKit container.
- [NSPersistentCloudKitContainer.EventType](nspersistentcloudkitcontainer/eventtype.md)
  The type of event in a persistent CloudKit container, either setup, import, or export.
- [class NSPersistentCloudKitContainerEventRequest](nspersistentcloudkitcontainereventrequest.md)
  A request to fetch setup, import, or export events in a persistent CloudKit container.
- [class NSPersistentCloudKitContainerEventResult](nspersistentcloudkitcontainereventresult.md)
  The result of a request to fetch persistent CloudKit container events.
- [class let eventNotificationUserInfoKey: String](nspersistentcloudkitcontainer/eventnotificationuserinfokey.md)
  The user info dictionary key for the persistent CloudKit container event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/eventchangednotification)*