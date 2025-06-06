# fetchEvents(after:)

**Framework**: Core Data  
**Kind**: method

Creates a fetch request for events after a specified date from a persistent CloudKit container.

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
class func fetchEvents(after date: Date) -> Self
```

#### Return Value

A request object that fetches persistent CloudKit container events by executing in a managed object context.

## Parameters

- `date`: The earliest date to return events for.

## See Also

- [class func fetchEvents(after: NSPersistentCloudKitContainer.Event?) -> Self](nspersistentcloudkitcontainereventrequest/fetchevents(after:)-3yfp.md)
  Creates a fetch request for events that occur after a specified event from a persistent CloudKit container.
- [class func fetchEvents(matchingFetch: NSFetchRequest<any NSFetchRequestResult>) -> Self](nspersistentcloudkitcontainereventrequest/fetchevents(matchingfetch:).md)
  Creates a fetch request for events that match a specified fetch request from a persistent CloudKit container.
- [class func fetchForEvents() -> NSFetchRequest<any NSFetchRequestResult>](nspersistentcloudkitcontainereventrequest/fetchforevents.md)
  Creates a fetch request for all events in a persistent CloudKit container.
- [var resultType: NSPersistentCloudKitContainerEventResult.ResultType](nspersistentcloudkitcontainereventrequest/resulttype.md)
  The type of result that the request returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainereventrequest/fetchevents(after:)-5izg7)*