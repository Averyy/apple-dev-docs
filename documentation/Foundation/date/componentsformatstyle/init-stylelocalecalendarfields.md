# init(style:locale:calendar:fields:)

**Framework**: Foundation  
**Kind**: init

Shows the date interval with the specified style and the specified date and time fields.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init(style: Date.ComponentsFormatStyle.Style, locale: Locale = .autoupdatingCurrent, calendar: Calendar = .autoupdatingCurrent, fields: Set<Date.ComponentsFormatStyle.Field>? = nil)
```

## Parameters

- `style`: The style for the field names.
- `locale`: The locale for formatting the date interval. May affect the language in which the formatted fields are displayed and how the individual fields are connected.
- `calendar`: The calendar to interpret date values.
- `fields`: The fields to be included in the output string. Chosen automatically based on the interval being formatted if unspecified. Fields with 0 value are dropped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/componentsformatstyle/init(style:locale:calendar:fields:))*