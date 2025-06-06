# nextDate(after:matching:matchingPolicy:repeatedTimePolicy:direction:)

**Framework**: Foundation  
**Kind**: method

Computes the next date which matches (or most closely matches) a given set of components.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func nextDate(after date: Date, matching components: DateComponents, matchingPolicy: Calendar.MatchingPolicy, repeatedTimePolicy: Calendar.RepeatedTimePolicy = .first, direction: Calendar.SearchDirection = .forward) -> Date?
```

#### Return Value

A `Date` representing the result of the search, or `nil` if a result could not be found.

#### Discussion

The general semantics follow those of the `enumerateDates` function. To compute a sequence of results, use the `enumerateDates` function, rather than looping and calling this method with the previous loop iteration’s result.

## Parameters

- `date`: The starting date.
- `components`: The components to search for.
- `matchingPolicy`: Specifies the technique the search algorithm uses to find results. Default value is  .
- `repeatedTimePolicy`: Specifies the behavior when multiple matches are found. Default value is  .
- `direction`: Specifies the direction in time to search. Default is  .

## See Also

- [func startOfDay(for: Date) -> Date](calendar/startofday(for:).md)
  Returns the first moment of a given Date, as a Date.
- [func enumerateDates(startingAfter: Date, matching: DateComponents, matchingPolicy: Calendar.MatchingPolicy, repeatedTimePolicy: Calendar.RepeatedTimePolicy, direction: Calendar.SearchDirection, using: (Date?, Bool, inout Bool) -> Void)](calendar/enumeratedates(startingafter:matching:matchingpolicy:repeatedtimepolicy:direction:using:).md)
  Computes the dates which match (or most closely match) a given set of components, and calls the closure once for each of them, until the enumeration is stopped.
- [Calendar.MatchingPolicy](calendar/matchingpolicy.md)
  A hint to the search algorithm to control the method used for searching for dates.
- [Calendar.RepeatedTimePolicy](calendar/repeatedtimepolicy.md)
  Determines which result to use when a time is repeated on a day in a calendar (for example, during a daylight saving transition when the times between 2:00am and 3:00am may happen twice).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/nextdate(after:matching:matchingpolicy:repeatedtimepolicy:direction:))*