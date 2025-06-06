# FormatStyle

**Framework**: Foundation  
**Kind**: protocol

A type that converts a given data type into a representation in another type, such as a string.

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
protocol FormatStyle<FormatInput, FormatOutput> : Decodable, Encodable, Hashable
```

#### Overview

Types conforming to the [`FormatStyle`](formatstyle.md) protocol take their input type and produce formatted instances of their output type. The formatting process accounts for locale-specific conventions, like grouping and separators for numbers, and presentation of units for measurements. The format styles Foundation provides produce their output as [`String`](https://developer.apple.com/documentation/Swift/String) or [`AttributedString`](attributedstring.md) instances. You can also create custom styles that format their output as any type, like XML or JSON [`Data`](data.md) or an image.

There are two basic approaches to using a [`FormatStyle`](formatstyle.md):

- Create an instance of a type that conforms to [`FormatStyle`](formatstyle.md) and apply it to one or more instances of the input type, by calling the style’s [`format(_:)`](formatstyle/format(_:).md) method. Use this when you want to customize a style once and apply it repeatedly to many instances.
- Pass an instance of a type that conforms to [`FormatStyle`](formatstyle.md) to the data type’s `formatted(_:)` method, which takes the style as a parameter. Use this for one-off formatting scenarios, or when you want to apply different format styles to the same data value. For the simplest cases, most types that support formatting also have a no-argument `formatted()` method that applies a locale-appropriate default format style.

Foundation provides format styles for integers ([`IntegerFormatStyle`](integerformatstyle.md)), floating-point numbers ([`FloatingPointFormatStyle`](floatingpointformatstyle.md)), decimals ([`Decimal.FormatStyle`](decimal/formatstyle.md)), measurements ([`Measurement.FormatStyle`](measurement/formatstyle.md)), arrays ([`ListFormatStyle`](listformatstyle.md)), and more. The “Conforming types” section below shows all the format styles available from Foundation and any system frameworks that implement the [`FormatStyle`](formatstyle.md) protocol. The numeric format styles also provide supporting format styles to format currency and percent values, like [`IntegerFormatStyle.Currency`](integerformatstyle/currency.md) and [`Decimal.FormatStyle.Percent`](decimal/formatstyle/percent.md).

##### Modifying a Format Style

Format styles include modifier methods that return a new format style with an adjusted behavior. The following example creates an [`IntegerFormatStyle`](integerformatstyle.md), then applies modifiers to round values down to the nearest 1,000 and applies formatting appropriate to the `fr_FR` locale:

```swift
let style = IntegerFormatStyle<Int>()
    .rounded(rule: .down, increment: 1000)
    .locale(Locale(identifier: "fr_FR"))
