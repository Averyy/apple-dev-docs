# CFStringCompareWithOptionsAndLocale(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Compares a range of the characters in one string with another string using a given locale.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFStringCompareWithOptionsAndLocale(_ theString1: CFString!, _ theString2: CFString!, _ rangeToCompare: CFRange, _ compareOptions: CFStringCompareFlags, _ locale: CFLocale!) -> CFComparisonResult
```

#### Return Value

A [`CFComparisonResult`](cfcomparisonresult.md) value that indicates whether `theString1` is equal to, less than, or greater than `theString2`.

## Parameters

- `theString1`: The first string to use in the comparison.
- `theString2`: The second string to use in the comparison. The full range of this string is used.
- `rangeToCompare`: The range of characters in `theString1` to be used in the comparison to `theString2`. To use the whole string, pass the range `CFRangeMake(0, CFStringGetLength(theString1))`. The specified range must not exceed the bounds of the string.
- `compareOptions`: Flags that select different types of comparisons, such as case-insensitive comparison and non-literal comparison. See [`String Comparison Flags`](string-comparison-flags.md) for the available flags. Specifying the `kCFCompareBackwards` or `kCFCompareAnchored` option has no effect. Specifying the `kCFCompareLocalized` option and passing `NULL` for `locale` causes the current locale (the return value of [`CFLocaleCopyCurrent()`](cflocalecopycurrent().md)) to be used.
- `locale`: The locale to use for the comparison, which affects both equality and ordering algorithms. For example, in some locales, accented characters are ordered immediately after the base; other locales order them after “z”. If `NULL` and the `kCFCompareLocalized` option is not specified for `compareOptions`, the comparison is nonlocalized.

## See Also

- [func CFStringCompare(CFString!, CFString!, CFStringCompareFlags) -> CFComparisonResult](cfstringcompare(_:_:_:).md)
  Compares one string with another string.
- [func CFStringCompareWithOptions(CFString!, CFString!, CFRange, CFStringCompareFlags) -> CFComparisonResult](cfstringcomparewithoptions(_:_:_:_:).md)
  Compares a range of the characters in one string with that of another string.
- [func CFStringHasPrefix(CFString!, CFString!) -> Bool](cfstringhasprefix(_:_:).md)
  Determines if the character data of a string begin with a specified sequence of characters.
- [func CFStringHasSuffix(CFString!, CFString!) -> Bool](cfstringhassuffix(_:_:).md)
  Determines if a string ends with a specified sequence of characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringcomparewithoptionsandlocale(_:_:_:_:_:))*