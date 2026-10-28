# CFStringHasSuffix(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Determines if a string ends with a specified sequence of characters.

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
func CFStringHasSuffix(_ theString: CFString!, _ suffix: CFString!) -> Bool
```

```c
extern Boolean CFStringHasSuffix(CFStringRef theString, CFStringRef suffix);
```

## Return Value

`true` if `theString` ends with `suffix`, `false` otherwise.

## Parameters

- `theString`: The string to be evaluated.
- `suffix`: The suffix to search for.

## See Also

### Comparing Strings
- [func CFStringCompare(CFString!, CFString!, CFStringCompareFlags) -> CFComparisonResult](./cfstringcompare%28_,_,_%29.md)
  Compares one string with another string.
- [func CFStringCompareWithOptions(CFString!, CFString!, CFRange, CFStringCompareFlags) -> CFComparisonResult](./cfstringcomparewithoptions%28_,_,_,_%29.md)
  Compares a range of the characters in one string with that of another string.
- [func CFStringCompareWithOptionsAndLocale(CFString!, CFString!, CFRange, CFStringCompareFlags, CFLocale!) -> CFComparisonResult](./cfstringcomparewithoptionsandlocale%28_,_,_,_,_%29.md)
  Compares a range of the characters in one string with another string using a given locale.
- [func CFStringHasPrefix(CFString!, CFString!) -> Bool](./cfstringhasprefix%28_,_%29.md)
  Determines if the character data of a string begin with a specified sequence of characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringhassuffix(_:_:))*