# compare(_:options:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Compares the string with the specified string using the given options.

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
func compare(_ string: String, options mask: NSString.CompareOptions = []) -> ComparisonResult
```

```objc
- (NSComparisonResult) compare:(NSString *) string options:(NSStringCompareOptions) mask;
```

#### Return Value

Returns an [`ComparisonResult`](../comparisonresult.md) value that indicates the lexical ordering. [`ComparisonResult.orderedAscending`](../comparisonresult/orderedascending.md) the receiver precedes `aString` in lexical ordering, [`ComparisonResult.orderedSame`](../comparisonresult/orderedsame.md) the receiver and `aString` are equivalent in lexical value, and [`ComparisonResult.orderedDescending`](../comparisonresult/ordereddescending.md) if the receiver follows `aString`.

#### Discussion

This method is equivalent to invoking [`compare(_:options:range:)`](./compare%28_,options,range%29.md) with a given mask as the options and the receiver’s full extent as the range.

> ❗ **Important**:  When working with text that’s presented to the user, use the [`localizedStandardCompare(_:)`](./localizedstandardcompare%28_%29.md) instead, or use the [`compare(_:options:range:locale:)`](./compare%28_,options,range,locale%29.md) method, passing the user’s locale.

## Parameters

- `string`: The string with which to compare the receiver.

  This value must not be `nil`. If this value is `nil`, the behavior is undefined and may change in future versions of macOS.
- `mask`: Options for the search—you can combine any of the following using a C bitwise OR operator: [`caseInsensitive`](./compareoptions/caseinsensitive.md), [`literal`](./compareoptions/literal.md), [`numeric`](./compareoptions/numeric.md). See [String Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/introStrings.html#//apple_ref/doc/uid/10000035i) for details on these options.

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
- [NSString.EncodingConversionOptions](./encodingconversionoptions.md)
  Options for converting string encodings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/compare(_:options:))*