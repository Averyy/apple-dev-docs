# CFCalendarGetRangeOfUnit(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the range of values that one unit can take on within a larger unit during which a specific absolute time occurs.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFCalendarGetRangeOfUnit(_ calendar: CFCalendar!, _ smallerUnit: CFCalendarUnit, _ biggerUnit: CFCalendarUnit, _ at: CFAbsoluteTime) -> CFRange
```

#### Return Value

The range of values that the calendar unit specified by `smallerUnit` can take on within the calendar unit specified by `biggerUnit` that includes the absolute time `at`. For example, the range the Day unit can take on in the Month in which the absolute time lies.

#### Discussion

If `biggerUnit` is not logically bigger than `smallerUnit` in the calendar, or the given combination of units does not make sense (or is a computation which is undefined), the result is `{kCFNotFound, kCFNotFound`}.

## Parameters

- `calendar`: The calendar to examine.
- `smallerUnit`: A calendar unit. For valid values see  .
- `biggerUnit`: A calendar unit. For valid values see  .
- `at`: An absolute time.

## See Also

- [func CFCalendarGetOrdinalityOfUnit(CFCalendar!, CFCalendarUnit, CFCalendarUnit, CFAbsoluteTime) -> CFIndex](cfcalendargetordinalityofunit(_:_:_:_:).md)
  Returns the ordinal number of a calendrical unit within a larger unit at a specified absolute time.
- [func CFCalendarGetTimeRangeOfUnit(CFCalendar!, CFCalendarUnit, CFAbsoluteTime, UnsafeMutablePointer<CFAbsoluteTime>!, UnsafeMutablePointer<CFTimeInterval>!) -> Bool](cfcalendargettimerangeofunit(_:_:_:_:_:).md)
  Returns by reference the start time and duration of a given calendar unit that contains a given absolute time.
- [func CFCalendarGetMaximumRangeOfUnit(CFCalendar!, CFCalendarUnit) -> CFRange](cfcalendargetmaximumrangeofunit(_:_:).md)
  Returns the maximum range limits of the values that a specified unit can take on in a given calendar.
- [func CFCalendarGetMinimumRangeOfUnit(CFCalendar!, CFCalendarUnit) -> CFRange](cfcalendargetminimumrangeofunit(_:_:).md)
  Returns the minimum range limits of the values that a specified unit can take on in a given calendar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcalendargetrangeofunit(_:_:_:_:))*