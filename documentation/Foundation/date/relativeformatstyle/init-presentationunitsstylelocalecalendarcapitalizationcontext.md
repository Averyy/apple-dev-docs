# init(presentation:unitsStyle:locale:calendar:capitalizationContext:)

**Framework**: Foundation  
**Kind**: init

Creates a relative date format style with the specified presentation, units, locale, calendar, and capitalization context.

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
init(presentation: Date.RelativeFormatStyle.Presentation = .numeric, unitsStyle: Date.RelativeFormatStyle.UnitsStyle = .wide, locale: Locale = .autoupdatingCurrent, calendar: Calendar = .autoupdatingCurrent, capitalizationContext: FormatStyleCapitalizationContext = .unknown)
```

#### Discussion

The following example creates a format style applied to a relative date to create a string representation.

```swift
if let past = Calendar.current.date(byAdding: .day, value: -7, to: Date()) {

    let formatStyle = Date.RelativeFormatStyle(
        presentation: .named,
        unitsStyle: .abbreviated,
        locale: Locale(identifier: "en_US"),
        calendar: Calendar.current,
        capitalizationContext: .beginningOfSentence)
    
    print(past.formatted(formatStyle)) // "Last wk."
}
```

## Parameters

- `presentation`: The style to use when describing a relative date, such as “1 day ago” or “yesterday”.
- `unitsStyle`: The style to use when formatting the quantity or the name of the unit, such as “1 day ago” or “one day ago”.
- `locale`: The locale to use when formatting the relative date.
- `calendar`: The calendar to use when formatting the relative date.
- `capitalizationContext`: The capitalization context to use when formatting the relative date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/relativeformatstyle/init(presentation:unitsstyle:locale:calendar:capitalizationcontext:))*