# CFStringCompareWithOptions(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Compares a range of the characters in one string with that of another string.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFStringCompareWithOptions(_ theString1: CFString!, _ theString2: CFString!, _ rangeToCompare: CFRange, _ compareOptions: CFStringCompareFlags) -> CFComparisonResult
```

#### Return Value

A [`CFComparisonResult`](cfcomparisonresult.md) value that indicates whether `theString1` is equal to, less than, or greater than `theString2`.

#### Discussion

You can affect how the comparison proceeds by specifying one or more option flags in `compareOptions`.

If you want to compare one entire string with another string, use the [`CFStringCompare(_:_:_:)`](cfstringcompare(_:_:_:).md) function.

## Parameters

- `theString1`: The first string to use in the comparison.
- `theString2`: The second string to use in the comparison.
- `rangeToCompare`: The range of characters in   to be used in the comparison to  . To use the whole string, pass the range   or use  . The specified range must not exceed the length of the string.
- `compareOptions`: Flags that select different types of comparisons, such as localized comparison, case-insensitive comparison, and non-literal comparison. If you want the default comparison behavior, pass  . See   for the available flags.

## See Also

- [func CFStringCompare(CFString!, CFString!, CFStringCompareFlags) -> CFComparisonResult](cfstringcompare(_:_:_:).md)
  Compares one string with another string.
- [func CFStringCompareWithOptionsAndLocale(CFString!, CFString!, CFRange, CFStringCompareFlags, CFLocale!) -> CFComparisonResult](cfstringcomparewithoptionsandlocale(_:_:_:_:_:).md)
  Compares a range of the characters in one string with another string using a given locale.
- [func CFStringHasPrefix(CFString!, CFString!) -> Bool](cfstringhasprefix(_:_:).md)
  Determines if the character data of a string begin with a specified sequence of characters.
- [func CFStringHasSuffix(CFString!, CFString!) -> Bool](cfstringhassuffix(_:_:).md)
  Determines if a string ends with a specified sequence of characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringcomparewithoptions(_:_:_:_:))*