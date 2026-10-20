# timeZone

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

The time zone for the calendar item.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var timeZone: TimeZone? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSTimeZone * timeZone;
```

#### Discussion

If `nil`, the calendar item is a floating event. A floating event is not tied to a particular time zone. It occurs at a given time regardless of the time zone — for example, “lunch at noon.” The start and end times of a floating event should be set as if they were in the system time zone.

## See Also

### Accessing Calendar Item Properties
- [var calendar: EKCalendar!](./calendar.md)
  The calendar for the calendar item.
- [var title: String!](./title.md)
  The title for the calendar item.
- [var location: String?](./location.md)
  The location associated with the calendar item.
- [var creationDate: Date?](./creationdate.md)
  The date that this calendar item was created.
- [var lastModifiedDate: Date?](./lastmodifieddate.md)
  The date that the calendar item was last modified.
- [var url: URL?](./url.md)
  The URL for the calendar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekcalendaritem/timezone)*