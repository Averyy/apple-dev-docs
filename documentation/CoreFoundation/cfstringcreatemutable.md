# CFStringCreateMutable(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates an empty CFMutableString object.

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
func CFStringCreateMutable(_ alloc: CFAllocator!, _ maxLength: CFIndex) -> CFMutableString!
```

#### Return Value

A new empty CFMutableString object or `NULL` if there was a problem creating the object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

This function creates an empty (that is, content-less) CFMutableString object. You can add character data to this object with any of the `CFStringAppend...` functions, and thereafter you can insert, delete, replace, pad, and trim characters with the appropriate CFString functions. If the `maxLength` parameter is greater than `0`, any attempt to add characters beyond this limit results in a run-time error.

## Parameters

- `alloc`: The allocator to use to allocate memory for the new string. Pass   or kCFAllocatorDefault to use the current default allocator.
- `maxLength`: The maximum number of Unicode characters that can be stored by the returned string. Pass   if there should be no character limit. Note that initially the string still has a length of  ; this parameter simply specifies what the maximum size is. CFMutableString might try to optimize its internal storage by paying attention to this value.

## See Also

- [func CFStringAppend(CFMutableString!, CFString!)](cfstringappend(_:_:).md)
  Appends the characters of a string to those of a CFMutableString object.
- [func CFStringAppendCharacters(CFMutableString!, UnsafePointer<UniChar>!, CFIndex)](cfstringappendcharacters(_:_:_:).md)
  Appends a buffer of Unicode characters to the character contents of a CFMutableString object.
- [func CFStringAppendCString(CFMutableString!, UnsafePointer<CChar>!, CFStringEncoding)](cfstringappendcstring(_:_:_:).md)
  Appends a C string to the character contents of a CFMutableString object.
- [func CFStringAppendFormatAndArguments(CFMutableString!, CFDictionary!, CFString!, CVaListPointer)](cfstringappendformatandarguments(_:_:_:_:).md)
  Appends a formatted string to the character contents of a CFMutableString object.
- [func CFStringAppendPascalString(CFMutableString!, ConstStr255Param!, CFStringEncoding)](cfstringappendpascalstring(_:_:_:).md)
  Appends a Pascal string to the character contents of a CFMutableString object.
- [func CFStringCapitalize(CFMutableString!, CFLocale!)](cfstringcapitalize(_:_:).md)
  Changes the first character in each word of a string to uppercase (if it is a lowercase alphabetical character).
- [func CFStringCreateMutableCopy(CFAllocator!, CFIndex, CFString!) -> CFMutableString!](cfstringcreatemutablecopy(_:_:_:).md)
  Creates a mutable copy of a string.
- [func CFStringCreateMutableWithExternalCharactersNoCopy(CFAllocator!, UnsafeMutablePointer<UniChar>!, CFIndex, CFIndex, CFAllocator!) -> CFMutableString!](cfstringcreatemutablewithexternalcharactersnocopy(_:_:_:_:_:).md)
  Creates a CFMutableString object whose Unicode character buffer is controlled externally.
- [func CFStringDelete(CFMutableString!, CFRange)](cfstringdelete(_:_:).md)
  Deletes a range of characters in a string.
- [func CFStringFindAndReplace(CFMutableString!, CFString!, CFString!, CFRange, CFStringCompareFlags) -> CFIndex](cfstringfindandreplace(_:_:_:_:_:).md)
  Replaces all occurrences of a substring within a given range.
- [func CFStringFold(CFMutableString!, CFStringCompareFlags, CFLocale!)](cfstringfold(_:_:_:).md)
  Folds a given string into the form specified by optional flags.
- [func CFStringInsert(CFMutableString!, CFIndex, CFString!)](cfstringinsert(_:_:_:).md)
  Inserts a string at a specified location in the character buffer of a CFMutableString object.
- [func CFStringLowercase(CFMutableString!, CFLocale!)](cfstringlowercase(_:_:).md)
  Changes all uppercase alphabetical characters in a CFMutableString to lowercase.
- [func CFStringNormalize(CFMutableString!, CFStringNormalizationForm)](cfstringnormalize(_:_:).md)
  Normalizes the string into the specified form as described in Unicode Technical Report #15.
- [func CFStringPad(CFMutableString!, CFString!, CFIndex, CFIndex)](cfstringpad(_:_:_:_:).md)
  Enlarges a string, padding it with specified characters, or truncates the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringcreatemutable(_:_:))*