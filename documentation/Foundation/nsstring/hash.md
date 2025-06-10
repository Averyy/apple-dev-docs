# hash

**Framework**: Foundation  
**Kind**: property

An unsigned integer that can be used as a hash table address.

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
var hash: Int { get }
```

#### Discussion

If two string objects are equal (as determined by the [`isEqual(to:)`](nsstring/isequal(to:).md) method), they must have the same hash value. This property fulfills this requirement.

You should not rely on this property having the same hash value across releases of macOS.

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
- [NSString.CompareOptions](nsstring/compareoptions.md)
  These values represent the options available to many of the string classes’ search and comparison methods.
- [NSString.EncodingConversionOptions](nsstring/encodingconversionoptions.md)
  Options for converting string encodings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/hash)*