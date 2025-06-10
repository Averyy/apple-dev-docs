# IntegerFormatStyle

**Framework**: Foundation  
**Kind**: struct

A structure that converts between integer values and their textual representations.

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
struct IntegerFormatStyle<Value> where Value : BinaryInteger
```

#### Overview

Instances of [`IntegerFormatStyle`](integerformatstyle.md) create localized, human-readable text from [`BinaryInteger`](https://developer.apple.com/documentation/Swift/BinaryInteger) numbers and parse string representations of numbers into instances of [`BinaryInteger`](https://developer.apple.com/documentation/Swift/BinaryInteger) types. All of the Swift standard library’s integer types, such as [`Int`](https://developer.apple.com/documentation/Swift/Int) and [`UInt32`](https://developer.apple.com/documentation/Swift/UInt32), conform to [`BinaryInteger`](https://developer.apple.com/documentation/Swift/BinaryInteger), and therefore work with this format style.

[`IntegerFormatStyle`](integerformatstyle.md) includes two nested types, [`IntegerFormatStyle.Percent`](integerformatstyle/percent.md) and [`IntegerFormatStyle.Currency`](integerformatstyle/currency.md), for working with percentages and currencies. Each format style includes a configuration that determines how it represents numeric values, for things like grouping, displaying signs, and variant presentations like scientific notation. [`IntegerFormatStyle`](integerformatstyle.md) and [`IntegerFormatStyle.Percent`](integerformatstyle/percent.md) include a [`NumberFormatStyleConfiguration`](numberformatstyleconfiguration.md), and [`IntegerFormatStyle.Currency`](integerformatstyle/currency.md) includes a [`CurrencyFormatStyleConfiguration`](currencyformatstyleconfiguration.md). You can customize numeric formatting for a style by adjusting its backing configuration. The system automatically caches unique configurations of a format style to enhance performance.

> **Note**:  Foundation provides another format style type, [`FloatingPointFormatStyle`](floatingpointformatstyle.md), for working with numbers that conform to [`BinaryFloatingPoint`](https://developer.apple.com/documentation/Swift/BinaryFloatingPoint). For Foundation’s [`Decimal`](decimal.md) type, use [`Decimal.FormatStyle`](decimal/formatstyle.md).

##### Formatting Integers

Use the [`formatted()`](https://developer.apple.com/documentation/Swift/BinaryInteger/formatted()) method to create a string representation of an integer using the default [`IntegerFormatStyle`](integerformatstyle.md) configuration.

```swift
let formattedDefault = 123456.formatted()
// formattedDefault is "123,456" in en_US locale.
// Other locales may use different separator and grouping behavior.
```

You can specify a format style by providing an argument to the [`formatted(_:)`](https://developer.apple.com/documentation/Swift/BinaryInteger/formatted(_:)-73k3e) method. The following example shows the number `12345` represented in each of the available styles, in the `en_US` locale:

```swift
let number = 123456

let formattedNumber = number.formatted(.number)
// formattedNumber is "123,456".

let formattedPercent = number.formatted(.percent)
// formattedPercent is "123,456%".

let formattedCurrency = number.formatted(.currency(code: "USD"))
// formattedCurrency is "$123,456.00".
```

Each style provides methods for updating its numeric configuration, including the number of significant digits, grouping length, and more. You can specify a numeric configuration by calling as many of these methods as you need in any order you choose. The following example shows the same number with default and custom configurations:

```swift
let exampleNumber = 123456

let defaultFormatting = exampleNumber.formatted(.number)
// defaultFormatting is "125 000" for the "fr_FR" locale
// defaultFormatting is "125000" for the "jp_JP" locale
// defaultFormatting is "125,000" for the "en_US" locale

let customFormatting = exampleNumber.formatted(
    .number
    .grouping(.never)
    .sign(strategy: .always()))
// customFormatting is "+123456"
```

##### Creating an Integer Format Style Instance

The previous examples use static factory methods like [`number`](formatstyle/number-7fxvo.md) to create format styles within the call to the [`formatted(_:)`](https://developer.apple.com/documentation/Swift/BinaryInteger/formatted(_:)-73k3e) method. You can also create an [`IntegerFormatStyle`](integerformatstyle.md) instance and use it to repeatedly format different values with the [`format(_:)`](integerformatstyle/format(_:).md) method:

```swift
let percentFormatStyle = IntegerFormatStyle<Int>.Percent()

percentFormatStyle.format(50) // "50%"
percentFormatStyle.format(85) // "85%"
percentFormatStyle.format(100) // "100%"
```

##### Parsing Integers

You can use [`IntegerFormatStyle`](integerformatstyle.md) to parse strings into integer values. You can define the format style within the type’s initializer or pass in a format style you create prior to calling the method, as shown here:

```swift
let price = try? Int("$123,456",
                     format: .currency(code: "USD")) // 123456

let priceFormatStyle = IntegerFormatStyle<Int>.Currency(code: "USD")
let salePrice = try? Int("$120,000",
                          format: priceFormatStyle) // 120000
