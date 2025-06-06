# CFMutableString

**Framework**: Core Foundation  
**Kind**: class

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
class CFMutableString
```

#### Overview

CFMutableString manages dynamic strings. The basic interface for managing strings is provided by [`CFString`](cfstring.md). CFMutableString adds functions to modify the contents of a string.

CFMutableString is “toll-free bridged” with its Cocoa Foundation counterpart, [`NSMutableString`](https://developer.apple.com/documentation/Foundation/NSMutableString). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSMutableString *` parameter, you can pass in a `CFMutableStringRef`, and in a function where you see a `CFMutableStringRef` parameter, you can pass in an NSMutableString instance. This also applies to concrete subclasses of NSMutableString. See [`Toll-Free Bridged Types`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Topics

### CFMutableString Miscellaneous Functions
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
- [func CFStringReplace(CFMutableString!, CFRange, CFString!)](cfstringreplace(_:_:_:).md)
  Replaces part of the character contents of a CFMutableString object with another string.
- [func CFStringReplaceAll(CFMutableString!, CFString!)](cfstringreplaceall(_:_:).md)
  Replaces all characters of a CFMutableString object with other characters.
- [func CFStringSetExternalCharactersNoCopy(CFMutableString!, UnsafeMutablePointer<UniChar>!, CFIndex, CFIndex)](cfstringsetexternalcharactersnocopy(_:_:_:_:).md)
  Notifies a CFMutableString object that its external backing store of Unicode characters has changed.
- [func CFStringTransform(CFMutableString!, UnsafeMutablePointer<CFRange>!, CFString!, Bool) -> Bool](cfstringtransform(_:_:_:_:).md)
  Perform in-place transliteration on a mutable string.
- [func CFStringTrim(CFMutableString!, CFString!)](cfstringtrim(_:_:).md)
  Trims a specified substring from the beginning and end of a CFMutableString object.
- [func CFStringTrimWhitespace(CFMutableString!)](cfstringtrimwhitespace(_:).md)
  Trims whitespace from the beginning and end of a CFMutableString object.
- [func CFStringUppercase(CFMutableString!, CFLocale!)](cfstringuppercase(_:_:).md)
  Changes all lowercase alphabetical characters in a CFMutableString object to uppercase.
### Constants
- [enum CFStringNormalizationForm](cfstringnormalizationform.md)
  Unicode normalization forms as described in Unicode Technical Report #15.
- [Transform Identifiers for CFStringTransform](transform-identifiers-for-cfstringtransform.md)
  Constants that identify transforms used with [`CFStringTransform(_:_:_:_:)`](cfstringtransform(_:_:_:_:).md).

## Relationships

### Inherits From
- [CFString](cfstring.md)
### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Property List Programming Topics for Core Foundation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/CFPropertyLists.html#//apple_ref/doc/uid/10000130i)
- [String Programming Guide for Core Foundation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/introCFStrings.html#//apple_ref/doc/uid/10000131i)
- [class CFAllocator](cfallocator.md)
- [class CFArray](cfarray.md)
- [class CFAttributedString](cfattributedstring.md)
- [class CFBag](cfbag.md)
- [class CFBinaryHeap](cfbinaryheap.md)
- [class CFBitVector](cfbitvector.md)
- [class CFBoolean](cfboolean.md)
- [class CFBundle](cfbundle.md)
- [class CFCalendar](cfcalendar.md)
- [class CFCharacterSet](cfcharacterset.md)
- [class CFData](cfdata.md)
- [class CFDate](cfdate.md)
- [class CFDateFormatter](cfdateformatter.md)
- [class CFDictionary](cfdictionary.md)
- [class CFError](cferror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmutablestring)*