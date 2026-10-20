# dateIntervalOfWeekend(containing:start:interval:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Find the range of the weekend around the given date, returned via two by-reference parameters.

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
func dateIntervalOfWeekend(containing date: Date, start: inout Date, interval: inout TimeInterval) -> Bool
```

#### Return Value

`true` if a date range could be found, and `false` if the date is not in a weekend.

#### Discussion

Note that a given entire day within a calendar is not necessarily all in a weekend or not; weekends can start in the middle of a day in some calendars and locales.

## Parameters

- `date`: The date at which to start the search.
- `start`: When the result is `true`, set

## See Also

### Calculating Intervals
- [func dateInterval(of: Calendar.Component, for: Date) -> DateInterval?](./dateinterval%28of,for%29.md)
  Returns the starting time and duration of a given calendar component that contains a given date.
- [func dateInterval(of: Calendar.Component, start: inout Date, interval: inout TimeInterval, for: Date) -> Bool](./dateinterval%28of,start,interval,for%29.md)
  Returns, via two inout parameters, the starting time and duration of a given calendar component that contains a given date.
- [func dateIntervalOfWeekend(containing: Date) -> DateInterval?](./dateintervalofweekend%28containing%29.md)
  Returns a `DateInterval` of the weekend contained by the given date, or `nil` if the date is not in a weekend.
- [func nextWeekend(startingAfter: Date, direction: Calendar.SearchDirection) -> DateInterval?](./nextweekend%28startingafter,direction%29.md)
  Returns a `DateInterval` of the next weekend, which starts strictly after the given date.
- [func nextWeekend(startingAfter: Date, start: inout Date, interval: inout TimeInterval, direction: Calendar.SearchDirection) -> Bool](./nextweekend%28startingafter,start,interval,direction%29.md)
  Returns the range of the next weekend via two inout parameters. The weekend starts strictly after the given date.
- [Calendar.SearchDirection](./searchdirection.md)
  The direction in time to search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/dateintervalofweekend(containing:start:interval:))*