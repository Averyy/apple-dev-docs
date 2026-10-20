# timeZone

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The time zone with which to specify time values.

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
var timeZone: TimeZone! { get set }
```

```objc
@property (copy, null_resettable) NSTimeZone * timeZone;
```

#### Discussion

The default value of this property is the default time zone for the current user, which is accessible from the [`default`](../nstimezone/default.md) method of [`NSTimeZone`](../nstimezone.md). You can change this value to a different time zone to generate strings based on that time zone.

## See Also

### Configuring the Formatter Options
- [var dateStyle: DateIntervalFormatter.Style](./datestyle.md)
  The style to use when formatting day, month, and year information.
- [var timeStyle: DateIntervalFormatter.Style](./timestyle.md)
  The style to use when formatting hour, minute, and second information.
- [var dateTemplate: String!](./datetemplate.md)
  The template for formatting one date and time value.
- [var calendar: Calendar!](./calendar.md)
  The calendar to use for date values.
- [var locale: Locale!](./locale.md)
  The locale to use when formatting date and time values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateintervalformatter/timezone)*