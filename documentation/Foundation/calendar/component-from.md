# component(_:from:)

**Framework**: Foundation  
**Kind**: method

Returns the value for one component of a date.

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
func component(_ component: Calendar.Component, from date: Date) -> Int
```

#### Return Value

The value for the component.

## Parameters

- `component`: The component to calculate.
- `date`: The date to use.

## See Also

- [func date(Date, matchesComponents: DateComponents) -> Bool](calendar/date(_:matchescomponents:).md)
  Determines if the date has all of the specified date components.
- [func dateComponents(Set<Calendar.Component>, from: Date) -> DateComponents](calendar/datecomponents(_:from:).md)
  Returns all the date components of a date, using the calendar time zone.
- [func dateComponents(Set<Calendar.Component>, from: Date, to: Date) -> DateComponents](calendar/datecomponents(_:from:to:)-2kcg.md)
  Returns the difference between two dates.
- [func dateComponents(Set<Calendar.Component>, from: DateComponents, to: DateComponents) -> DateComponents](calendar/datecomponents(_:from:to:)-5g20t.md)
  Returns the difference between two dates specified as `DateComponents`.
- [func dateComponents(in: TimeZone, from: Date) -> DateComponents](calendar/datecomponents(in:from:).md)
  Returns all the date components of a date, as if in a given time zone (instead of the `Calendar` time zone).
- [Calendar.Component](calendar/component.md)
  An enumeration for the various components of a calendar date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/component(_:from:))*