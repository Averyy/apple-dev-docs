# CFCalendarGetMaximumRangeOfUnit(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the maximum range limits of the values that a specified unit can take on in a given calendar.

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
func CFCalendarGetMaximumRangeOfUnit(_ calendar: CFCalendar!, _ unit: CFCalendarUnit) -> CFRange
```

#### Return Value

The maximum range limits of the values that the specified unit can take on in `calendar`. For example, in the Gregorian calendar the maximum ranges for the Day unit is 1-31.

## Parameters

- `calendar`: The calendar to examine.
- `unit`: A calendar unit. For valid values see  .

## See Also

- [func CFCalendarGetRangeOfUnit(CFCalendar!, CFCalendarUnit, CFCalendarUnit, CFAbsoluteTime) -> CFRange](cfcalendargetrangeofunit(_:_:_:_:).md)
  Returns the range of values that one unit can take on within a larger unit during which a specific absolute time occurs.
- [func CFCalendarGetOrdinalityOfUnit(CFCalendar!, CFCalendarUnit, CFCalendarUnit, CFAbsoluteTime) -> CFIndex](cfcalendargetordinalityofunit(_:_:_:_:).md)
  Returns the ordinal number of a calendrical unit within a larger unit at a specified absolute time.
- [func CFCalendarGetTimeRangeOfUnit(CFCalendar!, CFCalendarUnit, CFAbsoluteTime, UnsafeMutablePointer<CFAbsoluteTime>!, UnsafeMutablePointer<CFTimeInterval>!) -> Bool](cfcalendargettimerangeofunit(_:_:_:_:_:).md)
  Returns by reference the start time and duration of a given calendar unit that contains a given absolute time.
- [func CFCalendarGetMinimumRangeOfUnit(CFCalendar!, CFCalendarUnit) -> CFRange](cfcalendargetminimumrangeofunit(_:_:).md)
  Returns the minimum range limits of the values that a specified unit can take on in a given calendar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcalendargetmaximumrangeofunit(_:_:))*