let rounded = 123456789.formatted(style) // "123 456 000"
```

Foundation caches identical instances of a customized format style, so you don’t need to pass format style instances around unrelated parts of your app’s source code.

##### Accessing Static Instances

Types that conform to [`FormatStyle`](formatstyle.md) typically extend the base protocol with type properties or type methods to provide convenience instances. These are available for use in a data type’s `formatted(_:)` method when the format style’s input type matches the data type. For example, the various numeric format styles define `number` properties with generic constraints to match the different numeric types ([`Double`](https://developer.apple.com/documentation/Swift/Double), [`Int`](https://developer.apple.com/documentation/Swift/Int), [`Float16`](https://developer.apple.com/documentation/Swift/Float16), and so on).

To see how this works, consider this example of a default formatter for an [`Int`](https://developer.apple.com/documentation/Swift/Int) value. Because `123456789` is a [`BinaryInteger`](https://developer.apple.com/documentation/Swift/BinaryInteger), its [`formatted(_:)`](https://developer.apple.com/documentation/Swift/BinaryInteger/formatted(_:)-4qd73) method accepts an [`IntegerFormatStyle`](integerformatstyle.md) parameter. The following example shows the style’s default behavior in the `en_US` locale.

```swift
let formatted = 123456789.formatted(IntegerFormatStyle()) // "123,456,789"
```

[`IntegerFormatStyle`](integerformatstyle.md) extends [`FormatStyle`](formatstyle.md) with multiple type properties called `number`, each of which is an [`IntegerFormatStyle`](integerformatstyle.md) instance; these properties differ by which [`BinaryInteger`](https://developer.apple.com/documentation/Swift/BinaryInteger)-conforming type they take as input. Since one of these statically-defined properties ([`number`](formatstyle/number-7fxvo.md)) takes [`Int`](https://developer.apple.com/documentation/Swift/Int) as its input, you can use this type property instead of instantiating a new format style instance. Using dot notation to access this property on the inferred [`FormatStyle`](formatstyle.md) makes the call point much easier to read, as seen here:

```swift
let formatted = 123456789.formatted( .number) // "123,456,789"
```

Furthermore, since you can customize these statically-accessed format style instances, you can rewrite the example from the previous section without instantiating a new [`IntegerFormatStyle`](integerformatstyle.md), like this:

```swift
let rounded = 123456789.formatted( .number
    .rounded(rule: .down, increment: 1000)
    .locale(Locale(identifier: "fr_FR"))) // "123 456 000"
