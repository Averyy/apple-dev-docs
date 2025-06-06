# attributed

**Framework**: Foundation  
**Kind**: property

An attributed format style based on the floating-point format style.

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
var attributed: FloatingPointFormatStyle<Value>.Attributed { get }
```

#### Discussion

Use this modifier to create a [`FloatingPointFormatStyle.Attributed`](floatingpointformatstyle/attributed-swift.struct.md) instance, which formats values as [`AttributedString`](attributedstring.md) instances. These attributed strings contain attributes from the [`AttributeScopes.FoundationAttributes.NumberFormatAttributes`](attributescopes/foundationattributes/numberformatattributes.md) attribute scope. Use these attributes to determine which runs of the attributed string represent different parts of the formatted value.

The following example finds runs of the attributed string that represent different parts of a formatted currency, and adds additional attributes like [`foregroundColor`](attributescopes/swiftuiattributes/foregroundcolor.md) and [`inlinePresentationIntent`](attributescopes/foundationattributes/inlinepresentationintent.md).

```swift
func attributedPrice(price: Double) -> AttributedString {
    var attributedPrice = price.formatted(
        .currency(code: "USD")
        .attributed)

    for run in attributedPrice.runs {
        if run.attributes.numberSymbol == .currency ||
            run.attributes.numberSymbol == .decimalSeparator {
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

![The currency value $1,234.56, with the dollar sign and decimal separator in red, and the digits in bold.](https://docs-assets.developer.apple.com/published/7a4b9269c09c3f9fcab491116254bbc9/media-4098627%402x.png)

## See Also

- [FloatingPointFormatStyle.Attributed](floatingpointformatstyle/attributed-swift.struct.md)
  A format style that converts integers into attributed strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/floatingpointformatstyle/attributed-swift.property)*