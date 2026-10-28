# dateComponents(_:from:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns all the date components of a date, using the calendar time zone.

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
func dateComponents(_ components: Set<Calendar.Component>, from date: Date) -> DateComponents
```

## Return Value

The date components of the specified date.

## Discussion

> **Note**:  If you want “date information in a given time zone” in order to display it, you should use `DateFormatter` to format the date.

## Parameters

- `components`: The components to return.
- `date`: The `Date` to use.

## See Also

### Extracting Components
- [func date(Date, matchesComponents: DateComponents) -> Bool](./date%28_,matchescomponents%29.md)
  Determines if the date has all of the specified date components.
- [func component(Calendar.Component, from: Date) -> Int](./component%28_,from%29.md)
  Returns the value for one component of a date.
- [func dateComponents(Set<Calendar.Component>, from: Date, to: Date) -> DateComponents](./datecomponents%28_,from,to%29-2kcg.md)
  Returns the difference between two dates.
- [func dateComponents(Set<Calendar.Component>, from: DateComponents, to: DateComponents) -> DateComponents](./datecomponents%28_,from,to%29-5g20t.md)
  Returns the difference between two dates specified as `DateComponents`.
- [func dateComponents(in: TimeZone, from: Date) -> DateComponents](./datecomponents%28in,from%29.md)
  Returns all the date components of a date, as if in a given time zone (instead of the `Calendar` time zone).
- [Calendar.Component](./component.md)
  An enumeration for the various components of a calendar date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/datecomponents(_:from:))*