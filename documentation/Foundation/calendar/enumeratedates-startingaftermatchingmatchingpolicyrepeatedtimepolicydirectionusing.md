# enumerateDates(startingAfter:matching:matchingPolicy:repeatedTimePolicy:direction:using:)

**Framework**: Foundation  
**Kind**: method

Computes the dates which match (or most closely match) a given set of components, and calls the closure once for each of them, until the enumeration is stopped.

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
func enumerateDates(startingAfter start: Date, matching components: DateComponents, matchingPolicy: Calendar.MatchingPolicy, repeatedTimePolicy: Calendar.RepeatedTimePolicy = .first, direction: Calendar.SearchDirection = .forward, using block: (Date?, Bool, inout Bool) -> Void)
```

#### Discussion

There will be at least one intervening date which does not match all the components (or the given date itself must not match) between the given date and any result.

If `direction` is set to `.backward`, this method finds the previous match before the given date. The intent is that the same matches as for a `.forward` search will be found (that is, if you are enumerating forwards or backwards for each hour with minute “27”, the seconds in the date you will get in forwards search would obviously be 00, and the same will be true in a backwards search in order to implement this rule.  Similarly for DST backwards jumps which repeats times, you’ll get the first match by default, where “first” is defined from the point of view of searching forwards.  So, when searching backwards looking for a particular hour, with no minute and second specified, you don’t get a minute and second of 59:59 for the matching hour (which would be the nominal first match within a given hour, given the other rules here, when searching backwards).

If an exact match is not possible, and requested with the `strict` option, nil is passed to the closure and the enumeration ends.  (Logically, since an exact match searches indefinitely into the future, if no match is found there’s no point in continuing the enumeration.)

Result dates have an integer number of seconds (as if 0 was specified for the nanoseconds property of the `DateComponents` matching parameter), unless a value was set in the nanoseconds property, in which case the result date will have that number of nanoseconds (or as close as possible with floating point numbers).

The enumeration is stopped by setting `stop` to `true` in the closure and returning. It is not necessary to set `stop` to `false` to keep the enumeration going.

## Parameters

- `start`: The   at which to start the search.
- `components`: The   to use as input to the search algorithm.
- `matchingPolicy`: Determines the behavior of the search algorithm when the input produces an ambiguous result.
- `repeatedTimePolicy`: Determines the behavior of the search algorithm when the input produces a time that occurs twice on a particular day.
- `direction`: Which direction in time to search. The default value is  , which means later in time.
- `block`: A closure that is called with search results.

## See Also

- [func startOfDay(for: Date) -> Date](calendar/startofday(for:).md)
  Returns the first moment of a given Date, as a Date.
- [func nextDate(after: Date, matching: DateComponents, matchingPolicy: Calendar.MatchingPolicy, repeatedTimePolicy: Calendar.RepeatedTimePolicy, direction: Calendar.SearchDirection) -> Date?](calendar/nextdate(after:matching:matchingpolicy:repeatedtimepolicy:direction:).md)
  Computes the next date which matches (or most closely matches) a given set of components.
- [Calendar.MatchingPolicy](calendar/matchingpolicy.md)
  A hint to the search algorithm to control the method used for searching for dates.
- [Calendar.RepeatedTimePolicy](calendar/repeatedtimepolicy.md)
  Determines which result to use when a time is repeated on a day in a calendar (for example, during a daylight saving transition when the times between 2:00am and 3:00am may happen twice).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/enumeratedates(startingafter:matching:matchingpolicy:repeatedtimepolicy:direction:using:))*