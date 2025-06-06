# Strings and Text

**Framework**: Foundation

Create and process strings of Unicode characters, use regular expressions to find patterns, and perform natural language analysis of text.

## Topics

### Strings
- [@frozen struct String](../Swift/String.md)
  A Unicode string value that is a collection of characters.
- [String Encodings](1497293-string-encodings.md)
  Constants for encoding standards used when converting raw data to and from string representations.
### Strings with Metadata
- [struct AttributedString](attributedstring.md)
  A value type for a string with associated attributes for portions of its text.
- [struct AttributedSubstring](attributedsubstring.md)
  A portion of an attributed string.
- [Attributed String Supporting Types](attributed-string-supporting-types.md)
  Types that the attributed string, attributed substring, and helper types extend or conform to, for sharing common functionality.
- [class NSAttributedString](nsattributedstring.md)
  A string of text that manages data, layout, and stylistic information for ranges of characters to support rendering.
- [class NSMutableAttributedString](nsmutableattributedstring.md)
  A mutable string with associated attributes (such as visual style, hyperlinks, or accessibility data) for portions of its text.
### Characters
- [struct CharacterSet](characterset.md)
  A set of Unicode character values for use in search operations.
- [typealias UnicodeScalar = Unicode.Scalar](../Swift/UnicodeScalar.md)
### Pattern Matching
- [class Scanner](scanner.md)
  A string parser that scans for substrings or characters in a character set, and for numeric values from decimal, hexadecimal, and floating-point representations.
- [class NSRegularExpression](nsregularexpression.md)
  An immutable representation of a compiled regular expression that you apply to Unicode strings.
- [class NSDataDetector](nsdatadetector.md)
  A specialized regular expression object that matches natural language text for predefined data patterns.
- [class NSTextCheckingResult](nstextcheckingresult.md)
  An occurrence of textual content found during the analysis of a block of text, such as when matching a regular expression.
- [let NSNotFound: Int](nsnotfound-4qp9h.md)
  A value indicating that a requested item couldn’t be found or doesn’t exist.
### Spelling and Grammar
- [class NSSpellServer](nsspellserver.md)
  A server that your app uses to provide a spell checker service to other apps running in the system.
- [protocol NSSpellServerDelegate](nsspellserverdelegate.md)
  The optional methods implemented by the delegate of a spell server.
### Localization
- [struct Locale](locale.md)
  Information about linguistic, cultural, and technological conventions for use in formatting data for presentation.
- [class NSOrthography](nsorthography.md)
  A description of the linguistic content of natural language text, typically used for spelling and grammar checking.
- [func NSLocalizedString(String, tableName: String?, bundle: Bundle, value: String, comment: String) -> String](nslocalizedstring(_:tablename:bundle:value:comment:).md)
  Returns a localized string from a table that Xcode generates for you when exporting localizations.
- [struct LocalizedStringResource](localizedstringresource.md)
  A reference to a localizable string, accessible from another process.
- [protocol CustomLocalizedStringResourceConvertible](customlocalizedstringresourceconvertible.md)
  A type that provides an out-of-process localizable description.
- [struct URLResource](urlresource.md)
  A resource located at a particular file URL within a bundle.
### Deprecated
- [class NSLinguisticTagger](nslinguistictagger.md)
  Analyze natural language text to tag part of speech and lexical class, identify names, perform lemmatization, and determine the language and script.
- [Deprecated String Encodings](1497268-deprecated-string-encodings.md)

## See Also

- [Numbers, Data, and Basic Values](numbers-data-and-basic-values.md)
  Work with primitive values and other fundamental types used throughout Cocoa.
- [Collections](collections.md)
  Use arrays, dictionaries, sets, and specialized collections to store and iterate groups of objects or values.
- [Dates and Times](dates-and-times.md)
  Compare dates and times, and perform calendar and time zone calculations.
- [Units and Measurement](units-and-measurement.md)
  Label numeric quantities with physical dimensions to allow locale-aware formatting and conversion between related units.
- [Data Formatting](data-formatting.md)
  Convert numbers, dates, measurements, and other values to and from locale-aware string representations.
- [Filters and Sorting](filters-and-sorting.md)
  Use predicates, expressions, and sort descriptors to examine elements in collections and other services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/strings-and-text)*