# CFStringCreateArrayWithFindResults(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Searches a string for multiple occurrences of a substring and creates an array of ranges identifying the locations of these substrings within the target string.

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
func CFStringCreateArrayWithFindResults(_ alloc: CFAllocator!, _ theString: CFString!, _ stringToFind: CFString!, _ rangeToSearch: CFRange, _ compareOptions: CFStringCompareFlags) -> CFArray!
```

#### Return Value

An array that contains pointers to [`CFRange`](cfrange.md) structures identifying the character locations of `stringToFind` in `theString`. Returns `NULL`, if no matching substring is found in the source object, or if there was a problem creating the array. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `alloc`: The allocator to use to allocate memory for the new CFArray object. Pass   or   to use the current default allocator.
- `theString`: The string in which to search for  .
- `stringToFind`: The string to search for in  .
- `rangeToSearch`: The range of characters within   to be searched. The specified range must not exceed the length of the string.
- `compareOptions`: Flags that select different types of comparisons, such as localized comparison, case-insensitive comparison, and non-literal comparison. If you want the default comparison behavior, pass  . See   for the available flags.

## See Also

- [func CFStringFind(CFString!, CFString!, CFStringCompareFlags) -> CFRange](cfstringfind(_:_:_:).md)
  Searches for a substring within a string and, if it is found, yields the range of the substring within the object’s characters.
- [func CFStringFindCharacterFromSet(CFString!, CFCharacterSet!, CFRange, CFStringCompareFlags, UnsafeMutablePointer<CFRange>!) -> Bool](cfstringfindcharacterfromset(_:_:_:_:_:).md)
  Query the range of the first character contained in the specified character set.
- [func CFStringFindWithOptions(CFString!, CFString!, CFRange, CFStringCompareFlags, UnsafeMutablePointer<CFRange>!) -> Bool](cfstringfindwithoptions(_:_:_:_:_:).md)
  Searches for a substring within a range of the characters represented by a string and, if the substring is found, returns its range within the object’s characters.
- [func CFStringFindWithOptionsAndLocale(CFString!, CFString!, CFRange, CFStringCompareFlags, CFLocale!, UnsafeMutablePointer<CFRange>!) -> Bool](cfstringfindwithoptionsandlocale(_:_:_:_:_:_:).md)
  Returns a Boolean value that indicates whether a given string was found in a given source string.
- [func CFStringGetLineBounds(CFString!, CFRange, UnsafeMutablePointer<CFIndex>!, UnsafeMutablePointer<CFIndex>!, UnsafeMutablePointer<CFIndex>!)](cfstringgetlinebounds(_:_:_:_:_:).md)
  Given a range of characters in a string, obtains the line bounds—that is, the indexes of the first character and the final characters of the lines containing the range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringcreatearraywithfindresults(_:_:_:_:_:))*