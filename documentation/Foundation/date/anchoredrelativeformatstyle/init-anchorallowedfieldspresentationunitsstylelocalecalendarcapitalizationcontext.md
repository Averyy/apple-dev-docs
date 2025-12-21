# init(anchor:allowedFields:presentation:unitsStyle:locale:calendar:capitalizationContext:)

**Framework**: Foundation  
**Kind**: init

Create a relative format style that is detached from the system time, and instead formats an anchor date relative to the format input.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
init(anchor: Date, allowedFields: Set<Date.AnchoredRelativeFormatStyle.Field>, presentation: Date.AnchoredRelativeFormatStyle.Presentation = .numeric, unitsStyle: Date.AnchoredRelativeFormatStyle.UnitsStyle = .wide, locale: Locale = .autoupdatingCurrent, calendar: Calendar = .autoupdatingCurrent, capitalizationContext: FormatStyleCapitalizationContext = .unknown)
```

## Parameters

- `anchor`: The date the formatted output is referring to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/anchoredrelativeformatstyle/init(anchor:allowedfields:presentation:unitsstyle:locale:calendar:capitalizationcontext:))*