# Date.AttributedStyle

**Framework**: Foundation  
**Kind**: struct

A structure that creates a locale-appropriate attributed string representation of a date instance.

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
struct AttributedStyle
```

#### Overview

Use a [`Date.FormatStyle`](date/formatstyle.md) instance to customize the lexical representation of a date as a string. Use the format style’s [`attributed`](date/formatstyle/attributed-swift.property.md) property to customize the visual representation of the date as a string. Attributed strings can represent the subcomponent characters, words, and phrases of a string with a custom combination of font size, weight, and color.

For example, the function below uses a date format style to create a custom lexical representation of a date, then retrieves an attributed string representation of the same date and applies a visual emphasis to the year component of the date.

```swift
// Applies visual emphasis to the year component of a formatted attributed date string.
private func makeAttributedString() -> AttributedString {
    let date = Date()
    let formatStyle = Date.FormatStyle(date: .abbreviated, time: .standard)
    var attributedString = formatStyle.attributed.format(date)
    for run in attributedString.runs {
        if let dateFieldAttribute = run.attributes.foundation.dateField,
           dateFieldAttribute == .year {
            // When you find a year, change its attributes.
            attributedString[run.range].inlinePresentationIntent = [.emphasized, .stronglyEmphasized]
        }
    }
    return attributedString
}
```

The expression `formatStyle.attributed.format(date)` above creates an attributed string representation of the date. This assigns instances of the [`AttributeScopes.FoundationAttributes.DateFieldAttribute`](attributescopes/foundationattributes/datefieldattribute.md) to indicate ranges of the string that represent different date fields. The example then loops over the [`runs`](attributedstringprotocol/runs.md) of the attributed string to find any run with the [`AttributeScopes.FoundationAttributes.DateFieldAttribute.Field.year`](attributescopes/foundationattributes/datefieldattribute/field/year.md) attribute. When it finds one, it adds the [`inlinePresentationIntent`](attributescopes/foundationattributes/inlinepresentationintent.md) attributes [`emphasized`](inlinepresentationintent/emphasized.md) and [`stronglyEmphasized`](inlinepresentationintent/stronglyemphasized.md).

The runs of the resulting attributed string have the following attributes:

| Run text | Attributes |
| --- | --- |
| `Mar` | [`AttributeScopes.FoundationAttributes.DateFieldAttribute.Field.month`](attributescopes/foundationattributes/datefieldattribute/field/month.md) |
| `15` | [`AttributeScopes.FoundationAttributes.DateFieldAttribute.Field.day`](attributescopes/foundationattributes/datefieldattribute/field/day.md) |
| `2022` | [`AttributeScopes.FoundationAttributes.DateFieldAttribute.Field.year`](attributescopes/foundationattributes/datefieldattribute/field/year.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`emphasized`](inlinepresentationintent/emphasized.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`stronglyEmphasized`](inlinepresentationintent/stronglyemphasized.md) |
| `10` | [`AttributeScopes.FoundationAttributes.DateFieldAttribute.Field.hour`](attributescopes/foundationattributes/datefieldattribute/field/hour.md) |
| `06` | [`AttributeScopes.FoundationAttributes.DateFieldAttribute.Field.minute`](attributescopes/foundationattributes/datefieldattribute/field/minute.md) |
| `46` | [`AttributeScopes.FoundationAttributes.DateFieldAttribute.Field.second`](attributescopes/foundationattributes/datefieldattribute/field/second.md) |
| `AM` | [`AttributeScopes.FoundationAttributes.DateFieldAttribute.Field.amPM`](attributescopes/foundationattributes/datefieldattribute/field/ampm.md) |

If you create a SwiftUI [`Text`](https://developer.apple.com/documentation/SwiftUI/Text) view with this attributed string, SwiftUI renders the combination of [`emphasized`](inlinepresentationintent/emphasized.md) and [`stronglyEmphasized`](inlinepresentationintent/stronglyemphasized.md) attributes as bold, italicized text, as seen in the following screenshot.

![A macOS window with a text view showing the current date and time. The year is displayed in bold, italicized text.](https://docs-assets.developer.apple.com/published/28831814e748f64678cda91ac0f2f449/media-3957719%402x.png)

## Topics

### Applying Date Attributed Styles
- [func format(Date) -> AttributedString](date/attributedstyle/format(_:).md)
  Creates a locale-aware attributed string representation from a date value.
### Comparing Date Attributed Styles
- [static func != (Self, Self) -> Bool](date/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func == (Date, Date) -> Bool](date/==(_:_:).md)
  Returns true if the two `Date` values represent the same point in time.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [FormatStyle](formatstyle.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var attributed: Date.AttributedStyle](date/formatstyle/attributed-swift.property.md)
  An attributed format style created from the date format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/attributedstyle)*