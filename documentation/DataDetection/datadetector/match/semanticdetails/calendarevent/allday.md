# allDay

**Framework**: DataDetection  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the event is an all-day event.

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
let allDay: Bool
```

## Discussion

This may be `true` if the date or date range doesn’t specify a time.

## See Also

### Calendar event properties
- [let startDate: Date?](./startdate.md)
  An optional date that may contain the start date of the event.
- [let endDate: Date?](./enddate.md)
  An optional date that may contain the end date of the event.
- [let startTimeZone: TimeZone?](./starttimezone.md)
  An optional time zone object that may contain the time zone of the start date of the event.
- [let endTimeZone: TimeZone?](./endtimezone.md)
  An optional time zone object that may contain the time zone of the end date of the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/datadetection/datadetector/match/semanticdetails/calendarevent/allday)*