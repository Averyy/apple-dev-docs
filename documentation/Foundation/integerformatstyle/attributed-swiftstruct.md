# IntegerFormatStyle.Attributed

**Framework**: Foundation  
**Kind**: struct

A format style that converts integers into attributed strings.

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
struct Attributed
```

#### Overview

Use the [`attributed`](integerformatstyle/attributed-swift.property.md) modifier on an [`IntegerFormatStyle`](integerformatstyle.md) to create a format style of this type.

The attributed strings that this format style creates contain attributes from the [`AttributeScopes.FoundationAttributes.NumberFormatAttributes`](attributescopes/foundationattributes/numberformatattributes.md) attribute scope. Use these attributes to determine which runs of the attributed string represent different parts of the formatted value.

The following example finds runs of the attributed string that represent different parts of a formatted currency, and adds additional attributes like [`foregroundColor`](attributescopes/swiftuiattributes/foregroundcolor.md) and [`inlinePresentationIntent`](attributescopes/foundationattributes/inlinepresentationintent.md).

```swift
func attributedPrice(price: Decimal) -> AttributedString {
    var attributedPrice = price.formatted(
        .currency(code: "USD")
        .attributed)

    for run in attributedPrice.runs {
        if run.attributes.numberSymbol == .currency ||
            run.attributes.numberSymbol == .decimalSeparator  {
            attributedPrice[run.range].foregroundColor = .red
        }
        if run.attributes.numberPart == .integer ||
            run.attributes.numberPart == .fraction {
            attributedPrice[run.range].inlinePresentationIntent = [.stronglyEmphasized]
        }
    }
    return attributedPrice
}

```

User interface frameworks like SwiftUI can use these attributes when presenting the attributed string, as seen here:

![The currency value $1,234.56, with the dollar sign and decimal separator in red, and the digits in bold.](https://docs-assets.developer.apple.com/published/7a4b9269c09c3f9fcab491116254bbc9/media-4097935%402x.png)

## Topics

### Formatting an integer
- [func format(Value) -> AttributedString](integerformatstyle/attributed-swift.struct/format(_:).md)
  Formats an integer, using this style.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [FormatStyle](formatstyle.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var attributed: IntegerFormatStyle<Value>.Attributed](integerformatstyle/attributed-swift.property.md)
  An attributed format style based on the integer format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/integerformatstyle/attributed-swift.struct)*