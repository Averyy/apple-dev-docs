# CFStringCompare(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Compares one string with another string.

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
func CFStringCompare(_ theString1: CFString!, _ theString2: CFString!, _ compareOptions: CFStringCompareFlags) -> CFComparisonResult
```

```c
extern CFComparisonResult CFStringCompare(CFStringRef theString1, CFStringRef theString2, CFStringCompareFlags compareOptions);
```

#### Return Value

A [`CFComparisonResult`](./cfcomparisonresult.md) value that indicates whether `theString1` is equal to, less than, or greater than `theString2`.

#### Discussion

You can affect how the comparison proceeds by specifying one or more option flags in `compareOptions`. Not all comparison options are currently implemented.

## Parameters

- `theString1`: The first string to use in the comparison.
- `theString2`: The second string to use in the comparison.
- `compareOptions`: Flags that select different types of comparisons, such as localized comparison, case-insensitive comparison, and non-literal comparison. If you want the default comparison behavior, pass `0`. See [String Comparison Flags](./string-comparison-flags.md) for the available flags.

## See Also

### Comparing Strings
- [func CFStringCompareWithOptions(CFString!, CFString!, CFRange, CFStringCompareFlags) -> CFComparisonResult](./cfstringcomparewithoptions%28_,_,_,_%29.md)
  Compares a range of the characters in one string with that of another string.
- [func CFStringCompareWithOptionsAndLocale(CFString!, CFString!, CFRange, CFStringCompareFlags, CFLocale!) -> CFComparisonResult](./cfstringcomparewithoptionsandlocale%28_,_,_,_,_%29.md)
  Compares a range of the characters in one string with another string using a given locale.
- [func CFStringHasPrefix(CFString!, CFString!) -> Bool](./cfstringhasprefix%28_,_%29.md)
  Determines if the character data of a string begin with a specified sequence of characters.
- [func CFStringHasSuffix(CFString!, CFString!) -> Bool](./cfstringhassuffix%28_,_%29.md)
  Determines if a string ends with a specified sequence of characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringcompare(_:_:_:))*