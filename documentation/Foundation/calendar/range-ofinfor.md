# range(of:in:for:)

**Framework**: Foundation  
**Kind**: method

Returns the range of absolute time values that a smaller calendar component (such as a day) can take on in a larger calendar component (such as a month) that includes a specified absolute time.

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
func range(of smaller: Calendar.Component, in larger: Calendar.Component, for date: Date) -> Range<Int>?
```

#### Return Value

The range of absolute time values smaller can take on in larger at the time specified by date. Returns `nil` if larger is not logically bigger than smaller in the calendar, or the given combination of components does not make sense (or is a computation which is undefined).

#### Discussion

You can use this method to calculate, for example, the range the `day` component can take on in the `month` in which `date` lies.

## Parameters

- `smaller`: The smaller calendar component.
- `larger`: The larger calendar component.
- `date`: The absolute time for which the calculation is performed.

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
- [func maximumRange(of: Calendar.Component) -> Range<Int>?](calendar/maximumrange(of:).md)
  The maximum range limits of the values that a given component can take on.
- [func minimumRange(of: Calendar.Component) -> Range<Int>?](calendar/minimumrange(of:).md)
  Returns the minimum range limits of the values that a given component can take on.
- [func ordinality(of: Calendar.Component, in: Calendar.Component, for: Date) -> Int?](calendar/ordinality(of:in:for:).md)
  Returns, for a given absolute time, the ordinal number of a smaller calendar component (such as a day) within a specified larger calendar component (such as a week).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/range(of:in:for:))*