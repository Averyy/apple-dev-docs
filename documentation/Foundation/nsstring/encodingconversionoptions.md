# NSString.EncodingConversionOptions

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
enum NSStringEncodingConversionOptions : NSUInteger;
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
- [static var allowLossy: NSString.EncodingConversionOptions](./encodingconversionoptions/allowlossy.md)
  Allows lossy conversion.
- [static var externalRepresentation: NSString.EncodingConversionOptions](./encodingconversionoptions/externalrepresentation.md)
  Specifies an external representation (with a byte-order mark, if necessary, to indicate endianness).
### Initializers
- [init(rawValue: UInt)](./encodingconversionoptions/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Identifying and Comparing Strings
- [func caseInsensitiveCompare(String) -> ComparisonResult](./caseinsensitivecompare%28_%29.md)
  Returns the result of invoking [`compare(_:options:)`](./compare%28_,options%29.md) with `NSCaseInsensitiveSearch` as the only option.
- [func localizedCaseInsensitiveCompare(String) -> ComparisonResult](./localizedcaseinsensitivecompare%28_%29.md)
  Compares the string with a given string using a case-insensitive, localized, comparison.
- [func compare(String) -> ComparisonResult](./compare%28_%29.md)
  Returns the result of invoking [`compare(_:options:range:)`](./compare%28_,options,range%29.md) with no options and the receiver’s full extent as the range.
- [func localizedCompare(String) -> ComparisonResult](./localizedcompare%28_%29.md)
  Compares the string and a given string using a localized comparison.
- [func compare(String, options: NSString.CompareOptions) -> ComparisonResult](./compare%28_,options%29.md)
  Compares the string with the specified string using the given options.
- [func compare(String, options: NSString.CompareOptions, range: NSRange) -> ComparisonResult](./compare%28_,options,range%29.md)
  Returns the result of invoking [`compare(_:options:range:locale:)`](./compare%28_,options,range,locale%29.md) with a `nil` locale.
- [func compare(String, options: NSString.CompareOptions, range: NSRange, locale: Any?) -> ComparisonResult](./compare%28_,options,range,locale%29.md)
  Compares the string using the specified options and returns the lexical ordering for the range.
- [func localizedStandardCompare(String) -> ComparisonResult](./localizedstandardcompare%28_%29.md)
  Compares strings as sorted by the Finder.
- [func hasPrefix(String) -> Bool](./hasprefix%28_%29.md)
  Returns a Boolean value that indicates whether a given string matches the beginning characters of the receiver.
- [func hasSuffix(String) -> Bool](./hassuffix%28_%29.md)
  Returns a Boolean value that indicates whether a given string matches the ending characters of the receiver.
- [func isEqual(to: String) -> Bool](./isequal%28to%29.md)
  Returns a Boolean value that indicates whether a given string is equal to the receiver using a literal Unicode-based comparison.
- [var hash: Int](./hash.md)
  An unsigned integer that can be used as a hash table address.
- [NSString.CompareOptions](./compareoptions.md)
  These values represent the options available to many of the string classes’ search and comparison methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/encodingconversionoptions)*