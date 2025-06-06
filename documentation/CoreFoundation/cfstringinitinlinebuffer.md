# CFStringInitInlineBuffer(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Initializes an in-line buffer to use for efficient access of a CFString object’s characters.

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
func CFStringInitInlineBuffer(_ str: CFString!, _ buf: UnsafeMutablePointer<CFStringInlineBuffer>!, _ range: CFRange)
```

#### Discussion

This function initializes an [`CFStringInlineBuffer`](cfstringinlinebuffer.md) structure that can be used for accessing the characters of a string. Once the buffer is initialized you can call the [`CFStringGetCharacterFromInlineBuffer(_:_:)`](cfstringgetcharacterfrominlinebuffer(_:_:).md) function to access the characters in the buffer one at a time. The in-line buffer functions, along with the [`CFStringInlineBuffer`](cfstringinlinebuffer.md) structure, give you fast access to the characters of a string. The technique for in-line buffer access combines the convenience of one-at-a-time character access with the efficiency of bulk access.

## Parameters

- `str`: The string to copy to the in-line buffer.
- `buf`: The (uninitialized)   structure to initialize. On return, an initialized structure that can be used in a   function call. Typically this buffer is allocated on the stack.
- `range`: The range of characters in   to copy to  . The specified range must not exceed the length of the string.

## See Also

- [func CFStringCreateExternalRepresentation(CFAllocator!, CFString!, CFStringEncoding, UInt8) -> CFData!](cfstringcreateexternalrepresentation(_:_:_:_:).md)
  Creates an “external representation” of a CFString object, that is, a CFData object.
- [func CFStringGetBytes(CFString!, CFRange, CFStringEncoding, UInt8, Bool, UnsafeMutablePointer<UInt8>!, CFIndex, UnsafeMutablePointer<CFIndex>!) -> CFIndex](cfstringgetbytes(_:_:_:_:_:_:_:_:).md)
  Fetches a range of the characters from a string into a byte buffer after converting the characters to a specified encoding.
- [func CFStringGetCharacterAtIndex(CFString!, CFIndex) -> UniChar](cfstringgetcharacteratindex(_:_:).md)
  Returns the Unicode character at a specified location in a string.
- [func CFStringGetCharacters(CFString!, CFRange, UnsafeMutablePointer<UniChar>!)](cfstringgetcharacters(_:_:_:).md)
  Copies a range of the Unicode characters from a string to a user-provided buffer.
- [func CFStringGetCharactersPtr(CFString!) -> UnsafePointer<UniChar>!](cfstringgetcharactersptr(_:).md)
  Quickly obtains a pointer to the contents of a string as a buffer of Unicode characters.
- [func CFStringGetCharacterFromInlineBuffer(UnsafeMutablePointer<CFStringInlineBuffer>!, CFIndex) -> UniChar](cfstringgetcharacterfrominlinebuffer(_:_:).md)
  Returns the Unicode character at a specific location in an in-line buffer.
- [func CFStringGetCString(CFString!, UnsafeMutablePointer<CChar>!, CFIndex, CFStringEncoding) -> Bool](cfstringgetcstring(_:_:_:_:).md)
  Copies the character contents of a string to a local C string buffer after converting the characters to a given encoding.
- [func CFStringGetCStringPtr(CFString!, CFStringEncoding) -> UnsafePointer<CChar>!](cfstringgetcstringptr(_:_:).md)
  Quickly obtains a pointer to a C-string buffer containing the characters of a string in a given encoding.
- [func CFStringGetLength(CFString!) -> CFIndex](cfstringgetlength(_:).md)
  Returns the number (in terms of UTF-16 code pairs) of Unicode characters in a string.
- [func CFStringGetPascalString(CFString!, StringPtr!, CFIndex, CFStringEncoding) -> Bool](cfstringgetpascalstring(_:_:_:_:).md)
  Copies the character contents of a CFString object to a local Pascal string buffer after converting the characters to a requested encoding.
- [func CFStringGetPascalStringPtr(CFString!, CFStringEncoding) -> ConstStringPtr!](cfstringgetpascalstringptr(_:_:).md)
  Quickly obtains a pointer to a Pascal buffer containing the characters of a string in a given encoding.
- [func CFStringGetRangeOfComposedCharactersAtIndex(CFString!, CFIndex) -> CFRange](cfstringgetrangeofcomposedcharactersatindex(_:_:).md)
  Returns the range of the composed character sequence at a specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringinitinlinebuffer(_:_:_:))*