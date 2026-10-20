# Calendar.RepeatedTimePolicy

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

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
- [Calendar.RepeatedTimePolicy.first](./repeatedtimepolicy/first.md)
  If there are two or more matching times (all the components are the same, including isLeapMonth) before the end of the next instance of the next higher component to the highest specified component, then the algorithm will return the first occurrence.
- [Calendar.RepeatedTimePolicy.last](./repeatedtimepolicy/last.md)
  If there are two or more matching times (all the components are the same, including isLeapMonth) before the end of the next instance of the next higher component to the highest specified component, then the algorithm will return the last occurrence.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Scanning Dates
- [func startOfDay(for: Date) -> Date](./startofday%28for%29.md)
  Returns the first moment of a given Date, as a Date.
- [func enumerateDates(startingAfter: Date, matching: DateComponents, matchingPolicy: Calendar.MatchingPolicy, repeatedTimePolicy: Calendar.RepeatedTimePolicy, direction: Calendar.SearchDirection, using: (Date?, Bool, inout Bool) -> Void)](./enumeratedates%28startingafter,matching,matchingpolicy,repeatedtimepolicy,direction,using%29.md)
  Computes the dates which match (or most closely match) a given set of components, and calls the closure once for each of them, until the enumeration is stopped.
- [func nextDate(after: Date, matching: DateComponents, matchingPolicy: Calendar.MatchingPolicy, repeatedTimePolicy: Calendar.RepeatedTimePolicy, direction: Calendar.SearchDirection) -> Date?](./nextdate%28after,matching,matchingpolicy,repeatedtimepolicy,direction%29.md)
  Computes the next date which matches (or most closely matches) a given set of components.
- [Calendar.MatchingPolicy](./matchingpolicy.md)
  A hint to the search algorithm to control the method used for searching for dates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/repeatedtimepolicy)*