# CFStringFindWithOptions(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Searches for a substring within a range of the characters represented by a string and, if the substring is found, returns its range within the object’s characters.

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
func CFStringFindWithOptions(_ theString: CFString!, _ stringToFind: CFString!, _ rangeToSearch: CFRange, _ searchOptions: CFStringCompareFlags, _ result: UnsafeMutablePointer<CFRange>!) -> Bool
```

```c
extern Boolean CFStringFindWithOptions(CFStringRef theString, CFStringRef stringToFind, CFRange rangeToSearch, CFStringCompareFlags searchOptions, CFRange *result);
```

#### Return Value

`true` if the substring was found, `false` otherwise.

#### Discussion

This function allows you to search only part of the characters of a string for a substring. It returns the found range indirectly, in the final `result` parameter. If you want to know if the entire range of characters represented by a string contains a particular substring, you can use the convenience function [`CFStringFind(_:_:_:)`](./cfstringfind%28_,_,_%29.md). Both of these functions return upon finding the first occurrence of the substring, so if you want to find out about multiple occurrences, call the [`CFStringCreateArrayWithFindResults(_:_:_:_:_:)`](./cfstringcreatearraywithfindresults%28_,_,_,_,_%29.md) function.

Depending on the comparison-option flags specified, the length of the resulting range might be different than the length of the search string.

## Parameters

- `theString`: The string in which to to search for `stringToFind`.
- `stringToFind`: The substring to search for in `theString`.
- `rangeToSearch`: A range of the characters to search in `theString`. The specified range must not exceed the length of the string.
- `searchOptions`: The option flags to control the search behavior. See [String Comparison Flags](./string-comparison-flags.md) for possible values. The flags [`compareNumerically`](./cfstringcompareflags/comparenumerically.md) and [`compareForcedOrdering`](./cfstringcompareflags/compareforcedordering.md) are ignored.
- `result`: On return, if the function result is `true`, contains the starting location and length of the found substring. You may pass `NULL` if you only want to know if the substring exists in the larger string.

## See Also

### Searching Strings
- [func CFStringCreateArrayWithFindResults(CFAllocator!, CFString!, CFString!, CFRange, CFStringCompareFlags) -> CFArray!](./cfstringcreatearraywithfindresults%28_,_,_,_,_%29.md)
  Searches a string for multiple occurrences of a substring and creates an array of ranges identifying the locations of these substrings within the target string.
- [func CFStringFind(CFString!, CFString!, CFStringCompareFlags) -> CFRange](./cfstringfind%28_,_,_%29.md)
  Searches for a substring within a string and, if it is found, yields the range of the substring within the object’s characters.
- [func CFStringFindCharacterFromSet(CFString!, CFCharacterSet!, CFRange, CFStringCompareFlags, UnsafeMutablePointer<CFRange>!) -> Bool](./cfstringfindcharacterfromset%28_,_,_,_,_%29.md)
  Query the range of the first character contained in the specified character set.
- [func CFStringFindWithOptionsAndLocale(CFString!, CFString!, CFRange, CFStringCompareFlags, CFLocale!, UnsafeMutablePointer<CFRange>!) -> Bool](./cfstringfindwithoptionsandlocale%28_,_,_,_,_,_%29.md)
  Returns a Boolean value that indicates whether a given string was found in a given source string.
- [func CFStringGetLineBounds(CFString!, CFRange, UnsafeMutablePointer<CFIndex>!, UnsafeMutablePointer<CFIndex>!, UnsafeMutablePointer<CFIndex>!)](./cfstringgetlinebounds%28_,_,_,_,_%29.md)
  Given a range of characters in a string, obtains the line bounds—that is, the indexes of the first character and the final characters of the lines containing the range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringfindwithoptions(_:_:_:_:_:))*