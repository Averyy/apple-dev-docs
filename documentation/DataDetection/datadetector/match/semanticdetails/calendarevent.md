# DataDetector.Match.SemanticDetails.CalendarEvent

**Framework**: DataDetection  
**Kind**: struct  
**Role**: Structure

The values the framework returns that represent date components of a calendar event.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct CalendarEvent
```

#### Discussion

You can use these properties to populate an Event. The event may contain just a single date, such as a start date, but can contain both a start and end date.

- [`allDay`](./calendarevent/allday.md) is `true` if the date or date range doesn’t specify a time.
- [`startDate`](./calendarevent/startdate.md) may contain the start date of the event.
- [`endDate`](./calendarevent/enddate.md) may contain the end date of the event.
- [`endTimeZone`](./calendarevent/endtimezone.md) may contain the time zone of the end date of the event.
- [`startTimeZone`](./calendarevent/starttimezone.md) may contain the time zone of the start date of the event.

## Topics

### Calendar event properties
- [let allDay: Bool](./calendarevent/allday.md)
  A Boolean value that indicates whether the event is an all-day event.
- [let startDate: Date?](./calendarevent/startdate.md)
  An optional date that may contain the start date of the event.
- [let endDate: Date?](./calendarevent/enddate.md)
  An optional date that may contain the end date of the event.
- [let startTimeZone: TimeZone?](./calendarevent/starttimezone.md)
  An optional time zone object that may contain the time zone of the start date of the event.
- [let endTimeZone: TimeZone?](./calendarevent/endtimezone.md)
  An optional time zone object that may contain the time zone of the end date of the event.

## Relationships

### Conforms To
- [Copyable](../../../../Swift/copyable.md)
- [Decodable](../../../../Swift/decodable.md)
- [Encodable](../../../../Swift/encodable.md)
- [Equatable](../../../../Swift/equatable.md)
- [Escapable](../../../../Swift/escapable.md)
- [Hashable](../../../../Swift/hashable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/datadetection/datadetector/match/semanticdetails/calendarevent)*