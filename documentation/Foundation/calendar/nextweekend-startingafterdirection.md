# nextWeekend(startingAfter:direction:)

**Framework**: Foundation  
**Kind**: method

Returns a `DateInterval` of the next weekend, which starts strictly after the given date.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func nextWeekend(startingAfter date: Date, direction: Calendar.SearchDirection = .forward) -> DateInterval?
```

#### Return Value

A `DateInterval`, or `nil` if weekends do not exist in the specific calendar or locale.

#### Discussion

If `direction` is `.backward`, then finds the previous weekend range strictly before the given date.

Note that a given entire day within a calendar is not necessarily all in a weekend or not; weekends can start in the middle of a day in some calendars and locales.

## Parameters

- `date`: The date at which to begin the search.
- `direction`: Which direction in time to search. The default value is  .

## See Also

- [func dateInterval(of: Calendar.Component, for: Date) -> DateInterval?](calendar/dateinterval(of:for:).md)
  Returns the starting time and duration of a given calendar component that contains a given date.
- [func dateInterval(of: Calendar.Component, start: inout Date, interval: inout TimeInterval, for: Date) -> Bool](calendar/dateinterval(of:start:interval:for:).md)
  Returns, via two inout parameters, the starting time and duration of a given calendar component that contains a given date.
- [func dateIntervalOfWeekend(containing: Date) -> DateInterval?](calendar/dateintervalofweekend(containing:).md)
  Returns a `DateInterval` of the weekend contained by the given date, or `nil` if the date is not in a weekend.
- [func dateIntervalOfWeekend(containing: Date, start: inout Date, interval: inout TimeInterval) -> Bool](calendar/dateintervalofweekend(containing:start:interval:).md)
  Find the range of the weekend around the given date, returned via two by-reference parameters.
- [func nextWeekend(startingAfter: Date, start: inout Date, interval: inout TimeInterval, direction: Calendar.SearchDirection) -> Bool](calendar/nextweekend(startingafter:start:interval:direction:).md)
  Returns the range of the next weekend via two inout parameters. The weekend starts strictly after the given date.
- [Calendar.SearchDirection](calendar/searchdirection.md)
  The direction in time to search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/nextweekend(startingafter:direction:))*