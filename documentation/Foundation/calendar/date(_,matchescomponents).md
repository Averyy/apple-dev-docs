# date(_:matchesComponents:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Determines if the date has all of the specified date components.

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
func date(_ date: Date, matchesComponents components: DateComponents) -> Bool
```

## Return Value

`true` if the date matches all of the components, otherwise `false`.

## Discussion

It may be useful to test the return value of `nextDate(after:matching:matchingPolicy:behavior:direction:)` to find out if the components were obeyed or if the method had to fudge the result value due to missing time (for example, a daylight saving time transition).

## See Also

### Extracting Components
- [func component(Calendar.Component, from: Date) -> Int](./component%28_,from%29.md)
  Returns the value for one component of a date.
- [func dateComponents(Set<Calendar.Component>, from: Date) -> DateComponents](./datecomponents%28_,from%29.md)
  Returns all the date components of a date, using the calendar time zone.
- [func dateComponents(Set<Calendar.Component>, from: Date, to: Date) -> DateComponents](./datecomponents%28_,from,to%29-2kcg.md)
  Returns the difference between two dates.
- [func dateComponents(Set<Calendar.Component>, from: DateComponents, to: DateComponents) -> DateComponents](./datecomponents%28_,from,to%29-5g20t.md)
  Returns the difference between two dates specified as `DateComponents`.
- [func dateComponents(in: TimeZone, from: Date) -> DateComponents](./datecomponents%28in,from%29.md)
  Returns all the date components of a date, as if in a given time zone (instead of the `Calendar` time zone).
- [Calendar.Component](./component.md)
  An enumeration for the various components of a calendar date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/date(_:matchescomponents:))*