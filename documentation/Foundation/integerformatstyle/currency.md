# IntegerFormatStyle.Currency

**Framework**: Foundation  
**Kind**: struct

A format style that converts between integer currency values and their textual representations.

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

### Creating an integer currency format style
- [init(code: String, locale: Locale)](integerformatstyle/currency/init(code:locale:).md)
  Creates an integer currency format style that uses the given currency code and locale.
### Customizing style behavior
- [func decimalSeparator(strategy: IntegerFormatStyle<Value>.Currency.Configuration.DecimalSeparatorDisplayStrategy) -> IntegerFormatStyle<Value>.Currency](integerformatstyle/currency/decimalseparator(strategy:).md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(IntegerFormatStyle<Value>.Currency.Configuration.Grouping) -> IntegerFormatStyle<Value>.Currency](integerformatstyle/currency/grouping(_:).md)
  Modifies the format style to use the specified grouping.
- [func precision(IntegerFormatStyle<Value>.Currency.Configuration.Precision) -> IntegerFormatStyle<Value>.Currency](integerformatstyle/currency/precision(_:).md)
  Modifies the format style to use the specified precision.
- [func presentation(IntegerFormatStyle<Value>.Currency.Configuration.Presentation) -> IntegerFormatStyle<Value>.Currency](integerformatstyle/currency/presentation(_:).md)
  Modifies the format style to use the specified presentation.
- [func rounded(rule: IntegerFormatStyle<Value>.Currency.Configuration.RoundingRule, increment: Int?) -> IntegerFormatStyle<Value>.Currency](integerformatstyle/currency/rounded(rule:increment:).md)
  Modifies the format style to use the specified rounding rule and increment.
- [func scale(Double) -> IntegerFormatStyle<Value>.Currency](integerformatstyle/currency/scale(_:).md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: IntegerFormatStyle<Value>.Currency.Configuration.SignDisplayStrategy) -> IntegerFormatStyle<Value>.Currency](integerformatstyle/currency/sign(strategy:).md)
  Modifies the format style to use the specified sign display strategy.
- [IntegerFormatStyle.Currency.Configuration](integerformatstyle/currency/configuration.md)
  The type the format style uses for configuration settings.
- [enum CurrencyFormatStyleConfiguration](currencyformatstyleconfiguration.md)
  Configuration settings for formatting currency values.
### Formatting integer currency values
- [func format(Value) -> String](integerformatstyle/currency/format(_:).md)
  Formats an integer, using this style.
### Creating attributed strings
- [var attributed: IntegerFormatStyle<Value>.Attributed](integerformatstyle/currency/attributed.md)
  An attributed format style based on the integer currency format style.
- [IntegerFormatStyle.Attributed](integerformatstyle/attributed-swift.struct.md)
  A format style that converts integers into attributed strings.
### Accessing style properties
- [let currencyCode: String](integerformatstyle/currency/currencycode.md)
  The currency code this format style uses.
- [var locale: Locale](integerformatstyle/currency/locale.md)
  The locale of the format style.
### Applying measurement styles
- [Measurement.FormatStyle](measurement/formatstyle.md)
  A type that provides localized representations of measurements.
### Instance Methods
- [func notation(IntegerFormatStyle<Value>.Currency.Configuration.Notation) -> IntegerFormatStyle<Value>.Currency](integerformatstyle/currency/notation(_:).md)
### Default Implementations
- [FormatStyle Implementations](integerformatstyle/currency/formatstyle-implementations.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/integerformatstyle/currency)*