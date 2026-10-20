# dateStyle

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The style to use when formatting day, month, and year information.

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
var dateStyle: DateIntervalFormatter.Style { get set }
```

```objc
@property NSDateIntervalFormatterStyle dateStyle;
```

#### Discussion

Set this property to an appropriate value before generating string values. The default value of this property is [`DateIntervalFormatter.Style.none`](./style/none.md).

## See Also

### Configuring the Formatter Options
- [var timeStyle: DateIntervalFormatter.Style](./timestyle.md)
  The style to use when formatting hour, minute, and second information.
- [var dateTemplate: String!](./datetemplate.md)
  The template for formatting one date and time value.
- [var calendar: Calendar!](./calendar.md)
  The calendar to use for date values.
- [var locale: Locale!](./locale.md)
  The locale to use when formatting date and time values.
- [var timeZone: TimeZone!](./timezone.md)
  The time zone with which to specify time values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateintervalformatter/datestyle)*