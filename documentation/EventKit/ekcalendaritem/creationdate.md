# creationDate

**Framework**: EventKit  
**Kind**: property

The date that this calendar item was created.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var creationDate: Date? { get }
```

#### Discussion

If `nil`, this property was not set or was synced in this state.

## See Also

- [var calendar: EKCalendar!](ekcalendaritem/calendar.md)
  The calendar for the calendar item.
- [var title: String!](ekcalendaritem/title.md)
  The title for the calendar item.
- [var location: String?](ekcalendaritem/location.md)
  The location associated with the calendar item.
- [var lastModifiedDate: Date?](ekcalendaritem/lastmodifieddate.md)
  The date that the calendar item was last modified.
- [var timeZone: TimeZone?](ekcalendaritem/timezone.md)
  The time zone for the calendar item.
- [var url: URL?](ekcalendaritem/url.md)
  The URL for the calendar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekcalendaritem/creationdate)*