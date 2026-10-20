# resultType

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The type of result that the request returns.

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
var resultType: NSPersistentCloudKitContainerEventResult.ResultType { get set }
```

```objc
@property NSPersistentCloudKitContainerEventResultType resultType;
```

## See Also

### Fetching Events
- [class func fetchEvents(after: Date) -> Self](./fetchevents%28after%29-5izg7.md)
  Creates a fetch request for events after a specified date from a persistent CloudKit container.
- [class func fetchEvents(after: NSPersistentCloudKitContainer.Event?) -> Self](./fetchevents%28after%29-3yfp.md)
  Creates a fetch request for events that occur after a specified event from a persistent CloudKit container.
- [class func fetchEvents(matchingFetch: NSFetchRequest<any NSFetchRequestResult>) -> Self](./fetchevents%28matchingfetch%29.md)
  Creates a fetch request for events that match a specified fetch request from a persistent CloudKit container.
- [class func fetchForEvents() -> NSFetchRequest<any NSFetchRequestResult>](./fetchforevents%28%29.md)
  Creates a fetch request for all events in a persistent CloudKit container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainereventrequest/resulttype)*