```

##### Matching Regular Expressions

Along with parsing numeric values in strings, you can use the Swift regular expression domain-specific language to match and capture numeric substrings. The following example defines a currency format style to match and capture a currency value using US dollars and `en_US` numeric conventions. The rest of the regular expression ignores any characters prior to a `": "` sequence that precedes the currency substring.

```swift
import RegexBuilder

let source = "Payment due: $123,456"
let matcher = Regex {
    OneOrMore(.any)
    ": "
    Capture {
        One(.localizedIntegerCurrency(code: Locale.Currency("USD"),
                                      locale: Locale(identifier: "en_US")))
    }
}
let match = source.firstMatch(of: matcher)
let localizedInteger = match?.1 // 123456
```

## Topics

### Creating an integer format style
- [init(locale: Locale)](integerformatstyle/init(locale:).md)
  Creates an integer format style that uses the given locale.
### Formatting integer values
- [func format(Value) -> String](integerformatstyle/format(_:).md)
  Formats an integer, using this style.
### Customizing style behavior
- [func decimalSeparator(strategy: IntegerFormatStyle<Value>.Configuration.DecimalSeparatorDisplayStrategy) -> IntegerFormatStyle<Value>](integerformatstyle/decimalseparator(strategy:).md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(IntegerFormatStyle<Value>.Configuration.Grouping) -> IntegerFormatStyle<Value>](integerformatstyle/grouping(_:).md)
  Modifies the format style to use the specified grouping.
- [func notation(IntegerFormatStyle<Value>.Configuration.Notation) -> IntegerFormatStyle<Value>](integerformatstyle/notation(_:).md)
  Modifies the format style to use the specified notation.
- [func precision(IntegerFormatStyle<Value>.Configuration.Precision) -> IntegerFormatStyle<Value>](integerformatstyle/precision(_:).md)
  Modifies the format style to use the specified precision.
- [func rounded(rule: IntegerFormatStyle<Value>.Configuration.RoundingRule, increment: Int?) -> IntegerFormatStyle<Value>](integerformatstyle/rounded(rule:increment:).md)
  Modifies the format style to use the specified rounding rule and increment.
- [func scale(Double) -> IntegerFormatStyle<Value>](integerformatstyle/scale(_:).md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: IntegerFormatStyle<Value>.Configuration.SignDisplayStrategy) -> IntegerFormatStyle<Value>](integerformatstyle/sign(strategy:).md)
  Modifies the format style to use the specified sign display strategy for displaying or omitting sign symbols.
- [IntegerFormatStyle.Configuration](integerformatstyle/configuration.md)
  The type the format style uses for configuration settings.
- [enum NumberFormatStyleConfiguration](numberformatstyleconfiguration.md)
  Configuration settings for formatting numbers of different types.
### Acessing style locale
- [var locale: Locale](integerformatstyle/locale.md)
  The locale of the format style.
### Applying currency styles
- [IntegerFormatStyle.Currency](integerformatstyle/currency.md)
  A format style that converts between integer currency values and their textual representations.
### Applying measurement styles
- [Measurement.FormatStyle](measurement/formatstyle.md)
  A type that provides localized representations of measurements.
### Applying list styles
- [struct ListFormatStyle](listformatstyle.md)
  A type that formats lists of items with a separator and conjunction appropriate for a given locale.
### Creating attributed strings
- [var attributed: IntegerFormatStyle<Value>.Attributed](integerformatstyle/attributed-swift.property.md)
  An attributed format style based on the integer format style.
- [IntegerFormatStyle.Attributed](integerformatstyle/attributed-swift.struct.md)
  A format style that converts integers into attributed strings.
### Parsing integers
- [struct IntegerParseStrategy](integerparsestrategy.md)
  A parse strategy for creating integer values from formatted strings.
### Supporting types
- [IntegerFormatStyle.Currency](integerformatstyle/currency.md)
  A format style that converts between integer currency values and their textual representations.
- [IntegerFormatStyle.Percent](integerformatstyle/percent.md)
  A format style that converts between integer percentage values and their textual representations.
### Default Implementations
- [FormatStyle Implementations](integerformatstyle/formatstyle-implementations.md)

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
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Language Introspector](language-introspector.md)
  Converts data into human-readable text using formatters and locales.
- [protocol FormatStyle](formatstyle.md)
  A type that converts a given data type into a representation in another type, such as a string.
- [struct FloatingPointFormatStyle](floatingpointformatstyle.md)
  A structure that converts between floating-point values and their textual representations.
- [Decimal.FormatStyle](decimal/formatstyle.md)
  A structure that converts between decimal values and their textual representations.
- [struct ListFormatStyle](listformatstyle.md)
  A type that formats lists of items with a separator and conjunction appropriate for a given locale.
- [struct StringStyle](stringstyle.md)
- [struct FormatStyle](url/formatstyle.md)
  A structure that converts between URL instances and their textual representations.
- [struct FormatStyleCapitalizationContext](formatstylecapitalizationcontext.md)
  The capitalization formatting context used when formatting dates and times.
- [Format Style Configurations](format-style-configurations.md)
  Behaviors for traits like numeric precision, rounding, and scale, used for formatting and parsing numeric values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/integerformatstyle)*