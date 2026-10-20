# minimumRange(of:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the minimum range limits of the values that a given unit can take on.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func minimumRange(of unit: NSCalendar.Unit) -> NSRange
```

```objc
- (NSRange) minimumRangeOfUnit:(NSCalendarUnit) unit;
```

#### Return Value

The minimum range limits of the values that the unit specified by `unit` can take on in the receiver.

#### Discussion

As an example, in the Gregorian calendar the minimum range of values for the Day unit is 1-28.

## Parameters

- `unit`: The unit for which the maximum range is returned.

## See Also

### Getting Calendar Information
- [var calendarIdentifier: NSCalendar.Identifier](./calendaridentifier.md)
  An identifier for the calendar.
- [var firstWeekday: Int](./firstweekday.md)
  The index of the first weekday of the receiver.
- [var locale: Locale?](./locale.md)
  The locale of the receiver.
- [var timeZone: TimeZone](./timezone.md)
  The time zone for the calendar.
- [func maximumRange(of: NSCalendar.Unit) -> NSRange](./maximumrange%28of%29.md)
  Returns the maximum range limits of the values that a given unit can take on.
- [var minimumDaysInFirstWeek: Int](./minimumdaysinfirstweek.md)
  The minimum number of days in the first week of the receiver.
- [func ordinality(of: NSCalendar.Unit, in: NSCalendar.Unit, for: Date) -> Int](./ordinality%28of,in,for%29.md)
  Returns, for a given absolute time, the ordinal number of a smaller calendar unit (such as a day) within a specified larger calendar unit (such as a week).
- [func range(of: NSCalendar.Unit, in: NSCalendar.Unit, for: Date) -> NSRange](./range%28of,in,for%29.md)
  Returns the range of absolute time values that a smaller calendar unit (such as a day) can take on in a larger calendar unit (such as a month) that includes a specified absolute time.
- [func range(of: NSCalendar.Unit, start: AutoreleasingUnsafeMutablePointer<NSDate?>?, interval: UnsafeMutablePointer<TimeInterval>?, for: Date) -> Bool](./range%28of,start,interval,for%29.md)
  Returns by reference the starting time and duration of a given calendar unit that contains a given date.
- [func range(ofWeekendStart: AutoreleasingUnsafeMutablePointer<NSDate?>?, interval: UnsafeMutablePointer<TimeInterval>?, containing: Date) -> Bool](./range%28ofweekendstart,interval,containing%29.md)
  Returns whether a given date falls within a weekend period, and if so, returns by reference the start date and time interval of the weekend range.
- [NSCalendar.Unit](./unit.md)
  Calendrical units such as year, month, day and hour.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/minimumrange(of:))*