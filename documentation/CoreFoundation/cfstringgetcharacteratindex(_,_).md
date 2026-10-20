# CFStringGetCharacterAtIndex(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the Unicode character at a specified location in a string.

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
func CFStringGetCharacterAtIndex(_ theString: CFString!, _ idx: CFIndex) -> UniChar
```

```c
extern UniChar CFStringGetCharacterAtIndex(CFStringRef theString, CFIndex idx);
```

#### Return Value

A Unicode character.

#### Discussion

This function is typically called in a loop to fetch the Unicode characters of a string in sequence or to fetch a character at a known position (first or last, for example). Using it in a loop can be inefficient, especially with longer strings, so consider the [`CFStringGetCharacters(_:_:_:)`](./cfstringgetcharacters%28_,_,_%29.md) function or the in-line buffer functions ([`CFStringInitInlineBuffer(_:_:_:)`](./cfstringinitinlinebuffer%28_,_,_%29.md) and [`CFStringGetCharacterFromInlineBuffer(_:_:)`](./cfstringgetcharacterfrominlinebuffer%28_,_%29.md)) as alternatives.

## Parameters

- `theString`: The string from which the Unicode character is obtained.
- `idx`: The position of the Unicode character in the CFString.

## See Also

### Accessing Characters
- [func CFStringCreateExternalRepresentation(CFAllocator!, CFString!, CFStringEncoding, UInt8) -> CFData!](./cfstringcreateexternalrepresentation%28_,_,_,_%29.md)
  Creates an “external representation” of a CFString object, that is, a CFData object.
- [func CFStringGetBytes(CFString!, CFRange, CFStringEncoding, UInt8, Bool, UnsafeMutablePointer<UInt8>!, CFIndex, UnsafeMutablePointer<CFIndex>!) -> CFIndex](./cfstringgetbytes%28_,_,_,_,_,_,_,_%29.md)
  Fetches a range of the characters from a string into a byte buffer after converting the characters to a specified encoding.
- [func CFStringGetCharacters(CFString!, CFRange, UnsafeMutablePointer<UniChar>!)](./cfstringgetcharacters%28_,_,_%29.md)
  Copies a range of the Unicode characters from a string to a user-provided buffer.
- [func CFStringGetCharactersPtr(CFString!) -> UnsafePointer<UniChar>!](./cfstringgetcharactersptr%28_%29.md)
  Quickly obtains a pointer to the contents of a string as a buffer of Unicode characters.
- [func CFStringGetCharacterFromInlineBuffer(UnsafeMutablePointer<CFStringInlineBuffer>!, CFIndex) -> UniChar](./cfstringgetcharacterfrominlinebuffer%28_,_%29.md)
  Returns the Unicode character at a specific location in an in-line buffer.
- [func CFStringGetCString(CFString!, UnsafeMutablePointer<CChar>!, CFIndex, CFStringEncoding) -> Bool](./cfstringgetcstring%28_,_,_,_%29.md)
  Copies the character contents of a string to a local C string buffer after converting the characters to a given encoding.
- [func CFStringGetCStringPtr(CFString!, CFStringEncoding) -> UnsafePointer<CChar>!](./cfstringgetcstringptr%28_,_%29.md)
  Quickly obtains a pointer to a C-string buffer containing the characters of a string in a given encoding.
- [func CFStringGetLength(CFString!) -> CFIndex](./cfstringgetlength%28_%29.md)
  Returns the number (in terms of UTF-16 code pairs) of Unicode characters in a string.
- [func CFStringGetPascalString(CFString!, StringPtr!, CFIndex, CFStringEncoding) -> Bool](./cfstringgetpascalstring%28_,_,_,_%29.md)
  Copies the character contents of a CFString object to a local Pascal string buffer after converting the characters to a requested encoding.
- [func CFStringGetPascalStringPtr(CFString!, CFStringEncoding) -> ConstStringPtr!](./cfstringgetpascalstringptr%28_,_%29.md)
  Quickly obtains a pointer to a Pascal buffer containing the characters of a string in a given encoding.
- [func CFStringGetRangeOfComposedCharactersAtIndex(CFString!, CFIndex) -> CFRange](./cfstringgetrangeofcomposedcharactersatindex%28_,_%29.md)
  Returns the range of the composed character sequence at a specified index.
- [func CFStringInitInlineBuffer(CFString!, UnsafeMutablePointer<CFStringInlineBuffer>!, CFRange)](./cfstringinitinlinebuffer%28_,_,_%29.md)
  Initializes an in-line buffer to use for efficient access of a CFString object’s characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringgetcharacteratindex(_:_:))*