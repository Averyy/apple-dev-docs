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
- `rangeToCompare`: The range of characters in   to be used in the comparison to  . To use the whole string, pass the range  . The specified range must not exceed the bounds of the string.
- `compareOptions`: Specifying the   option and passing   for   causes the current locale (the return value of  ) to be used.
- `locale`: If   and the   option is not specified for  , the comparison is nonlocalized.

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