# isEqual(to:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value that indicates whether a given string is equal to the receiver using a literal Unicode-based comparison.

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
func isEqual(to aString: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if `aString` is equivalent to the receiver (if they have the same id or if they are `NSOrderedSame` in a literal comparison), otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The comparison uses the canonical representation of strings, which for a particular string is the length of the string plus the UTF-16 code units that make up the string. When this method compares two strings, if the individual Unicodes are the same, then the strings are equal, regardless of the backing store. “Literal” when applied to string comparison means that various Unicode decomposition rules are not applied and UTF-16 code units are individually compared. So, for instance, “Ö” represented as the composed character sequence “O” (`U+004F LATIN CAPITAL LETTER O`) and a combining diaeresis “¨” (`U+0308 COMBINING DIAERESIS`) would not compare equal to “Ö” represented as a single Unicode character (`U+00D6 LATIN CAPITAL LETTER O WITH DIAERESIS`).

##### Special Considerations

When you know both objects are strings, this method is a faster way to check equality than [`isEqual(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/isEqual(_:)).

## Parameters

- `aString`: The string with which to compare the receiver.

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
- [var hash: Int](nsstring/hash.md)
  An unsigned integer that can be used as a hash table address.
- [NSString.CompareOptions](nsstring/compareoptions.md)
  These values represent the options available to many of the string classes’ search and comparison methods.
- [NSString.EncodingConversionOptions](nsstring/encodingconversionoptions.md)
  Options for converting string encodings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/isequal(to:))*