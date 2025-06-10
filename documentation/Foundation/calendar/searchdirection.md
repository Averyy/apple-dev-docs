# Calendar.SearchDirection

**Framework**: Foundation  
**Kind**: enum

The direction in time to search.

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
enum SearchDirection
```

## Topics

### Enumeration Cases
- [Calendar.SearchDirection.backward](calendar/searchdirection/backward.md)
  Search for a date earlier in time than the start date.
- [Calendar.SearchDirection.forward](calendar/searchdirection/forward.md)
  Search for a date later in time than the start date.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func dateInterval(of: Calendar.Component, for: Date) -> DateInterval?](calendar/dateinterval(of:for:).md)
  Returns the starting time and duration of a given calendar component that contains a given date.
- [func dateInterval(of: Calendar.Component, start: inout Date, interval: inout TimeInterval, for: Date) -> Bool](calendar/dateinterval(of:start:interval:for:).md)
  Returns, via two inout parameters, the starting time and duration of a given calendar component that contains a given date.
- [func dateIntervalOfWeekend(containing: Date) -> DateInterval?](calendar/dateintervalofweekend(containing:).md)
  Returns a `DateInterval` of the weekend contained by the given date, or `nil` if the date is not in a weekend.
- [func dateIntervalOfWeekend(containing: Date, start: inout Date, interval: inout TimeInterval) -> Bool](calendar/dateintervalofweekend(containing:start:interval:).md)
  Find the range of the weekend around the given date, returned via two by-reference parameters.
- [func nextWeekend(startingAfter: Date, direction: Calendar.SearchDirection) -> DateInterval?](calendar/nextweekend(startingafter:direction:).md)
  Returns a `DateInterval` of the next weekend, which starts strictly after the given date.
- [func nextWeekend(startingAfter: Date, start: inout Date, interval: inout TimeInterval, direction: Calendar.SearchDirection) -> Bool](calendar/nextweekend(startingafter:start:interval:direction:).md)
  Returns the range of the next weekend via two inout parameters. The weekend starts strictly after the given date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/searchdirection)*