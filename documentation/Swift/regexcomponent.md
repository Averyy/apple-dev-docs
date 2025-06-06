# RegexComponent

**Framework**: Swift  
**Kind**: protocol

A type that represents a regular expression.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
protocol RegexComponent<RegexOutput>
```

#### Overview

You can use types that conform to `RegexComponent` as parameters to string searching operations and inside `RegexBuilder` closures.

## Topics

### Creating a regex component
- [init(CharacterClass, CharacterClass...)](regexcomponent/init(_:_:).md)
  Creates a character class that combines the given classes in a union.
### Getting a regex from a component
- [var regex: Regex<Self.RegexOutput>](regexcomponent/regex.md)
  The regular expression represented by this component.
### Matching substring sequences
- [static func anyOf<S>(S) -> CharacterClass](regexcomponent/anyof(_:)-3pexl.md)
  Returns a character class that matches any Unicode scalar in the given sequence.
- [static func anyOf<S>(S) -> CharacterClass](regexcomponent/anyof(_:)-4xgea.md)
  Returns a character class that matches any character in the given string or sequence.
- [static var any: CharacterClass](regexcomponent/any.md)
  A character class that matches any element.
- [static var anyGraphemeCluster: CharacterClass](regexcomponent/anygraphemecluster.md)
  A character class that matches any single `Character`, or extended grapheme cluster, regardless of the current semantic level.
- [static var anyNonNewline: CharacterClass](regexcomponent/anynonnewline.md)
  A character class that matches any element that isn’t a newline.
- [static var digit: CharacterClass](regexcomponent/digit.md)
  A character class that matches any digit.
- [static var hexDigit: CharacterClass](regexcomponent/hexdigit.md)
  A character class that matches any hexadecimal digit.
- [static var word: CharacterClass](regexcomponent/word.md)
  A character class that matches any element that is a “word character”.
### Matching whitespace and line endings
- [static var horizontalWhitespace: CharacterClass](regexcomponent/horizontalwhitespace.md)
  A character class that matches any element that is classified as horizontal whitespace.
- [static var newlineSequence: CharacterClass](regexcomponent/newlinesequence.md)
  A character class that matches any newline sequence.
- [static var verticalWhitespace: CharacterClass](regexcomponent/verticalwhitespace.md)
  A character class that matches any element that is classified as vertical whitespace.
- [static var whitespace: CharacterClass](regexcomponent/whitespace.md)
  A character class that matches any element that is classified as whitespace.
### Matching dates and times
- [static func date(Date.FormatStyle.DateStyle, locale: Locale, timeZone: TimeZone, calendar: Calendar?) -> Date.ParseStrategy](regexcomponent/date(_:locale:timezone:calendar:).md)
  Creates a regex component that matches a localized date string formatted in accordance with a style, capturing it as a Foundation date.
- [static func date(format: Date.FormatString, locale: Locale, timeZone: TimeZone, calendar: Calendar?, twoDigitStartDate: Date) -> Self](regexcomponent/date(format:locale:timezone:calendar:twodigitstartdate:).md)
  Creates a regex component that matches a localized date string formatted in accordance with a format string, capturing it as a Foundation date.
- [static func dateTime(date: Date.FormatStyle.DateStyle, time: Date.FormatStyle.TimeStyle, locale: Locale, timeZone: TimeZone, calendar: Calendar?) -> Date.ParseStrategy](regexcomponent/datetime(date:time:locale:timezone:calendar:).md)
  Creates a regex component that matches a localized date and time string, capturing it as a Foundation date.
- [static var iso8601: Date.ISO8601FormatStyle](regexcomponent/iso8601.md)
  A regex component that matches a default ISO 8601-formatted date string, capturing it as a Foundation date.
- [static func iso8601Date(timeZone: TimeZone, dateSeparator: Date.ISO8601FormatStyle.DateSeparator) -> Self](regexcomponent/iso8601date(timezone:dateseparator:).md)
  Creates a regex component that matches an ISO 8601-formatted date string, capturing it as a Foundation date in the specified time zone.
- [static func iso8601(timeZone: TimeZone, includingFractionalSeconds: Bool, dateSeparator: Date.ISO8601FormatStyle.DateSeparator, dateTimeSeparator: Date.ISO8601FormatStyle.DateTimeSeparator, timeSeparator: Date.ISO8601FormatStyle.TimeSeparator) -> Self](regexcomponent/iso8601(timezone:includingfractionalseconds:dateseparator:datetimeseparator:timeseparator:).md)
  Creates a regex component that matches an ISO 8601-formatted date string, capturing the matched substring as a Foundation date in the specified time zone.
- [static func iso8601WithTimeZone(includingFractionalSeconds: Bool, dateSeparator: Date.ISO8601FormatStyle.DateSeparator, dateTimeSeparator: Date.ISO8601FormatStyle.DateTimeSeparator, timeSeparator: Date.ISO8601FormatStyle.TimeSeparator, timeZoneSeparator: Date.ISO8601FormatStyle.TimeZoneSeparator) -> Self](regexcomponent/iso8601withtimezone(includingfractionalseconds:dateseparator:datetimeseparator:timeseparator:timezoneseparator:).md)
  Creates a regex component that matches an ISO 8601-formatted date string that includes a time zone component, capturing the matched substring as a Foundation date.
### Matching numeric formats
- [static func localizedInteger(locale: Locale) -> Self](regexcomponent/localizedinteger(locale:).md)
  Creates a regex component that matches a localized numeric string, capturing it as an integer value.
- [static func localizedDouble(locale: Locale) -> Self](regexcomponent/localizeddouble(locale:).md)
  Creates a regex component that matches a localized numeric string, capturing it as a double-precision floating-point value.
- [static func localizedDecimal(locale: Locale) -> Self](regexcomponent/localizeddecimal(locale:).md)
  Creates a regex component that matches a localized decimal string, capturing it as a Foundation decimal.
- [static func localizedCurrency(code: Locale.Currency, locale: Locale) -> Self](regexcomponent/localizedcurrency(code:locale:).md)
  Creates a regex component that matches a localized currency string, capturing it as a decimal value.
- [static func localizedIntegerCurrency(code: Locale.Currency, locale: Locale) -> Self](regexcomponent/localizedintegercurrency(code:locale:).md)
  Creates a regex component that matches a localized currency string, capturing it as an integer value.
- [static func localizedIntegerPercentage(locale: Locale) -> Self](regexcomponent/localizedintegerpercentage(locale:).md)
  Creates a regex component that matches a localized percentage string, capturing it as a double-precision floating-point value.
- [static func localizedDoublePercentage(locale: Locale) -> Self](regexcomponent/localizeddoublepercentage(locale:).md)
  Creates a regex component that matches a localized percentage string, capturing it as a double-precision floating-point value.
### Matching URLs
- [static func url(scheme: URL.ParseStrategy.ComponentParseStrategy<String>, user: URL.ParseStrategy.ComponentParseStrategy<String>, password: URL.ParseStrategy.ComponentParseStrategy<String>, host: URL.ParseStrategy.ComponentParseStrategy<String>, port: URL.ParseStrategy.ComponentParseStrategy<Int>, path: URL.ParseStrategy.ComponentParseStrategy<String>, query: URL.ParseStrategy.ComponentParseStrategy<String>, fragment: URL.ParseStrategy.ComponentParseStrategy<String>) -> Self](regexcomponent/url(scheme:user:password:host:port:path:query:fragment:).md)
  Creates a regex component that matches a URL substring, capturing it as a Foundation URL.
### Supporting types
- [associatedtype RegexOutput](regexcomponent/regexoutput.md)
  The output type for this regular expression.
- [RegexComponent.DateStyle](regexcomponent/datestyle.md)
  A type alias to use when matching date components in a regular expression.
- [RegexComponent.TimeStyle](regexcomponent/timestyle.md)
  A type alias to use when matching time components in a regular expression.

## Relationships

### Inherited By
- [CustomConsumingRegexComponent](customconsumingregexcomponent.md)
### Conforming Types
- [Anchor](../regexbuilder/anchor.md)
- [Capture](../regexbuilder/capture.md)
- [Character](character.md)
- [CharacterClass](../regexbuilder/characterclass.md)
- [ChoiceOf](../regexbuilder/choiceof.md)
- [Local](../regexbuilder/local.md)
- [Lookahead](../regexbuilder/lookahead.md)
- [NegativeLookahead](../regexbuilder/negativelookahead.md)
- [One](../regexbuilder/one.md)
- [OneOrMore](../regexbuilder/oneormore.md)
- [Optionally](../regexbuilder/optionally.md)
- [Reference](../regexbuilder/reference.md)
- [Regex](regex.md)
- [Repeat](../regexbuilder/repeat.md)
- [String](string.md)
- [Substring](substring.md)
- [TryCapture](../regexbuilder/trycapture.md)
- [Unicode.Scalar](unicode/scalar.md)
- [ZeroOrMore](../regexbuilder/zeroormore.md)

## See Also

- [struct Regex](regex.md)
  A regular expression.
- [struct RegexRepetitionBehavior](regexrepetitionbehavior.md)
  Specifies how much to attempt to match when using a quantifier.
- [struct RegexSemanticLevel](regexsemanticlevel.md)
  A semantic level to use during regex matching.
- [struct RegexWordBoundaryKind](regexwordboundarykind.md)
  A word boundary algorithm to use during regex matching.
- [struct AnyRegexOutput](anyregexoutput.md)
  The type-erased, dynamic output of a regular expression match.
- [protocol CustomConsumingRegexComponent](customconsumingregexcomponent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regexcomponent)*