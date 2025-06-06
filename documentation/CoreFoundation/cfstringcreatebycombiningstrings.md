# CFStringCreateByCombiningStrings(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a single string from the individual CFString objects that comprise the elements of an array.

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
func CFStringCreateByCombiningStrings(_ alloc: CFAllocator!, _ theArray: CFArray!, _ separatorString: CFString!) -> CFString!
```

#### Return Value

A string that contains a concatenation of the strings in `theArray` separated by `separatorString`. The order of the substrings in the string is identical to the order of the elements in `theArray`.

#### Discussion

If `theArray` is empty, returns an empty CFString object; if `theArray` contains one CFString object, that object is returned (without the separator string). Returns `NULL` if there was a problem in creating the string. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

See also [`CFStringCreateArrayBySeparatingStrings(_:_:_:)`](cfstringcreatearraybyseparatingstrings(_:_:_:).md).

## Parameters

- `alloc`: The allocator to use to allocate memory for the new string. Pass   or   to use the current default allocator.
- `theArray`: An array of CFString objects to concatenate.  This value should not be  .
- `separatorString`: The string to insert between the substrings in the returned string. This value is commonly a whitespace character such as a tab or a newline (carriage return). If this value is not a valid CFString object, an assertion is raised.

## See Also

- [func CFStringCreateArrayBySeparatingStrings(CFAllocator!, CFString!, CFString!) -> CFArray!](cfstringcreatearraybyseparatingstrings(_:_:_:).md)
  Creates an array of CFString objects from a single CFString object.
- [func CFStringCreateCopy(CFAllocator!, CFString!) -> CFString!](cfstringcreatecopy(_:_:).md)
  Creates an immutable copy of a string.
- [func CFStringCreateFromExternalRepresentation(CFAllocator!, CFData!, CFStringEncoding) -> CFString!](cfstringcreatefromexternalrepresentation(_:_:_:).md)
  Creates a string from its “external representation.”
- [func CFStringCreateWithBytes(CFAllocator!, UnsafePointer<UInt8>!, CFIndex, CFStringEncoding, Bool) -> CFString!](cfstringcreatewithbytes(_:_:_:_:_:).md)
  Creates a string from a buffer containing characters in a specified encoding.
- [func CFStringCreateWithBytesNoCopy(CFAllocator!, UnsafePointer<UInt8>!, CFIndex, CFStringEncoding, Bool, CFAllocator!) -> CFString!](cfstringcreatewithbytesnocopy(_:_:_:_:_:_:).md)
  Creates a string from a buffer, containing characters in a specified encoding, that might serve as the backing store for the new string.
- [func CFStringCreateWithCharacters(CFAllocator!, UnsafePointer<UniChar>!, CFIndex) -> CFString!](cfstringcreatewithcharacters(_:_:_:).md)
  Creates a string from a buffer of Unicode characters.
- [func CFStringCreateWithCharactersNoCopy(CFAllocator!, UnsafePointer<UniChar>!, CFIndex, CFAllocator!) -> CFString!](cfstringcreatewithcharactersnocopy(_:_:_:_:).md)
  Creates a string from a buffer of Unicode characters that might serve as the backing store for the object.
- [func CFStringCreateWithCString(CFAllocator!, UnsafePointer<CChar>!, CFStringEncoding) -> CFString!](cfstringcreatewithcstring(_:_:_:).md)
  Creates an immutable string from a C string.
- [func CFStringCreateWithCStringNoCopy(CFAllocator!, UnsafePointer<CChar>!, CFStringEncoding, CFAllocator!) -> CFString!](cfstringcreatewithcstringnocopy(_:_:_:_:).md)
  Creates a CFString object from an external C string buffer that might serve as the backing store for the object.
- [func CFStringCreateWithFormatAndArguments(CFAllocator!, CFDictionary!, CFString!, CVaListPointer) -> CFString!](cfstringcreatewithformatandarguments(_:_:_:_:).md)
  Creates an immutable string from a formatted string and a variable number of arguments (specified in a parameter of type `va_list`).
- [func CFStringCreateWithPascalString(CFAllocator!, ConstStr255Param!, CFStringEncoding) -> CFString!](cfstringcreatewithpascalstring(_:_:_:).md)
  Creates an immutable CFString object from a Pascal string.
- [func CFStringCreateWithPascalStringNoCopy(CFAllocator!, ConstStr255Param!, CFStringEncoding, CFAllocator!) -> CFString!](cfstringcreatewithpascalstringnocopy(_:_:_:_:).md)
  Creates a CFString object from an external Pascal string buffer that might serve as the backing store for the object.
- [func CFStringCreateWithSubstring(CFAllocator!, CFString!, CFRange) -> CFString!](cfstringcreatewithsubstring(_:_:_:).md)
  Creates an immutable string from a segment (substring) of an existing string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringcreatebycombiningstrings(_:_:_:))*