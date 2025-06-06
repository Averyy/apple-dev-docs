# CFCalendarGetMinimumRangeOfUnit(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the minimum range limits of the values that a specified unit can take on in a given calendar.

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
func CFCalendarGetMinimumRangeOfUnit(_ calendar: CFCalendar!, _ unit: CFCalendarUnit) -> CFRange
```

#### Return Value

The minimum range limits of the values that the specified unit can take on in `calendar`. For example, in the Gregorian calendar the minimum ranges for the Day unit is 1-28.

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
- [func CFCalendarGetMaximumRangeOfUnit(CFCalendar!, CFCalendarUnit) -> CFRange](cfcalendargetmaximumrangeofunit(_:_:).md)
  Returns the maximum range limits of the values that a specified unit can take on in a given calendar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcalendargetminimumrangeofunit(_:_:))*