# FloatingPointFormatStyle

**Framework**: Foundation  
**Kind**: struct

A structure that converts between floating-point values and their textual representations.

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
struct FloatingPointFormatStyle<Value> where Value : BinaryFloatingPoint
```

#### Overview

Instances of [`FloatingPointFormatStyle`](floatingpointformatstyle.md) create localized, human-readable text from [`BinaryFloatingPoint`](https://developer.apple.com/documentation/Swift/BinaryFloatingPoint) numbers and parse string representations of numbers into instances of [`BinaryFloatingPoint`](https://developer.apple.com/documentation/Swift/BinaryFloatingPoint) types. All of the Swift standard library’s floating-point types, such as [`Double`](https://developer.apple.com/documentation/Swift/Double), [`Float`](https://developer.apple.com/documentation/Swift/Float), and [`Float80`](https://developer.apple.com/documentation/Swift/Float80), conform to [`BinaryFloatingPoint`](https://developer.apple.com/documentation/Swift/BinaryFloatingPoint), and therefore work with this format style.

[`FloatingPointFormatStyle`](floatingpointformatstyle.md) includes two nested types, [`FloatingPointFormatStyle.Percent`](floatingpointformatstyle/percent.md) and [`FloatingPointFormatStyle.Currency`](floatingpointformatstyle/currency.md), for working with percentages and currencies, respectively. Each format style includes a configuration that determines how it represents numeric values, for things like grouping, displaying signs, and variant presentations like scientific notation. [`FloatingPointFormatStyle`](floatingpointformatstyle.md) and [`FloatingPointFormatStyle.Percent`](floatingpointformatstyle/percent.md) include a [`NumberFormatStyleConfiguration`](numberformatstyleconfiguration.md), and [`FloatingPointFormatStyle.Currency`](floatingpointformatstyle/currency.md) includes a [`CurrencyFormatStyleConfiguration`](currencyformatstyleconfiguration.md). You can customize numeric formatting for a style by adjusting its backing configuration. The system automatically caches unique configurations of a format style to enhance performance.

> **Note**:  Foundation provides another format style type, [`IntegerFormatStyle`](integerformatstyle.md), for working with numbers that conform to [`BinaryInteger`](https://developer.apple.com/documentation/Swift/BinaryInteger). For Foundation’s [`Decimal`](decimal.md) type, use [`Decimal.FormatStyle`](decimal/formatstyle.md).

##### Formatting Floating Point Values

Use the [`formatted()`](https://developer.apple.com/documentation/Swift/BinaryFloatingPoint/formatted()) method to create a string representation of a floating-point value using the default [`FloatingPointFormatStyle`](floatingpointformatstyle.md) configuration.

```swift
let formattedDefault = 12345.67.formatted()
// formattedDefault is "12,345.67" in the en_US locale.
// Other locales may use different separator and grouping behavior.
```

You can specify a format style by providing an argument to the [`formatted(_:)`](https://developer.apple.com/documentation/Swift/BinaryFloatingPoint/formatted(_:)-4ksqj) method. The following example shows the number `0.1` represented in each of the available styles, in the `en_US` locale:

```swift
let number = 0.1

let formattedNumber = number.formatted(.number)
// formattedNumber is "0.1".

let formattedPercent = number.formatted(.percent)
// formattedPercent is "10%".

let formattedCurrency = number.formatted(.currency(code: "USD"))
// formattedCurrency is "$0.10".
```

Each style provides methods for updating its numeric configuration, including the number of significant digits, grouping length, and more. You can specify a numeric configuration by calling as many of these methods as you need in any order you choose. The following example shows the same number with default and custom configurations:

```swift
let exampleNumber = 123456.78

let defaultFormatting = exampleNumber.formatted(.number)
// defaultFormatting is "123 456,78" for the "fr_FR" locale.
// defaultFormatting is "123,456.78" for the "en_US" locale.

let customFormatting = exampleNumber.formatted(
    .number
        .grouping(.never)
        .sign(strategy: .always()))
// customFormatting is "+123456.78"
```

##### Creating a Floating Point Format Style Instance

The previous examples use static factory methods like [`number`](formatstyle/number-8c8rj.md) to create format styles within the call to the [`formatted(_:)`](https://developer.apple.com/documentation/Swift/BinaryFloatingPoint/formatted(_:)-4ksqj) method. You can also create a [`FloatingPointFormatStyle`](floatingpointformatstyle.md) instance and use it to repeatedly format different values, with the `format(_:)` method:

```swift
let percentFormatStyle = FloatingPointFormatStyle<Double>.Percent()

percentFormatStyle.format(0.5) // "50%"
percentFormatStyle.format(0.855) // "85.5%"
percentFormatStyle.format(1.0) // "100%"

