# CFCalendarGetMaximumRangeOfUnit(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the maximum range limits of the values that a specified unit can take on in a given calendar.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFCalendarGetMaximumRangeOfUnit(_ calendar: CFCalendar!, _ unit: CFCalendarUnit) -> CFRange
```

```c
extern CFRange CFCalendarGetMaximumRangeOfUnit(CFCalendarRef calendar, CFCalendarUnit unit);
```

## Return Value

The maximum range limits of the values that the specified unit can take on in `calendar`. For example, in the Gregorian calendar the maximum ranges for the Day unit is 1-31.

## Parameters

- `calendar`: The calendar to examine.
- `unit`: A calendar unit. For valid values see [`CFCalendarUnit`](./cfcalendarunit.md).

## See Also

### Getting Ranges of Units
- [func CFCalendarGetRangeOfUnit(CFCalendar!, CFCalendarUnit, CFCalendarUnit, CFAbsoluteTime) -> CFRange](./cfcalendargetrangeofunit%28_,_,_,_%29.md)
  Returns the range of values that one unit can take on within a larger unit during which a specific absolute time occurs.
- [func CFCalendarGetOrdinalityOfUnit(CFCalendar!, CFCalendarUnit, CFCalendarUnit, CFAbsoluteTime) -> CFIndex](./cfcalendargetordinalityofunit%28_,_,_,_%29.md)
  Returns the ordinal number of a calendrical unit within a larger unit at a specified absolute time.
- [func CFCalendarGetTimeRangeOfUnit(CFCalendar!, CFCalendarUnit, CFAbsoluteTime, UnsafeMutablePointer<CFAbsoluteTime>!, UnsafeMutablePointer<CFTimeInterval>!) -> Bool](./cfcalendargettimerangeofunit%28_,_,_,_,_%29.md)
  Returns by reference the start time and duration of a given calendar unit that contains a given absolute time.
- [func CFCalendarGetMinimumRangeOfUnit(CFCalendar!, CFCalendarUnit) -> CFRange](./cfcalendargetminimumrangeofunit%28_,_%29.md)
  Returns the minimum range limits of the values that a specified unit can take on in a given calendar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcalendargetmaximumrangeofunit(_:_:))*