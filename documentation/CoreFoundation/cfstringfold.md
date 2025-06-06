# CFStringFold(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Folds a given string into the form specified by optional flags.

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
func CFStringFold(_ theString: CFMutableString!, _ theFlags: CFStringCompareFlags, _ theLocale: CFLocale!)
```

#### Discussion

Character foldings are operations that convert any of a set of characters sharing similar semantics into a single representative from that set.

You can use this function to preprocess strings that are to be compared, searched, or indexed. Note that folding does not include normalization, so you must use [`CFStringNormalize(_:_:)`](cfstringnormalize(_:_:).md) in addition to CFStringFold in order to obtain the effect of `kCFCompareNonliteral`.

## Parameters

- `theString`: The string which is to be folded.  If this parameter is not a valid mutable CFString, the behavior is undefined.
- `theFlags`: Folding with   removes case distinctions in accordance with the mapping specified by  .  Folding with   removes distinctions of accents and other diacritics.  Folding with   removes character width distinctions by mapping characters in the range   to their ordinary equivalents.
- `theLocale`: The locale argument affects the case mapping algorithm. For example, for the Turkish locale, case-insensitive compare matches “I” to “ı” (Unicode code point U+0131, Latin Small Dotless I), not the normal “i” character.

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
- [func CFStringCreateMutable(CFAllocator!, CFIndex) -> CFMutableString!](cfstringcreatemutable(_:_:).md)
  Creates an empty CFMutableString object.
- [func CFStringCreateMutableCopy(CFAllocator!, CFIndex, CFString!) -> CFMutableString!](cfstringcreatemutablecopy(_:_:_:).md)
  Creates a mutable copy of a string.
- [func CFStringCreateMutableWithExternalCharactersNoCopy(CFAllocator!, UnsafeMutablePointer<UniChar>!, CFIndex, CFIndex, CFAllocator!) -> CFMutableString!](cfstringcreatemutablewithexternalcharactersnocopy(_:_:_:_:_:).md)
  Creates a CFMutableString object whose Unicode character buffer is controlled externally.
- [func CFStringDelete(CFMutableString!, CFRange)](cfstringdelete(_:_:).md)
  Deletes a range of characters in a string.
- [func CFStringFindAndReplace(CFMutableString!, CFString!, CFString!, CFRange, CFStringCompareFlags) -> CFIndex](cfstringfindandreplace(_:_:_:_:_:).md)
  Replaces all occurrences of a substring within a given range.
- [func CFStringInsert(CFMutableString!, CFIndex, CFString!)](cfstringinsert(_:_:_:).md)
  Inserts a string at a specified location in the character buffer of a CFMutableString object.
- [func CFStringLowercase(CFMutableString!, CFLocale!)](cfstringlowercase(_:_:).md)
  Changes all uppercase alphabetical characters in a CFMutableString to lowercase.
- [func CFStringNormalize(CFMutableString!, CFStringNormalizationForm)](cfstringnormalize(_:_:).md)
  Normalizes the string into the specified form as described in Unicode Technical Report #15.
- [func CFStringPad(CFMutableString!, CFString!, CFIndex, CFIndex)](cfstringpad(_:_:_:_:).md)
  Enlarges a string, padding it with specified characters, or truncates the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringfold(_:_:_:))*