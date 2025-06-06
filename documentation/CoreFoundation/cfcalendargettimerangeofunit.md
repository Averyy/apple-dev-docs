# CFCalendarGetTimeRangeOfUnit(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns by reference the start time and duration of a given calendar unit that contains a given absolute time.

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
func CFCalendarGetTimeRangeOfUnit(_ calendar: CFCalendar!, _ unit: CFCalendarUnit, _ at: CFAbsoluteTime, _ startp: UnsafeMutablePointer<CFAbsoluteTime>!, _ tip: UnsafeMutablePointer<CFTimeInterval>!) -> Bool
```

#### Return Value

`true` if the values of `startp` and `tip` could be calculated, otherwise `false`.

#### Discussion

The function may fail if, for example, you try to get the range of a `kCFCalendarUnitWeekday` and specify a time (`at`) that is during a weekend.

## Parameters

- `calendar`: The calendar to examine.
- `unit`: A calendar unit (for valid values, see  ).
- `at`: An absolute time.
- `startp`: Upon return, contains the beginning of the calendar unit specified by   that contains the time  .
- `tip`: Upon return, contains the duration of the calendar unit specified by   that contains the time  .

## See Also

- [func CFCalendarGetRangeOfUnit(CFCalendar!, CFCalendarUnit, CFCalendarUnit, CFAbsoluteTime) -> CFRange](cfcalendargetrangeofunit(_:_:_:_:).md)
  Returns the range of values that one unit can take on within a larger unit during which a specific absolute time occurs.
- [func CFCalendarGetOrdinalityOfUnit(CFCalendar!, CFCalendarUnit, CFCalendarUnit, CFAbsoluteTime) -> CFIndex](cfcalendargetordinalityofunit(_:_:_:_:).md)
  Returns the ordinal number of a calendrical unit within a larger unit at a specified absolute time.
- [func CFCalendarGetMaximumRangeOfUnit(CFCalendar!, CFCalendarUnit) -> CFRange](cfcalendargetmaximumrangeofunit(_:_:).md)
  Returns the maximum range limits of the values that a specified unit can take on in a given calendar.
- [func CFCalendarGetMinimumRangeOfUnit(CFCalendar!, CFCalendarUnit) -> CFRange](cfcalendargetminimumrangeofunit(_:_:).md)
  Returns the minimum range limits of the values that a specified unit can take on in a given calendar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcalendargettimerangeofunit(_:_:_:_:_:))*