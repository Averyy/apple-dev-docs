# CFStringGetCharacters(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Copies a range of the Unicode characters from a string to a user-provided buffer.

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
func CFStringGetCharacters(_ theString: CFString!, _ range: CFRange, _ buffer: UnsafeMutablePointer<UniChar>!)
```

#### Discussion

Use this function to obtain some or all of the Unicode characters represented by a CFString object. If this operation involves a large number of characters, the function call can be expensive in terms of memory. Instead you might want to consider using the in-line buffer functions [`CFStringInitInlineBuffer(_:_:_:)`](cfstringinitinlinebuffer(_:_:_:).md) and [`CFStringGetCharacterFromInlineBuffer(_:_:)`](cfstringgetcharacterfrominlinebuffer(_:_:).md) to extract the characters incrementally.

## Parameters

- `theString`: The string from which the characters are to be obtained.
- `range`: The range of characters to copy. The specified range must not exceed the length of the string.
- `buffer`: The   buffer of length   that you have allocated on the stack or heap. On return, the buffer contains the requested Unicode characters.

## See Also

- [func CFStringCreateExternalRepresentation(CFAllocator!, CFString!, CFStringEncoding, UInt8) -> CFData!](cfstringcreateexternalrepresentation(_:_:_:_:).md)
  Creates an “external representation” of a CFString object, that is, a CFData object.
- [func CFStringGetBytes(CFString!, CFRange, CFStringEncoding, UInt8, Bool, UnsafeMutablePointer<UInt8>!, CFIndex, UnsafeMutablePointer<CFIndex>!) -> CFIndex](cfstringgetbytes(_:_:_:_:_:_:_:_:).md)
  Fetches a range of the characters from a string into a byte buffer after converting the characters to a specified encoding.
- [func CFStringGetCharacterAtIndex(CFString!, CFIndex) -> UniChar](cfstringgetcharacteratindex(_:_:).md)
  Returns the Unicode character at a specified location in a string.
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
- [func CFStringInitInlineBuffer(CFString!, UnsafeMutablePointer<CFStringInlineBuffer>!, CFRange)](cfstringinitinlinebuffer(_:_:_:).md)
  Initializes an in-line buffer to use for efficient access of a CFString object’s characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringgetcharacters(_:_:_:))*