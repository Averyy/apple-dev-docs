# dateInterval(of:for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the starting time and duration of a given calendar component that contains a given date.

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
func dateInterval(of component: Calendar.Component, for date: Date) -> DateInterval?
```

## Return Value

A new `DateInterval` if the starting time and duration of a component could be calculated; otherwise, `nil`.

## Parameters

- `component`: A calendar component.
- `date`: The specified date.

## See Also

### Calculating Intervals
- [func dateInterval(of: Calendar.Component, start: inout Date, interval: inout TimeInterval, for: Date) -> Bool](./dateinterval%28of,start,interval,for%29.md)
  Returns, via two inout parameters, the starting time and duration of a given calendar component that contains a given date.
- [func dateIntervalOfWeekend(containing: Date) -> DateInterval?](./dateintervalofweekend%28containing%29.md)
  Returns a `DateInterval` of the weekend contained by the given date, or `nil` if the date is not in a weekend.
- [func dateIntervalOfWeekend(containing: Date, start: inout Date, interval: inout TimeInterval) -> Bool](./dateintervalofweekend%28containing,start,interval%29.md)
  Find the range of the weekend around the given date, returned via two by-reference parameters.
- [func nextWeekend(startingAfter: Date, direction: Calendar.SearchDirection) -> DateInterval?](./nextweekend%28startingafter,direction%29.md)
  Returns a `DateInterval` of the next weekend, which starts strictly after the given date.
- [func nextWeekend(startingAfter: Date, start: inout Date, interval: inout TimeInterval, direction: Calendar.SearchDirection) -> Bool](./nextweekend%28startingafter,start,interval,direction%29.md)
  Returns the range of the next weekend via two inout parameters. The weekend starts strictly after the given date.
- [Calendar.SearchDirection](./searchdirection.md)
  The direction in time to search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/dateinterval(of:for:))*