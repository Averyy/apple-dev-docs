# NSPersistentCloudKitContainerEventResult

**Framework**: Core Data  
**Kind**: class

The result of a request to fetch persistent CloudKit container events.

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
class NSPersistentCloudKitContainerEventResult
```

## Topics

### Handling Event Results
- [var result: Any?](nspersistentcloudkitcontainereventresult/result.md)
  The result of the persistent CloudKit container event request, which the result type determines.
- [var resultType: NSPersistentCloudKitContainerEventResult.ResultType](nspersistentcloudkitcontainereventresult/resulttype-swift.property.md)
  The type of result that the CloudKit container event fetch request returns.
- [NSPersistentCloudKitContainerEventResult.ResultType](nspersistentcloudkitcontainereventresult/resulttype-swift.enum.md)
  The types of results from a persistent CloudKit container event fetch request.

## Relationships

### Inherits From
- [NSPersistentStoreResult](nspersistentstoreresult.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [NSPersistentCloudKitContainer.Event](nspersistentcloudkitcontainer/event.md)
  An object that represents activity in a persistent CloudKit container.
- [NSPersistentCloudKitContainer.EventType](nspersistentcloudkitcontainer/eventtype.md)
  The type of event in a persistent CloudKit container, either setup, import, or export.
- [class NSPersistentCloudKitContainerEventRequest](nspersistentcloudkitcontainereventrequest.md)
  A request to fetch setup, import, or export events in a persistent CloudKit container.
- [class let eventChangedNotification: NSNotification.Name](nspersistentcloudkitcontainer/eventchangednotification.md)
  A notification that contains details about an event in a persistent CloudKit container.
- [class let eventNotificationUserInfoKey: String](nspersistentcloudkitcontainer/eventnotificationuserinfokey.md)
  The user info dictionary key for the persistent CloudKit container event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainereventresult)*