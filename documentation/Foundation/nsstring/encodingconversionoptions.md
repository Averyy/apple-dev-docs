# NSString.EncodingConversionOptions

**Framework**: Foundation  
**Kind**: struct

Options for converting string encodings.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct EncodingConversionOptions
```

#### Overview

These constants are available in OS X v10.4; they are, however, differently named:

```objc
typedef enum {
    NSAllowLossyEncodingConversion = 1,
    NSExternalRepresentationEncodingConversion = 2
} NSStringEncodingConversionOptions;
```

You can use them in OS X v10.4 if you define the symbols as `extern` constants.

## Topics

### Constants
- [static var allowLossy: NSString.EncodingConversionOptions](nsstring/encodingconversionoptions/allowlossy.md)
  Allows lossy conversion.
- [static var externalRepresentation: NSString.EncodingConversionOptions](nsstring/encodingconversionoptions/externalrepresentation.md)
  Specifies an external representation (with a byte-order mark, if necessary, to indicate endianness).
- [static var allowLossy: NSString.EncodingConversionOptions](nsstring/encodingconversionoptions/allowlossy.md)
  Allows lossy conversion.
- [static var externalRepresentation: NSString.EncodingConversionOptions](nsstring/encodingconversionoptions/externalrepresentation.md)
  Specifies an external representation (with a byte-order mark, if necessary, to indicate endianness).
### Initializers
- [init(rawValue: UInt)](nsstring/encodingconversionoptions/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func caseInsensitiveCompare(String) -> ComparisonResult](nsstring/caseinsensitivecompare(_:).md)
  Returns the result of invoking [`compare(_:options:)`](nsstring/compare(_:options:).md) with `NSCaseInsensitiveSearch` as the only option.
- [func localizedCaseInsensitiveCompare(String) -> ComparisonResult](nsstring/localizedcaseinsensitivecompare(_:).md)
  Compares the string with a given string using a case-insensitive, localized, comparison.
- [func compare(String) -> ComparisonResult](nsstring/compare(_:).md)
  Returns the result of invoking [`compare(_:options:range:)`](nsstring/compare(_:options:range:).md) with no options and the receiver’s full extent as the range.
- [func localizedCompare(String) -> ComparisonResult](nsstring/localizedcompare(_:).md)
  Compares the string and a given string using a localized comparison.
- [func compare(String, options: NSString.CompareOptions) -> ComparisonResult](nsstring/compare(_:options:).md)
  Compares the string with the specified string using the given options.
- [func compare(String, options: NSString.CompareOptions, range: NSRange) -> ComparisonResult](nsstring/compare(_:options:range:).md)
  Returns the result of invoking [`compare(_:options:range:locale:)`](nsstring/compare(_:options:range:locale:).md) with a `nil` locale.
- [func compare(String, options: NSString.CompareOptions, range: NSRange, locale: Any?) -> ComparisonResult](nsstring/compare(_:options:range:locale:).md)
  Compares the string using the specified options and returns the lexical ordering for the range.
- [func localizedStandardCompare(String) -> ComparisonResult](nsstring/localizedstandardcompare(_:).md)
  Compares strings as sorted by the Finder.
- [func hasPrefix(String) -> Bool](nsstring/hasprefix(_:).md)
  Returns a Boolean value that indicates whether a given string matches the beginning characters of the receiver.
- [func hasSuffix(String) -> Bool](nsstring/hassuffix(_:).md)
  Returns a Boolean value that indicates whether a given string matches the ending characters of the receiver.
- [func isEqual(to: String) -> Bool](nsstring/isequal(to:).md)
  Returns a Boolean value that indicates whether a given string is equal to the receiver using a literal Unicode-based comparison.
- [var hash: Int](nsstring/hash.md)
  An unsigned integer that can be used as a hash table address.
- [NSString.CompareOptions](nsstring/compareoptions.md)
  These values represent the options available to many of the string classes’ search and comparison methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/encodingconversionoptions)*