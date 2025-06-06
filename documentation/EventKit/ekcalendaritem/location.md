# location

**Framework**: EventKit  
**Kind**: property

The location associated with the calendar item.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var location: String? { get set }
```

#### Discussion

This property is `nil` if the calendar item has no location.

## See Also

- [var calendar: EKCalendar!](ekcalendaritem/calendar.md)
  The calendar for the calendar item.
- [var title: String!](ekcalendaritem/title.md)
  The title for the calendar item.
- [var creationDate: Date?](ekcalendaritem/creationdate.md)
  The date that this calendar item was created.
- [var lastModifiedDate: Date?](ekcalendaritem/lastmodifieddate.md)
  The date that the calendar item was last modified.
- [var timeZone: TimeZone?](ekcalendaritem/timezone.md)
  The time zone for the calendar item.
- [var url: URL?](ekcalendaritem/url.md)
  The URL for the calendar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekcalendaritem/location)*