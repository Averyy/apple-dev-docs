# dateComponents(in:from:)

**Framework**: Foundation  
**Kind**: method

Returns all the date components of a date, as if in a given time zone (instead of the `Calendar` time zone).

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
func dateComponents(in timeZone: TimeZone, from date: Date) -> DateComponents
```

#### Return Value

All components, calculated using the `Calendar` and `TimeZone`.

#### Discussion

The time zone overrides the time zone of the `Calendar` for the purposes of this calculation.

> **Note**:  If you want “date information in a given time zone” in order to display it, you should use `DateFormatter` to format the date.

 If you want “date information in a given time zone” in order to display it, you should use `DateFormatter` to format the date.

## Parameters

- `timeZone`: The   to use.
- `date`: The   to use.

## See Also

- [func date(Date, matchesComponents: DateComponents) -> Bool](calendar/date(_:matchescomponents:).md)
  Determines if the date has all of the specified date components.
- [func component(Calendar.Component, from: Date) -> Int](calendar/component(_:from:).md)
  Returns the value for one component of a date.
- [func dateComponents(Set<Calendar.Component>, from: Date) -> DateComponents](calendar/datecomponents(_:from:).md)
  Returns all the date components of a date, using the calendar time zone.
- [func dateComponents(Set<Calendar.Component>, from: Date, to: Date) -> DateComponents](calendar/datecomponents(_:from:to:)-2kcg.md)
  Returns the difference between two dates.
- [func dateComponents(Set<Calendar.Component>, from: DateComponents, to: DateComponents) -> DateComponents](calendar/datecomponents(_:from:to:)-5g20t.md)
  Returns the difference between two dates specified as `DateComponents`.
- [Calendar.Component](calendar/component.md)
  An enumeration for the various components of a calendar date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/datecomponents(in:from:))*