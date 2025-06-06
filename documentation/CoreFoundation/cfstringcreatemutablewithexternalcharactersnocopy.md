# CFStringCreateMutableWithExternalCharactersNoCopy(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a CFMutableString object whose Unicode character buffer is controlled externally.

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
func CFStringCreateMutableWithExternalCharactersNoCopy(_ alloc: CFAllocator!, _ chars: UnsafeMutablePointer<UniChar>!, _ numChars: CFIndex, _ capacity: CFIndex, _ externalCharactersAllocator: CFAllocator!) -> CFMutableString!
```

#### Return Value

A new mutable string, or `NULL` if there was a problem creating the object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

This function permits you to create a `CFMutableString` object whose backing store is an external Unicode character buffer—that is, a buffer that you control (or can control) entirely. This function allows you to take advantage of the features of `CFString`, particularly the `CFMutableString` functions that add and modify character data. But at the same time you can directly add, delete, modify, and examine the characters in the buffer. You can even replace the buffer entirely. If, however, you directly modify or replace the character buffer, you should inform the `CFString` object of this change with the [`CFStringSetExternalCharactersNoCopy(_:_:_:_:)`](cfstringsetexternalcharactersnocopy(_:_:_:_:).md) function.

If you mutate the character contents with the `CFString` functions, and the buffer needs to be enlarged, the `CFString` object calls the allocation callbacks specified for the allocator `externalCharactersAllocator`,  or

the default allocator

if `kCFAllocatorNull` is specified.

This function should be used in special circumstances where you want to create a `CFString` wrapper around an existing, potentially large `UniChar` buffer you own. Using this function causes the `CFString` object to forgo some of its internal optimizations, so it should be avoided in general use. That is, if you want to create a `CFString` object from a small `UniChar` buffer, and you don’t need to continue owning the buffer, use one of the other creation functions (for instance [`CFStringCreateWithCharacters(_:_:_:)`](cfstringcreatewithcharacters(_:_:_:).md)) instead.

## Parameters

- `alloc`: The allocator to use to allocate memory for the string. Pass   or   to use the current default allocator.
- `chars`: The Unicode character buffer for the new  . Before calling, create this buffer on the stack or heap and optionally initialize it with Unicode character data. Upon return, the created   object keeps its own copy of the pointer to this buffer. You may pass in   if there is no initial buffer being provided.
- `numChars`: The number of characters initially in the Unicode buffer pointed to by  .
- `capacity`: The capacity of the external buffer ( ); that is, the maximum number of Unicode characters that can be stored. This value should be   if no initial buffer is provided.
- `externalCharactersAllocator`: .

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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringcreatemutablewithexternalcharactersnocopy(_:_:_:_:_:))*