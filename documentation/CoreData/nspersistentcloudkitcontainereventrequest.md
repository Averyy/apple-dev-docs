# NSPersistentCloudKitContainerEventRequest

**Framework**: Core Data  
**Kind**: class

A request to fetch setup, import, or export events in a persistent CloudKit container.

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
class NSPersistentCloudKitContainerEventRequest
```

## Topics

### Fetching Events
- [class func fetchEvents(after: Date) -> Self](nspersistentcloudkitcontainereventrequest/fetchevents(after:)-5izg7.md)
  Creates a fetch request for events after a specified date from a persistent CloudKit container.
- [class func fetchEvents(after: NSPersistentCloudKitContainer.Event?) -> Self](nspersistentcloudkitcontainereventrequest/fetchevents(after:)-3yfp.md)
  Creates a fetch request for events that occur after a specified event from a persistent CloudKit container.
- [class func fetchEvents(matchingFetch: NSFetchRequest<any NSFetchRequestResult>) -> Self](nspersistentcloudkitcontainereventrequest/fetchevents(matchingfetch:).md)
  Creates a fetch request for events that match a specified fetch request from a persistent CloudKit container.
- [class func fetchForEvents() -> NSFetchRequest<any NSFetchRequestResult>](nspersistentcloudkitcontainereventrequest/fetchforevents.md)
  Creates a fetch request for all events in a persistent CloudKit container.
- [var resultType: NSPersistentCloudKitContainerEventResult.ResultType](nspersistentcloudkitcontainereventrequest/resulttype.md)
  The type of result that the request returns.

## Relationships

### Inherits From
- [NSPersistentStoreRequest](nspersistentstorerequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [NSPersistentCloudKitContainer.Event](nspersistentcloudkitcontainer/event.md)
  An object that represents activity in a persistent CloudKit container.
- [NSPersistentCloudKitContainer.EventType](nspersistentcloudkitcontainer/eventtype.md)
  The type of event in a persistent CloudKit container, either setup, import, or export.
- [class NSPersistentCloudKitContainerEventResult](nspersistentcloudkitcontainereventresult.md)
  The result of a request to fetch persistent CloudKit container events.
- [class let eventChangedNotification: NSNotification.Name](nspersistentcloudkitcontainer/eventchangednotification.md)
  A notification that contains details about an event in a persistent CloudKit container.
- [class let eventNotificationUserInfoKey: String](nspersistentcloudkitcontainer/eventnotificationuserinfokey.md)
  The user info dictionary key for the persistent CloudKit container event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainereventrequest)*