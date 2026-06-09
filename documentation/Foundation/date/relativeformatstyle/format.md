# format(_:)

**Framework**: Foundation  
**Kind**: method

Creates a locale-aware string representation from a relative date value.

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
func format(_ destDate: Date) -> String
```

#### Return Value

A string representation of the relative date.

#### Discussion

The [`format(_:)`](date/relativeformatstyle/format(_:).md) instance method generates a string from the provided relative date. Once you create a style, you can use it to format dates multiple times.

The following example applies a format style repeatedly to produce string representations of relative dates:

```swift
if let pastWeek = Calendar.current.date(byAdding: .day, value: -7, to: Date()) {
    if let pastDay = Calendar.current.date(byAdding: .day, value: -1, to: Date()) {

        let formatStyle = Date.RelativeFormatStyle(
            presentation: .named,
            unitsStyle: .spellOut,
            locale: Locale(identifier: "en_GB"),
            calendar: Calendar.current,
            capitalizationContext: .beginningOfSentence)
        
        formatStyle.format(pastDay) // "Yesterday"
        formatStyle.format(pastWeek) // "Last week"
    }
}
```

## Parameters

- `destDate`: The date to format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/relativeformatstyle/format(_:))*