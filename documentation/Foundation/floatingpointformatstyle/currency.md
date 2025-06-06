# FloatingPointFormatStyle.Currency

**Framework**: Foundation  
**Kind**: struct

A format style that converts between floating-point currency values and their textual representations.

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
struct Currency
```

## Topics

### Creating a floating-point currency style
- [init(code: String, locale: Locale)](floatingpointformatstyle/currency/init(code:locale:).md)
  Creates a floating-point currency format style that uses the given currency code and locale.
### Customizing style behavior
- [func decimalSeparator(strategy: FloatingPointFormatStyle<Value>.Currency.Configuration.DecimalSeparatorDisplayStrategy) -> FloatingPointFormatStyle<Value>.Currency](floatingpointformatstyle/currency/decimalseparator(strategy:).md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(FloatingPointFormatStyle<Value>.Currency.Configuration.Grouping) -> FloatingPointFormatStyle<Value>.Currency](floatingpointformatstyle/currency/grouping(_:).md)
  Modifies the format style to use the specified grouping.
- [func precision(FloatingPointFormatStyle<Value>.Currency.Configuration.Precision) -> FloatingPointFormatStyle<Value>.Currency](floatingpointformatstyle/currency/precision(_:).md)
  Modifies the format style to use the specified precision.
- [func presentation(FloatingPointFormatStyle<Value>.Currency.Configuration.Presentation) -> FloatingPointFormatStyle<Value>.Currency](floatingpointformatstyle/currency/presentation(_:).md)
  Modifies the format style to use the specified presentation.
- [func rounded(rule: FloatingPointFormatStyle<Value>.Currency.Configuration.RoundingRule, increment: Double?) -> FloatingPointFormatStyle<Value>.Currency](floatingpointformatstyle/currency/rounded(rule:increment:).md)
  Modifies the format style to use the specified rounding rule and increment.
- [func scale(Double) -> FloatingPointFormatStyle<Value>.Currency](floatingpointformatstyle/currency/scale(_:).md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: FloatingPointFormatStyle<Value>.Currency.Configuration.SignDisplayStrategy) -> FloatingPointFormatStyle<Value>.Currency](floatingpointformatstyle/currency/sign(strategy:).md)
  Modifies the format style to use the specified sign display strategy.
- [FloatingPointFormatStyle.Currency.Configuration](floatingpointformatstyle/currency/configuration.md)
  The type the format style uses for configuration settings.
- [enum CurrencyFormatStyleConfiguration](currencyformatstyleconfiguration.md)
  Configuration settings for formatting currency values.
### Creating attributed strings
- [var attributed: FloatingPointFormatStyle<Value>.Attributed](floatingpointformatstyle/currency/attributed.md)
  An attributed format style based on the floating-point currency format style.
- [FloatingPointFormatStyle.Attributed](floatingpointformatstyle/attributed-swift.struct.md)
  A format style that converts integers into attributed strings.
### Accessing style properties
- [let currencyCode: String](floatingpointformatstyle/currency/currencycode.md)
  The currency code this format style uses.
- [var locale: Locale](floatingpointformatstyle/currency/locale.md)
  The locale of the format style.
### Applying measurement styles
- [Measurement.FormatStyle](measurement/formatstyle.md)
  A type that provides localized representations of measurements.
### Applying list styles
- [struct ListFormatStyle](listformatstyle.md)
  A type that formats lists of items with a separator and conjunction appropriate for a given locale.
### Instance Methods
- [func notation(FloatingPointFormatStyle<Value>.Currency.Configuration.Notation) -> FloatingPointFormatStyle<Value>.Currency](floatingpointformatstyle/currency/notation(_:).md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomConsumingRegexComponent](../Swift/CustomConsumingRegexComponent.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [FormatStyle](formatstyle.md)
- [Hashable](../Swift/Hashable.md)
- [ParseableFormatStyle](parseableformatstyle.md)
- [RegexComponent](../Swift/RegexComponent.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/floatingpointformatstyle/currency)*