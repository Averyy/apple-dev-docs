# attributed

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

An attributed format style created from the date format style.

**Availability**:
- iOS 15.0+ - Deprecated in 18.0
- iPadOS 15.0+ - Deprecated in 18.0
- Mac Catalyst 15.0+ - Deprecated in 18.0
- macOS 12.0+ - Deprecated in 15.0
- tvOS 15.0+ - Deprecated in 18.0
- visionOS 1.0+
- watchOS 8.0+ - Deprecated in 11.0

> **Deprecated**: Use attributedStyle instead

## Declaration

```swift
var attributed: Date.AttributedStyle { get }
```

#### Discussion

Use a [`Date.FormatStyle`](../formatstyle.md) instance to customize the lexical representation of a date as a string. Use the format style’s [`attributed`](./attributed-swift.property.md) property to customize the visual representation of the date as a string. Attributed strings can represent the subcomponent characters, words, and phrases of a string with a custom combination of font size, weight, and color.

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

The expression `formatStyle.attributed.format(date)` above creates an attributed string representation of the date. This assigns instances of the [`AttributeScopes.FoundationAttributes.DateFieldAttribute`](../../attributescopes/foundationattributes/datefieldattribute.md) to indicate ranges of the string that represent different date fields. The example then loops over the [`runs`](../../attributedstringprotocol/runs.md) of the attributed string to find any run with the [`AttributeScopes.FoundationAttributes.DateFieldAttribute.Field.year`](../../attributescopes/foundationattributes/datefieldattribute/field/year.md) attribute. When it finds one, it adds the [`inlinePresentationIntent`](../../attributescopes/foundationattributes/inlinepresentationintent.md) attributes [`emphasized`](../../inlinepresentationintent/emphasized.md) and [`stronglyEmphasized`](../../inlinepresentationintent/stronglyemphasized.md).

The runs of the resulting attributed string have the following attributes:

| Run Text | Attributes |
| --- | --- |
| Mar | [`AttributeScopes.FoundationAttributes.DateFieldAttribute.Field.month`](../../attributescopes/foundationattributes/datefieldattribute/field/month.md) |
| 15 | [`AttributeScopes.FoundationAttributes.DateFieldAttribute.Field.day`](../../attributescopes/foundationattributes/datefieldattribute/field/day.md) |
| 2022 | [`AttributeScopes.FoundationAttributes.DateFieldAttribute.Field.year`](../../attributescopes/foundationattributes/datefieldattribute/field/year.md) ![](https://developer.apple.com/tutorials/images/com.apple.foundation/spacer.png) [`emphasized`](../../inlinepresentationintent/emphasized.md)  ![](https://developer.apple.com/tutorials/images/com.apple.foundation/spacer.png) [`stronglyEmphasized`](../../inlinepresentationintent/stronglyemphasized.md) |
| 10 | [`AttributeScopes.FoundationAttributes.DateFieldAttribute.Field.hour`](../../attributescopes/foundationattributes/datefieldattribute/field/hour.md) |
| 06 | [`AttributeScopes.FoundationAttributes.DateFieldAttribute.Field.minute`](../../attributescopes/foundationattributes/datefieldattribute/field/minute.md) |
| 46 | [`AttributeScopes.FoundationAttributes.DateFieldAttribute.Field.second`](../../attributescopes/foundationattributes/datefieldattribute/field/second.md) |
| AM | [`AttributeScopes.FoundationAttributes.DateFieldAttribute.Field.amPM`](../../attributescopes/foundationattributes/datefieldattribute/field/ampm.md) |

If you create a SwiftUI [`Text`](../../../SwiftUI/text.md) view with this attributed string, SwiftUI renders the combination of [`emphasized`](../../inlinepresentationintent/emphasized.md) and [`stronglyEmphasized`](../../inlinepresentationintent/stronglyemphasized.md) attributes as bold, italicized text, as seen in the following screenshot.

![A macOS window with a text view showing the current date and time. The year is displayed in bold, italicized text.](https://developer.apple.com/tutorials/images/com.apple.foundation/media-3957718@2x.png)

## See Also

### Applying Visual Attributes to Dates
- [struct AttributedStyle](../attributedstyle.md)
  A structure that creates a locale-appropriate attributed string representation of a date instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/attributed-swift.property)*