```

##### Parsing Floating Point Values

You can use [`FloatingPointFormatStyle`](floatingpointformatstyle.md) to parse strings into floating-point values. You can define the format style within the type’s initializer or pass in a format style created outside the function, as shown here:

```swift
let price = try? Double("$3,500.63",
                         format: .currency(code: "USD")) // 3500.63

let priceFormatStyle = FloatingPointFormatStyle<Double>.Currency(code: "USD")
let salePrice = try? Double("$731.67",
                             format: priceFormatStyle) // 731.67
```

##### Matching Regular Expressions

Along with parsing numeric values in strings, you can use theSwift regular expression domain-specific language to match and capture numeric substrings. The following example defines a percentage format style to match a percentage value using `en_US` numeric conventions. The rest of the regular expression ignores any characters prior to a `": "` sequence that precedes the percentage substring.

```swift
import RegexBuilder
let source = "Percentage complete: 55.1%"
let matcher = Regex {
    OneOrMore(.any)
    ": "
    Capture {
        One(.localizedDoublePercentage(locale: Locale(identifier: "en_US")))
    }
}
let match = source.firstMatch(of: matcher)
let localizedPercentage = match?.1
print("\(localizedPercentage!)") // 0.551
```

## Topics

### Creating a floating-point format style
- [init(locale: Locale)](floatingpointformatstyle/init(locale:).md)
  Creates a floating-point format style that uses the given locale.
### Customizing style behavior
- [func decimalSeparator(strategy: FloatingPointFormatStyle<Value>.Configuration.DecimalSeparatorDisplayStrategy) -> FloatingPointFormatStyle<Value>](floatingpointformatstyle/decimalseparator(strategy:).md)
  Modifies the format style to use the specified decimal separator display strategy.
- [func grouping(FloatingPointFormatStyle<Value>.Configuration.Grouping) -> FloatingPointFormatStyle<Value>](floatingpointformatstyle/grouping(_:).md)
  Modifies the format style to use the specified grouping.
- [func notation(FloatingPointFormatStyle<Value>.Configuration.Notation) -> FloatingPointFormatStyle<Value>](floatingpointformatstyle/notation(_:).md)
  Modifies the format style to use the specified notation.
- [func precision(FloatingPointFormatStyle<Value>.Configuration.Precision) -> FloatingPointFormatStyle<Value>](floatingpointformatstyle/precision(_:).md)
  Modifies the format style to use the specified precision.
- [func rounded(rule: FloatingPointFormatStyle<Value>.Configuration.RoundingRule, increment: Double?) -> FloatingPointFormatStyle<Value>](floatingpointformatstyle/rounded(rule:increment:).md)
  Modifies the format style to use the specified rounding rule and increment.
- [func scale(Double) -> FloatingPointFormatStyle<Value>](floatingpointformatstyle/scale(_:).md)
  Modifies the format style to use the specified scale.
- [func sign(strategy: FloatingPointFormatStyle<Value>.Configuration.SignDisplayStrategy) -> FloatingPointFormatStyle<Value>](floatingpointformatstyle/sign(strategy:).md)
  Modifies the format style to use the specified sign display strategy for displaying or omitting sign symbols.
- [FloatingPointFormatStyle.Configuration](floatingpointformatstyle/configuration.md)
  The type the format style uses for configuration settings.
- [enum NumberFormatStyleConfiguration](numberformatstyleconfiguration.md)
  Configuration settings for formatting numbers of different types.
### Accessing style locale
- [var locale: Locale](floatingpointformatstyle/locale.md)
  The locale of the format style.
### Applying currency styles
- [FloatingPointFormatStyle.Currency](floatingpointformatstyle/currency.md)
  A format style that converts between floating-point currency values and their textual representations.
### Applying measurement styles
- [Measurement.FormatStyle](measurement/formatstyle.md)
  A type that provides localized representations of measurements.
### Applying list styles
- [struct ListFormatStyle](listformatstyle.md)
  A type that formats lists of items with a separator and conjunction appropriate for a given locale.
### Creating attributed strings
- [var attributed: FloatingPointFormatStyle<Value>.Attributed](floatingpointformatstyle/attributed-swift.property.md)
  An attributed format style based on the floating-point format style.
- [FloatingPointFormatStyle.Attributed](floatingpointformatstyle/attributed-swift.struct.md)
  A format style that converts integers into attributed strings.
### Parsing floating-point numbers
- [struct FloatingPointParseStrategy](floatingpointparsestrategy.md)
  A parse strategy for creating floating-point values from formatted strings.
### Supporting types
- [FloatingPointFormatStyle.Currency](floatingpointformatstyle/currency.md)
  A format style that converts between floating-point currency values and their textual representations.
- [FloatingPointFormatStyle.Percent](floatingpointformatstyle/percent.md)
  A format style that converts between floating-point percentage values and their textual representations.

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
- [struct IntegerFormatStyle](integerformatstyle.md)
  A structure that converts between integer values and their textual representations.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/floatingpointformatstyle)*