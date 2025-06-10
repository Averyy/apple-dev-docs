# Calendar.MatchingPolicy

**Framework**: Foundation  
**Kind**: enum

A hint to the search algorithm to control the method used for searching for dates.

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
enum MatchingPolicy
```

## Topics

### Enumeration Cases
- [Calendar.MatchingPolicy.nextTime](calendar/matchingpolicy/nexttime.md)
  If there is no matching time before the end of the next instance of the next higher component to the highest specified component in the `DateComponents` argument, the algorithm will return the next existing time which exists.
- [Calendar.MatchingPolicy.nextTimePreservingSmallerComponents](calendar/matchingpolicy/nexttimepreservingsmallercomponents.md)
  If specified, and there is no matching time before the end of the next instance of the next higher component to the highest specified component in the `DateComponents` argument, the method returns the next existing value of the missing component and preserves the lower components’ values (for example, no 2:37am results in 3:37am, if that exists).
- [Calendar.MatchingPolicy.previousTimePreservingSmallerComponents](calendar/matchingpolicy/previoustimepreservingsmallercomponents.md)
  If there is no matching time before the end of the next instance of the next higher component to the highest specified component in the `DateComponents` argument, the algorithm will return the previous existing value of the missing component and preserves the lower components’ values.
- [Calendar.MatchingPolicy.strict](calendar/matchingpolicy/strict.md)
  If specified, the algorithm travels as far forward or backward as necessary looking for a match.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func startOfDay(for: Date) -> Date](calendar/startofday(for:).md)
  Returns the first moment of a given Date, as a Date.
- [func enumerateDates(startingAfter: Date, matching: DateComponents, matchingPolicy: Calendar.MatchingPolicy, repeatedTimePolicy: Calendar.RepeatedTimePolicy, direction: Calendar.SearchDirection, using: (Date?, Bool, inout Bool) -> Void)](calendar/enumeratedates(startingafter:matching:matchingpolicy:repeatedtimepolicy:direction:using:).md)
  Computes the dates which match (or most closely match) a given set of components, and calls the closure once for each of them, until the enumeration is stopped.
- [func nextDate(after: Date, matching: DateComponents, matchingPolicy: Calendar.MatchingPolicy, repeatedTimePolicy: Calendar.RepeatedTimePolicy, direction: Calendar.SearchDirection) -> Date?](calendar/nextdate(after:matching:matchingpolicy:repeatedtimepolicy:direction:).md)
  Computes the next date which matches (or most closely matches) a given set of components.
- [Calendar.RepeatedTimePolicy](calendar/repeatedtimepolicy.md)
  Determines which result to use when a time is repeated on a day in a calendar (for example, during a daylight saving transition when the times between 2:00am and 3:00am may happen twice).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/matchingpolicy)*