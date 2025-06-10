# Data Formatting

**Framework**: Foundation

Convert numbers, dates, measurements, and other values to and from locale-aware string representations.

#### Overview

Foundation supports two approaches for data formatting:

- When working in Swift, use `formatted` methods directly on the types you want to format, optionally using [`FormatStyle`](formatstyle.md) and its subtypes to customize formatter output. This approach supports dates, integers, floating-point numbers, measurements, sequences, and person name components. Foundation caches identically-configured formatter instances internally, allowing you to focus on your app’s formatting needs.
- In Objective-C, create instances of [`Formatter`](formatter.md) and its subtypes, and use the [`string(for:)`](formatter/string(for:).md) method to convert objects to formatted strings.

## Topics

### Data formatting in Swift
- [Language Introspector](language-introspector.md)
  Converts data into human-readable text using formatters and locales.
- [protocol FormatStyle](formatstyle.md)
  A type that converts a given data type into a representation in another type, such as a string.
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
### Data parsing in Swift
- [protocol ParseableFormatStyle](parseableformatstyle.md)
  A type that can convert a given input data type into a representation in an output type.
- [protocol ParseStrategy](parsestrategy.md)
  A type that parses an input representation, such as a formatted string, into a provided data type.
- [struct IntegerParseStrategy](integerparsestrategy.md)
  A parse strategy for creating integer values from formatted strings.
- [struct FloatingPointParseStrategy](floatingpointparsestrategy.md)
  A parse strategy for creating floating-point values from formatted strings.
- [Decimal.ParseStrategy](decimal/parsestrategy.md)
  A parse strategy for creating decimal values from formatted strings.
### Numbers and currency
- [class NumberFormatter](numberformatter.md)
  A formatter that converts between numeric values and their textual representations.
### Names
- [class PersonNameComponentsFormatter](personnamecomponentsformatter.md)
  A formatter that provides localized representations of the components of a person’s name.
- [struct PersonNameComponents](personnamecomponents.md)
  The separate parts of a person’s name, allowing locale-aware formatting.
### Dates and times
- [class DateFormatter](dateformatter.md)
  A formatter that converts between dates and their textual representations.
- [class DateComponentsFormatter](datecomponentsformatter.md)
  A formatter that creates string representations of quantities of time.
- [class RelativeDateTimeFormatter](relativedatetimeformatter.md)
  A formatter that creates locale-aware string representations of a relative date or time.
- [class DateIntervalFormatter](dateintervalformatter.md)
  A formatter that creates string representations of time intervals.
- [class ISO8601DateFormatter](iso8601dateformatter.md)
  A formatter that converts between dates and their ISO 8601 string representations.
### Data sizes
- [class ByteCountFormatter](bytecountformatter.md)
  A formatter that converts a byte count value into a localized description that is formatted with the appropriate byte modifier (KB, MB, GB and so on).
### Measurements
- [class MeasurementFormatter](measurementformatter.md)
  A formatter that provides localized representations of units and measurements.
### Lists
- [class ListFormatter](listformatter.md)
  An object that provides locale-correct formatting of a list of items using the appropriate separator and conjunction.
### Internationalization
- [struct Locale](locale.md)
  Information about linguistic, cultural, and technological conventions for use in formatting data for presentation.
### Custom formatters
- [class Formatter](formatter.md)
  An abstract class that declares an interface for objects that create, interpret, and validate the textual representation of values.
### Automatic grammar agreement
- [enum InflectionRule](inflectionrule.md)
  A rule that affects how an attributed string performs automatic grammatical agreement.
- [struct Morphology](morphology.md)
  A description of the grammatical properties of a string.
- [struct TermOfAddress](termofaddress.md)
  The type for representing grammatical gender in localized text.
- [enum InflectionConcept](inflectionconcept.md)
  An inflection method to use when localizing text.
- [Morphology.Pronoun](morphology/pronoun.md)
  A custom pronoun for referring to a third person.
### Deprecated
- [class LengthFormatter](lengthformatter.md)
  A formatter that provides localized descriptions of linear distances, such as length and height measurements.
- [class MassFormatter](massformatter.md)
  A formatter that provides localized descriptions of mass and weight values.
- [class EnergyFormatter](energyformatter.md)
  A formatter that provides localized descriptions of energy values.

## See Also

- [Numbers, Data, and Basic Values](numbers-data-and-basic-values.md)
  Work with primitive values and other fundamental types used throughout Cocoa.
- [Strings and Text](strings-and-text.md)
  Create and process strings of Unicode characters, use regular expressions to find patterns, and perform natural language analysis of text.
- [Collections](collections.md)
  Use arrays, dictionaries, sets, and specialized collections to store and iterate groups of objects or values.
- [Dates and Times](dates-and-times.md)
  Compare dates and times, and perform calendar and time zone calculations.
- [Units and Measurement](units-and-measurement.md)
  Label numeric quantities with physical dimensions to allow locale-aware formatting and conversion between related units.
- [Filters and Sorting](filters-and-sorting.md)
  Use predicates, expressions, and sort descriptors to examine elements in collections and other services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data-formatting)*