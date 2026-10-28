# calendar

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The calendar to use for date values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var calendar: Calendar! { get set }
```

```objc
@property (copy, null_resettable) NSCalendar * calendar;
```

## Discussion

The default value of this property is the calendar associated with the current [`locale`](./locale.md) object. You can change this value to use a different calendar for interpreting dates.

## See Also

### Configuring the Formatter Options
- [var dateStyle: DateIntervalFormatter.Style](./datestyle.md)
  The style to use when formatting day, month, and year information.
- [var timeStyle: DateIntervalFormatter.Style](./timestyle.md)
  The style to use when formatting hour, minute, and second information.
- [var dateTemplate: String!](./datetemplate.md)
  The template for formatting one date and time value.
- [var locale: Locale!](./locale.md)
  The locale to use when formatting date and time values.
- [var timeZone: TimeZone!](./timezone.md)
  The time zone with which to specify time values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateintervalformatter/calendar)*