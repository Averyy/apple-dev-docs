# CFStringCompareWithOptions(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Compares a range of the characters in one string with that of another string.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFStringCompareWithOptions(_ theString1: CFString!, _ theString2: CFString!, _ rangeToCompare: CFRange, _ compareOptions: CFStringCompareFlags) -> CFComparisonResult
```

```c
extern CFComparisonResult CFStringCompareWithOptions(CFStringRef theString1, CFStringRef theString2, CFRange rangeToCompare, CFStringCompareFlags compareOptions);
```

## Return Value

A [`CFComparisonResult`](./cfcomparisonresult.md) value that indicates whether `theString1` is equal to, less than, or greater than `theString2`.

## Discussion

You can affect how the comparison proceeds by specifying one or more option flags in `compareOptions`.

If you want to compare one entire string with another string, use the [`CFStringCompare(_:_:_:)`](./cfstringcompare%28_,_,_%29.md) function.

## Parameters

- `theString1`: The first string to use in the comparison.
- `theString2`: The second string to use in the comparison.
- `rangeToCompare`: The range of characters in `theString1` to be used in the comparison to `theString2`. To use the whole string, pass the range `CFRangeMake(0, CFStringGetLength(theString1))` or use [`CFStringCompare(_:_:_:)`](./cfstringcompare%28_,_,_%29.md). The specified range must not exceed the length of the string.
- `compareOptions`: Flags that select different types of comparisons, such as localized comparison, case-insensitive comparison, and non-literal comparison. If you want the default comparison behavior, pass `0`. See [String Comparison Flags](./string-comparison-flags.md) for the available flags.

## See Also

### Comparing Strings
- [func CFStringCompare(CFString!, CFString!, CFStringCompareFlags) -> CFComparisonResult](./cfstringcompare%28_,_,_%29.md)
  Compares one string with another string.
- [func CFStringCompareWithOptionsAndLocale(CFString!, CFString!, CFRange, CFStringCompareFlags, CFLocale!) -> CFComparisonResult](./cfstringcomparewithoptionsandlocale%28_,_,_,_,_%29.md)
  Compares a range of the characters in one string with another string using a given locale.
- [func CFStringHasPrefix(CFString!, CFString!) -> Bool](./cfstringhasprefix%28_,_%29.md)
  Determines if the character data of a string begin with a specified sequence of characters.
- [func CFStringHasSuffix(CFString!, CFString!) -> Bool](./cfstringhassuffix%28_,_%29.md)
  Determines if a string ends with a specified sequence of characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringcomparewithoptions(_:_:_:_:))*