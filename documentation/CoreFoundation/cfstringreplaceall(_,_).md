# CFStringReplaceAll(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Replaces all characters of a CFMutableString object with other characters.

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
func CFStringReplaceAll(_ theString: CFMutableString!, _ replacement: CFString!)
```

```c
extern void CFStringReplaceAll(CFMutableStringRef theString, CFStringRef replacement);
```

#### Discussion

The character buffer of `theString` is resized according to the length of the new characters.

## Parameters

- `theString`: The string to modify. If this value is not a CFMutableString object, an assertion is raised.
- `replacement`: The replacement string to put into `theString`.

## See Also

### CFMutableString Miscellaneous Functions
- [func CFStringAppend(CFMutableString!, CFString!)](./cfstringappend%28_,_%29.md)
  Appends the characters of a string to those of a CFMutableString object.
- [func CFStringAppendCharacters(CFMutableString!, UnsafePointer<UniChar>!, CFIndex)](./cfstringappendcharacters%28_,_,_%29.md)
  Appends a buffer of Unicode characters to the character contents of a CFMutableString object.
- [func CFStringAppendCString(CFMutableString!, UnsafePointer<CChar>!, CFStringEncoding)](./cfstringappendcstring%28_,_,_%29.md)
  Appends a C string to the character contents of a CFMutableString object.
- [func CFStringAppendFormatAndArguments(CFMutableString!, CFDictionary!, CFString!, CVaListPointer)](./cfstringappendformatandarguments%28_,_,_,_%29.md)
  Appends a formatted string to the character contents of a CFMutableString object.
- [func CFStringAppendPascalString(CFMutableString!, ConstStr255Param!, CFStringEncoding)](./cfstringappendpascalstring%28_,_,_%29.md)
  Appends a Pascal string to the character contents of a CFMutableString object.
- [func CFStringCapitalize(CFMutableString!, CFLocale!)](./cfstringcapitalize%28_,_%29.md)
  Changes the first character in each word of a string to uppercase (if it is a lowercase alphabetical character).
- [func CFStringCreateMutable(CFAllocator!, CFIndex) -> CFMutableString!](./cfstringcreatemutable%28_,_%29.md)
  Creates an empty CFMutableString object.
- [func CFStringCreateMutableCopy(CFAllocator!, CFIndex, CFString!) -> CFMutableString!](./cfstringcreatemutablecopy%28_,_,_%29.md)
  Creates a mutable copy of a string.
- [func CFStringCreateMutableWithExternalCharactersNoCopy(CFAllocator!, UnsafeMutablePointer<UniChar>!, CFIndex, CFIndex, CFAllocator!) -> CFMutableString!](./cfstringcreatemutablewithexternalcharactersnocopy%28_,_,_,_,_%29.md)
  Creates a CFMutableString object whose Unicode character buffer is controlled externally.
- [func CFStringDelete(CFMutableString!, CFRange)](./cfstringdelete%28_,_%29.md)
  Deletes a range of characters in a string.
- [func CFStringFindAndReplace(CFMutableString!, CFString!, CFString!, CFRange, CFStringCompareFlags) -> CFIndex](./cfstringfindandreplace%28_,_,_,_,_%29.md)
  Replaces all occurrences of a substring within a given range.
- [func CFStringFold(CFMutableString!, CFStringCompareFlags, CFLocale!)](./cfstringfold%28_,_,_%29.md)
  Folds a given string into the form specified by optional flags.
- [func CFStringInsert(CFMutableString!, CFIndex, CFString!)](./cfstringinsert%28_,_,_%29.md)
  Inserts a string at a specified location in the character buffer of a CFMutableString object.
- [func CFStringLowercase(CFMutableString!, CFLocale!)](./cfstringlowercase%28_,_%29.md)
  Changes all uppercase alphabetical characters in a CFMutableString to lowercase.
- [func CFStringNormalize(CFMutableString!, CFStringNormalizationForm)](./cfstringnormalize%28_,_%29.md)
  Normalizes the string into the specified form as described in Unicode Technical Report #15.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringreplaceall(_:_:))*