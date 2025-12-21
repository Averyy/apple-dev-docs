# range(of:start:interval:for:)

**Framework**: Foundation  
**Kind**: method

Returns by reference the starting time and duration of a given calendar unit that contains a given date.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func range(of unit: NSCalendar.Unit, start datep: AutoreleasingUnsafeMutablePointer<NSDate?>?, interval tip: UnsafeMutablePointer<TimeInterval>?, for date: Date) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the starting time and duration of a unit could be calculated, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `unit`: A calendar unit (see   for possible values).
- `datep`: Upon return, contains the starting time of the calendar unit   that contains the date 
- `tip`: Upon return, contains the duration of the calendar unit   that contains the date 
- `date`: A date.

## See Also

- [var calendarIdentifier: NSCalendar.Identifier](nscalendar/calendaridentifier.md)
  An identifier for the calendar.
- [var firstWeekday: Int](nscalendar/firstweekday.md)
  The index of the first weekday of the receiver.
- [var locale: Locale?](nscalendar/locale.md)
  The locale of the receiver.
- [var timeZone: TimeZone](nscalendar/timezone.md)
  The time zone for the calendar.
- [func maximumRange(of: NSCalendar.Unit) -> NSRange](nscalendar/maximumrange(of:).md)
  Returns the maximum range limits of the values that a given unit can take on.
- [func minimumRange(of: NSCalendar.Unit) -> NSRange](nscalendar/minimumrange(of:).md)
  Returns the minimum range limits of the values that a given unit can take on.
- [var minimumDaysInFirstWeek: Int](nscalendar/minimumdaysinfirstweek.md)
  The minimum number of days in the first week of the receiver.
- [func ordinality(of: NSCalendar.Unit, in: NSCalendar.Unit, for: Date) -> Int](nscalendar/ordinality(of:in:for:).md)
  Returns, for a given absolute time, the ordinal number of a smaller calendar unit (such as a day) within a specified larger calendar unit (such as a week).
- [func range(of: NSCalendar.Unit, in: NSCalendar.Unit, for: Date) -> NSRange](nscalendar/range(of:in:for:).md)
  Returns the range of absolute time values that a smaller calendar unit (such as a day) can take on in a larger calendar unit (such as a month) that includes a specified absolute time.
- [func range(ofWeekendStart: AutoreleasingUnsafeMutablePointer<NSDate?>?, interval: UnsafeMutablePointer<TimeInterval>?, containing: Date) -> Bool](nscalendar/range(ofweekendstart:interval:containing:).md)
  Returns whether a given date falls within a weekend period, and if so, returns by reference the start date and time interval of the weekend range.
- [NSCalendar.Unit](nscalendar/unit.md)
  Calendrical units such as year, month, day and hour.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/range(of:start:interval:for:))*