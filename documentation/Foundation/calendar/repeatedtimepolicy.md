# Calendar.RepeatedTimePolicy

**Framework**: Foundation  
**Kind**: enum

Determines which result to use when a time is repeated on a day in a calendar (for example, during a daylight saving transition when the times between 2:00am and 3:00am may happen twice).

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
enum RepeatedTimePolicy
```

## Topics

### Enumeration Cases
- [Calendar.RepeatedTimePolicy.first](calendar/repeatedtimepolicy/first.md)
  If there are two or more matching times (all the components are the same, including isLeapMonth) before the end of the next instance of the next higher component to the highest specified component, then the algorithm will return the first occurrence.
- [Calendar.RepeatedTimePolicy.last](calendar/repeatedtimepolicy/last.md)
  If there are two or more matching times (all the components are the same, including isLeapMonth) before the end of the next instance of the next higher component to the highest specified component, then the algorithm will return the last occurrence.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func startOfDay(for: Date) -> Date](calendar/startofday(for:).md)
  Returns the first moment of a given Date, as a Date.
- [func enumerateDates(startingAfter: Date, matching: DateComponents, matchingPolicy: Calendar.MatchingPolicy, repeatedTimePolicy: Calendar.RepeatedTimePolicy, direction: Calendar.SearchDirection, using: (Date?, Bool, inout Bool) -> Void)](calendar/enumeratedates(startingafter:matching:matchingpolicy:repeatedtimepolicy:direction:using:).md)
  Computes the dates which match (or most closely match) a given set of components, and calls the closure once for each of them, until the enumeration is stopped.
- [func nextDate(after: Date, matching: DateComponents, matchingPolicy: Calendar.MatchingPolicy, repeatedTimePolicy: Calendar.RepeatedTimePolicy, direction: Calendar.SearchDirection) -> Date?](calendar/nextdate(after:matching:matchingpolicy:repeatedtimepolicy:direction:).md)
  Computes the next date which matches (or most closely matches) a given set of components.
- [Calendar.MatchingPolicy](calendar/matchingpolicy.md)
  A hint to the search algorithm to control the method used for searching for dates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/repeatedtimepolicy)*