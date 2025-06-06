# CFStringFindWithOptionsAndLocale(_:_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a Boolean value that indicates whether a given string was found in a given source string.

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
func CFStringFindWithOptionsAndLocale(_ theString: CFString!, _ stringToFind: CFString!, _ rangeToSearch: CFRange, _ searchOptions: CFStringCompareFlags, _ locale: CFLocale!, _ result: UnsafeMutablePointer<CFRange>!) -> Bool
```

#### Return Value

`true` if the substring was found, `false` otherwise.

#### Discussion

If `stringToFind` is the empty string (zero length), nothing is found.

## Parameters

- `theString`: The string in which to to search for  .
- `stringToFind`: The substring to search for in  .
- `rangeToSearch`: A range of the characters to search in  . The specified range must not exceed the length of the string.
- `searchOptions`: The option flags to control the search behavior. See   for possible values. The flags   and   are ignored.
- `locale`: The locale argument affects the equality checking algorithm. For example, for the Turkish locale, case-insensitive compare matches “I” to “ı” (Unicode code point U+0131, Latin Small Dotless I), not the normal “i” character.
- `result`: On return, if the function result is   contains the starting location and length of the found substring. You may pass   if you only want to know if the   contains  .

## See Also

- [func CFStringCreateArrayWithFindResults(CFAllocator!, CFString!, CFString!, CFRange, CFStringCompareFlags) -> CFArray!](cfstringcreatearraywithfindresults(_:_:_:_:_:).md)
  Searches a string for multiple occurrences of a substring and creates an array of ranges identifying the locations of these substrings within the target string.
- [func CFStringFind(CFString!, CFString!, CFStringCompareFlags) -> CFRange](cfstringfind(_:_:_:).md)
  Searches for a substring within a string and, if it is found, yields the range of the substring within the object’s characters.
- [func CFStringFindCharacterFromSet(CFString!, CFCharacterSet!, CFRange, CFStringCompareFlags, UnsafeMutablePointer<CFRange>!) -> Bool](cfstringfindcharacterfromset(_:_:_:_:_:).md)
  Query the range of the first character contained in the specified character set.
- [func CFStringFindWithOptions(CFString!, CFString!, CFRange, CFStringCompareFlags, UnsafeMutablePointer<CFRange>!) -> Bool](cfstringfindwithoptions(_:_:_:_:_:).md)
  Searches for a substring within a range of the characters represented by a string and, if the substring is found, returns its range within the object’s characters.
- [func CFStringGetLineBounds(CFString!, CFRange, UnsafeMutablePointer<CFIndex>!, UnsafeMutablePointer<CFIndex>!, UnsafeMutablePointer<CFIndex>!)](cfstringgetlinebounds(_:_:_:_:_:).md)
  Given a range of characters in a string, obtains the line bounds—that is, the indexes of the first character and the final characters of the lines containing the range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringfindwithoptionsandlocale(_:_:_:_:_:_:))*