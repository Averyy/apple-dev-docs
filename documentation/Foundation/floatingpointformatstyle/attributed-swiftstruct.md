# FloatingPointFormatStyle.Attributed

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

Use the [`attributed`](integerformatstyle/attributed-swift.property.md) modifier on a [`FloatingPointFormatStyle`](floatingpointformatstyle.md) to create a format style of this type.

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

![The currency value $1,234.56, with the dollar sign and decimal separator in red, and the digits in bold.](/images/com.apple.foundation/media-4098701@2x.png)

## Topics

### Formatting a floating-point value
- [func format(Value) -> AttributedString](floatingpointformatstyle/attributed-swift.struct/format(_:).md)
  Formats a floating-point value, using this style.
### Modifying the locale
- [func locale(Locale) -> FloatingPointFormatStyle<Value>.Attributed](floatingpointformatstyle/attributed-swift.struct/locale(_:).md)
  Modifies the format style to use the specified locale.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [FormatStyle](formatstyle.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var attributed: FloatingPointFormatStyle<Value>.Attributed](floatingpointformatstyle/attributed-swift.property.md)
  An attributed format style based on the floating-point format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/floatingpointformatstyle/attributed-swift.struct)*