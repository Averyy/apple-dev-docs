# maximumRange(of:)

**Framework**: Foundation  
**Kind**: method

The maximum range limits of the values that a given component can take on.

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
func maximumRange(of component: Calendar.Component) -> Range<Int>?
```

#### Return Value

The range, or nil if it could not be calculated.

#### Discussion

As an example, in the Gregorian calendar the maximum range of values for the Day component is 1-31.

## Parameters

- `component`: A component to calculate a range for.

## See Also

- [var identifier: Calendar.Identifier](calendar/identifier-swift.property.md)
  The identifier of the calendar.
- [var locale: Locale?](calendar/locale.md)
  The locale of the calendar.
- [var firstWeekday: Int](calendar/firstweekday.md)
  The first day of the week for the calendar.
- [var minimumDaysInFirstWeek: Int](calendar/minimumdaysinfirstweek.md)
  The number of minimum days in the first week.
- [var timeZone: TimeZone](calendar/timezone.md)
  The time zone of the calendar.
- [func minimumRange(of: Calendar.Component) -> Range<Int>?](calendar/minimumrange(of:).md)
  Returns the minimum range limits of the values that a given component can take on.
- [func ordinality(of: Calendar.Component, in: Calendar.Component, for: Date) -> Int?](calendar/ordinality(of:in:for:).md)
  Returns, for a given absolute time, the ordinal number of a smaller calendar component (such as a day) within a specified larger calendar component (such as a week).
- [func range(of: Calendar.Component, in: Calendar.Component, for: Date) -> Range<Int>?](calendar/range(of:in:for:).md)
  Returns the range of absolute time values that a smaller calendar component (such as a day) can take on in a larger calendar component (such as a month) that includes a specified absolute time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/maximumrange(of:))*