```

##### Parsing with a Format Style

To perform the opposite conversion — from formatted output type to input data type — some format styles provide a corresponding [`ParseStrategy`](parsestrategy.md) type. These format styles typically expose an instance of this type as a variable, called `parseStrategy`.

You can use a [`ParseStrategy`](parsestrategy.md) one of two ways:

- Initialize the data type by calling an initializer of that type that takes a formatted instance and a parse strategy as parameters. For example, you can create a [`Decimal`](decimal.md) from a formatted string with the initializer [`init(_:format:lenient:)`](decimal/init(_:format:lenient:)-6fk71.md).
- Create a parse strategy and call its [`parse(_:)`](parsestrategy/parse(_:).md) method on one or more formatted instances.

## Topics

### Performing formatting
- [func format(Self.FormatInput) -> Self.FormatOutput](formatstyle/format(_:).md)
  Formats a value, using this style.
### Setting style Locale
- [func locale(Locale) -> Self](formatstyle/locale(_:).md)
  Modifies the format style to use the specified locale.
### Applying numeric styles for integers
- [static var number: IntegerFormatStyle<Int>](formatstyle/number-7fxvo.md)
  A style for formatting the Swift default integer type.
- [static var number: IntegerFormatStyle<UInt>](formatstyle/number-4ttgp.md)
  A style for formatting the Swift unsigned integer type.
- [static var number: IntegerFormatStyle<Int8>](formatstyle/number-5hzgj.md)
  A style for formatting 8-bit signed integers.
- [static var number: IntegerFormatStyle<Int16>](formatstyle/number-1o8fx.md)
  A style for formatting 16-bit signed integers.
- [static var number: IntegerFormatStyle<Int32>](formatstyle/number-4cj49.md)
  A style for formatting 32-bit signed integers.
- [static var number: IntegerFormatStyle<Int64>](formatstyle/number-3925i.md)
  A style for formatting 64-bit signed integers.
- [static var number: IntegerFormatStyle<UInt8>](formatstyle/number-8fms6.md)
  A style for formatting 8-bit unsigned integers.
- [static var number: IntegerFormatStyle<UInt16>](formatstyle/number-fak0.md)
  A style for formatting 16-bit unsigned integers.
- [static var number: IntegerFormatStyle<UInt32>](formatstyle/number-13mra.md)
  A style for formatting 32-bit unsigned integers.
- [static var number: IntegerFormatStyle<UInt64>](formatstyle/number-iyry.md)
  A style for formatting 64-bit unsigned integers.
- [struct IntegerFormatStyle](integerformatstyle.md)
  A structure that converts between integer values and their textual representations.
### Applying numeric styles for floating-point values
- [static var number: FloatingPointFormatStyle<Float>](formatstyle/number-432x3.md)
  A style for formatting the Swift standard single-precision floating-point type.
- [static var number: FloatingPointFormatStyle<Double>](formatstyle/number-8c8rj.md)
  A style for formatting the Swift standard double-precision floating-point type.
- [static var number: FloatingPointFormatStyle<Float16>](formatstyle/number-3qe2o.md)
  A style for formatting 16-bit floating-point values.
- [struct FloatingPointFormatStyle](floatingpointformatstyle.md)
  A structure that converts between floating-point values and their textual representations.
### Applying numeric styles for decimals
- [static var number: Decimal.FormatStyle](formatstyle/number-3luf2.md)
  A style for formatting decimal values.
- [Decimal.FormatStyle](decimal/formatstyle.md)
  A structure that converts between decimal values and their textual representations.
### Applying percentage styles for integers
- [static var percent: IntegerFormatStyle<Int>.Percent](formatstyle/percent-cl9k.md)
  A style for formatting signed integer types in Swift as a percent representation.
- [static var percent: IntegerFormatStyle<UInt>.Percent](formatstyle/percent-9pj79.md)
  A style for formatting signed integer types in Swift as a percent representation.
- [static var percent: IntegerFormatStyle<Int8>.Percent](formatstyle/percent-7r4rl.md)
  A style for formatting 8-bit signed integers as a percent representation.
- [static var percent: IntegerFormatStyle<Int16>.Percent](formatstyle/percent-3qjzh.md)
  A style for formatting 16-bit signed integers as a percent representation.
- [static var percent: IntegerFormatStyle<Int32>.Percent](formatstyle/percent-1f0q.md)
  A style for formatting 32-bit signed integers as a percent representation.
- [static var percent: IntegerFormatStyle<Int64>.Percent](formatstyle/percent-934se.md)
  A style for formatting 64-bit signed integers as a percent representation.
- [static var percent: IntegerFormatStyle<UInt8>.Percent](formatstyle/percent-8izzv.md)
  A style for formatting 8-bit unsigned integers as a percent representation.
- [static var percent: IntegerFormatStyle<UInt16>.Percent](formatstyle/percent-4kdme.md)
  A style for formatting 16-bit unsigned integers as a percent representation.
- [static var percent: IntegerFormatStyle<UInt32>.Percent](formatstyle/percent-2f11j.md)
  A style for formatting 32-bit unsigned integers as a percent representation.
- [static var percent: IntegerFormatStyle<UInt64>.Percent](formatstyle/percent-8bxla.md)
  A style for formatting 64-bit unsigned integers as a percent representation.
- [IntegerFormatStyle.Percent](integerformatstyle/percent.md)
  A format style that converts between integer percentage values and their textual representations.
### Applying percentage styles for floating-point values
- [static var percent: FloatingPointFormatStyle<Float>.Percent](formatstyle/percent-2gva1.md)
  A style for formatting the Swift standard single-precision floating-point type as a percent representation.
- [static var percent: FloatingPointFormatStyle<Double>.Percent](formatstyle/percent-6cwuv.md)
  A style for formatting the Swift standard single-precision floating-point type as a percent representation.
- [static var percent: FloatingPointFormatStyle<Float16>.Percent](formatstyle/percent-grss.md)
  A style for formatting 16-bit floating-point values as a percent representation.
- [FloatingPointFormatStyle.Percent](floatingpointformatstyle/percent.md)
  A format style that converts between floating-point percentage values and their textual representations.
### Applying percentage styles for decimals
- [static var percent: Decimal.FormatStyle.Percent](formatstyle/percent-4knsm.md)
  A style for formatting decimal values as a percent represntation.
- [Decimal.FormatStyle.Percent](decimal/formatstyle/percent.md)
  A format style that converts between decimal percentage values and their textual representations.
### Applying date and time styles
- [static var dateTime: Date.FormatStyle](formatstyle/datetime.md)
  A style for formatting a date and time.
- [struct FormatStyle](date/formatstyle.md)
  A structure that creates a locale-appropriate string representation of a date instance and converts strings of dates and times into date instances.
- [static var iso8601: Date.ISO8601FormatStyle](formatstyle/iso8601.md)
  A style for formatting a date in accordance with the ISO-8601 standard.
- [struct ISO8601FormatStyle](date/iso8601formatstyle.md)
  A type that converts between dates and their ISO-8601 string representations.
- [static func verbatim(Date.FormatString, locale: Locale?, timeZone: TimeZone, calendar: Calendar) -> Date.VerbatimFormatStyle](formatstyle/verbatim(_:locale:timezone:calendar:).md)
  Returns a style for formatting a date with an explicitly-specified style.
- [struct VerbatimFormatStyle](date/verbatimformatstyle.md)
  A style that formats a date with an explicitly-specified style.
- [static var interval: Date.IntervalFormatStyle](formatstyle/interval.md)
  A style for formatting a date interval.
- [struct IntervalFormatStyle](date/intervalformatstyle.md)
  A format style that creates string representations of date intervals.
- [static func relative(presentation: Date.RelativeFormatStyle.Presentation, unitsStyle: Date.RelativeFormatStyle.UnitsStyle) -> Self](formatstyle/relative(presentation:unitsstyle:).md)
  Returns a style for formatting a date as relative to the current date.
- [struct RelativeFormatStyle](date/relativeformatstyle.md)
  A format style that forms locale-aware string representations of a relative date or time.
- [static func components(style: Date.ComponentsFormatStyle.Style, fields: Set<Date.ComponentsFormatStyle.Field>?) -> Self](formatstyle/components(style:fields:).md)
  Returns a style for formatting a date interval in terms of specific date components.
- [struct ComponentsFormatStyle](date/componentsformatstyle.md)
  A style for formatting a date interval in terms of specific date components.
### Applying duration styles
- [static var timeDuration: Date.ComponentsFormatStyle](formatstyle/timeduration.md)
  A style for formatting a duration expressed as a range of dates.
- [struct ComponentsFormatStyle](date/componentsformatstyle.md)
  A style for formatting a date interval in terms of specific date components.
- [static func time(pattern: Duration.TimeFormatStyle.Pattern) -> Self](formatstyle/time(pattern:).md)
  Returns a style for formatting a duration using a provided pattern.
- [static func units(allowed: Set<Duration.UnitsFormatStyle.Unit>, width: Duration.UnitsFormatStyle.UnitWidth, maximumUnitCount: Int?, zeroValueUnits: Duration.UnitsFormatStyle.ZeroValueUnitsDisplayStrategy, valueLength: Int?, fractionalPart: Duration.UnitsFormatStyle.FractionalPartDisplayStrategy) -> Self](formatstyle/units(allowed:width:maximumunitcount:zerovalueunits:valuelength:fractionalpart:).md)
  Returns a style for formatting a duration that uses the specified units.
- [static func units<ValueRange>(allowed: Set<Duration.UnitsFormatStyle.Unit>, width: Duration.UnitsFormatStyle.UnitWidth, maximumUnitCount: Int?, zeroValueUnits: Duration.UnitsFormatStyle.ZeroValueUnitsDisplayStrategy, valueLengthLimits: ValueRange, fractionalPart: Duration.UnitsFormatStyle.FractionalPartDisplayStrategy) -> Self](formatstyle/units(allowed:width:maximumunitcount:zerovalueunits:valuelengthlimits:fractionalpart:).md)
  Returns a style for formatting a duration range that uses the specified units, with padding/truncating behavior defined as a range.
### Applying currency styles
- [static func currency<V>(code: String) -> Self](formatstyle/currency(code:)-is0v.md)
  Returns a format style to use integer currency notation.
- [static func currency<Value>(code: String) -> Self](formatstyle/currency(code:)-1yg68.md)
  Returns a format style to use floating-point currency notation.
- [static func currency(code: String) -> Self](formatstyle/currency(code:)-6fhr2.md)
  Returns a format style to use decimal currency notation.
### Applying measurement styles
- [static func measurement<UnitType>(width: Measurement<UnitType>.FormatStyle.UnitWidth, usage: MeasurementFormatUnitUsage<UnitType>, numberFormatStyle: FloatingPointFormatStyle<Double>?) -> Self](formatstyle/measurement(width:usage:numberformatstyle:).md)
  Returns a format style to format measurement units.
- [static func measurement(width: Measurement<UnitTemperature>.FormatStyle.UnitWidth, usage: MeasurementFormatUnitUsage<UnitTemperature>, hidesScaleName: Bool, numberFormatStyle: FloatingPointFormatStyle<Double>?) -> Self](formatstyle/measurement(width:usage:hidesscalename:numberformatstyle:).md)
  Returns a format style to format temperature units.
### Applying person name styles
- [static func name(style: PersonNameComponents.FormatStyle.Style) -> Self](formatstyle/name(style:).md)
  Returns a format style to use the given name style for formatting a name from its components.
### Applying list styles
- [static func list<MemberStyle, Base>(memberStyle: MemberStyle, type: ListFormatStyle<MemberStyle, Base>.ListType, width: ListFormatStyle<MemberStyle, Base>.Width) -> Self](formatstyle/list(memberstyle:type:width:).md)
  Returns a format style to format a list of items.
- [static func list<Base>(type: ListFormatStyle<StringStyle, Base>.ListType, width: ListFormatStyle<StringStyle, Base>.Width) -> Self](formatstyle/list(type:width:).md)
  Returns a format style to format a list of strings.
### Applying byte-count styles
- [static func byteCount(style: ByteCountFormatStyle.Style, allowedUnits: ByteCountFormatStyle.Units, spellsOutZero: Bool, includesActualByteCount: Bool) -> Self](formatstyle/bytecount(style:allowedunits:spellsoutzero:includesactualbytecount:)-59ep0.md)
  Returns a format style to format a data storage value.
- [struct ByteCountFormatStyle](bytecountformatstyle.md)
  A format style that provides string representations of byte counts.
- [static func byteCount(style: Measurement<UnitInformationStorage>.FormatStyle.ByteCount.Style, allowedUnits: Measurement<UnitInformationStorage>.FormatStyle.ByteCount.Units, spellsOutZero: Bool, includesActualByteCount: Bool) -> Self](formatstyle/bytecount(style:allowedunits:spellsoutzero:includesactualbytecount:)-ev0u.md)
  Returns a format style to format a data storage value represented with Foundation’s measurement type.
- [Measurement.FormatStyle.ByteCount](measurement/formatstyle/bytecount.md)
  A format style that provides string representations of byte counts, expressed as measurements of information storage.
### Applying URL styles
- [static var url: URL.FormatStyle](formatstyle/url.md)
  A style for formatting a URL.
- [struct FormatStyle](url/formatstyle.md)
  A structure that converts between URL instances and their textual representations.
### Declaring input and output types
- [associatedtype FormatInput](formatstyle/formatinput.md)
  The type this format style accepts as input.
- [associatedtype FormatOutput](formatstyle/formatoutput.md)
  The type this format style produces as output.
### Type Methods
- [static func offset(to: Date, allowedFields: Set<Date.ComponentsFormatStyle.Field>, maxFieldCount: Int, sign: NumberFormatStyleConfiguration.SignDisplayStrategy) -> SystemFormatStyle.DateOffset](formatstyle/offset(to:allowedfields:maxfieldcount:sign:).md)
- [static func reference(to: Date, allowedFields: Set<Date.RelativeFormatStyle.Field>, maxFieldCount: Int, thresholdField: Date.RelativeFormatStyle.Field) -> SystemFormatStyle.DateReference](formatstyle/reference(to:allowedfields:maxfieldcount:thresholdfield:).md)
- [static func stopwatch(startingAt: Date, showsHours: Bool, maxFieldCount: Int, maxPrecision: Duration) -> SystemFormatStyle.Stopwatch](formatstyle/stopwatch(startingat:showshours:maxfieldcount:maxprecision:).md)
- [static func timer(countingDownIn: Range<Date>, showsHours: Bool, maxFieldCount: Int, maxPrecision: Duration) -> SystemFormatStyle.Timer](formatstyle/timer(countingdownin:showshours:maxfieldcount:maxprecision:).md)
- [static func timer(countingUpIn: Range<Date>, showsHours: Bool, maxFieldCount: Int, maxPrecision: Duration) -> SystemFormatStyle.Timer](formatstyle/timer(countingupin:showshours:maxfieldcount:maxprecision:).md)

## Relationships

### Inherits From
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
### Inherited By
- [DiscreteFormatStyle](discreteformatstyle.md)
- [ParseableFormatStyle](parseableformatstyle.md)
### Conforming Types
- [ByteCountFormatStyle](bytecountformatstyle.md)
- [ByteCountFormatStyle.Attributed](bytecountformatstyle/attributed-swift.struct.md)
- [Date.AnchoredRelativeFormatStyle](date/anchoredrelativeformatstyle.md)
- [Date.AttributedStyle](date/attributedstyle.md)
- [Date.ComponentsFormatStyle](date/componentsformatstyle.md)
- [Date.FormatStyle](date/formatstyle.md)
- [Date.FormatStyle.Attributed](date/formatstyle/attributed-swift.struct.md)
- [Date.ISO8601FormatStyle](date/iso8601formatstyle.md)
- [Date.IntervalFormatStyle](date/intervalformatstyle.md)
- [Date.RelativeFormatStyle](date/relativeformatstyle.md)
- [Date.VerbatimFormatStyle](date/verbatimformatstyle.md)
- [Date.VerbatimFormatStyle.Attributed](date/verbatimformatstyle/attributed-swift.struct.md)
- [Decimal.FormatStyle](decimal/formatstyle.md)
- [Decimal.FormatStyle.Attributed](decimal/formatstyle/attributed-swift.struct.md)
- [Decimal.FormatStyle.Currency](decimal/formatstyle/currency.md)
- [Decimal.FormatStyle.Percent](decimal/formatstyle/percent.md)
- [FloatingPointFormatStyle](floatingpointformatstyle.md)
- [FloatingPointFormatStyle.Attributed](floatingpointformatstyle/attributed-swift.struct.md)
- [FloatingPointFormatStyle.Currency](floatingpointformatstyle/currency.md)
- [FloatingPointFormatStyle.Percent](floatingpointformatstyle/percent.md)
- [IntegerFormatStyle](integerformatstyle.md)
- [IntegerFormatStyle.Attributed](integerformatstyle/attributed-swift.struct.md)
- [IntegerFormatStyle.Currency](integerformatstyle/currency.md)
- [IntegerFormatStyle.Percent](integerformatstyle/percent.md)
- [ListFormatStyle](listformatstyle.md)
- [Measurement.AttributedStyle](measurement/attributedstyle.md)
- [Measurement.AttributedStyle.ByteCount](measurement/attributedstyle/bytecount.md)
- [Measurement.FormatStyle](measurement/formatstyle.md)
- [Measurement.FormatStyle.ByteCount](measurement/formatstyle/bytecount.md)
- [PersonNameComponents.AttributedStyle](personnamecomponents/attributedstyle.md)
- [PersonNameComponents.FormatStyle](personnamecomponents/formatstyle.md)
- [StringStyle](stringstyle.md)
- [URL.FormatStyle](url/formatstyle.md)

## See Also

- [struct IntegerFormatStyle](integerformatstyle.md)
  A structure that converts between integer values and their textual representations.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatstyle)*