# CFStringCreateWithCharactersNoCopy(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a string from a buffer of Unicode characters that might serve as the backing store for the object.

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
func CFStringCreateWithCharactersNoCopy(_ alloc: CFAllocator!, _ chars: UnsafePointer<UniChar>!, _ numChars: CFIndex, _ contentsDeallocator: CFAllocator!) -> CFString!
```

#### Return Value

An immutable string containing `chars`, or `NULL` if there was a problem creating the object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

Unless the situation warrants otherwise, the returned object does not copy the external buffer to internal storage but instead uses the buffer as its backing store. However, you should never count on the object using the external buffer since it could copy the buffer to internal storage or might even dump the buffer altogether and use alternative means for storing the characters.

The function includes a `contentsDeallocator` parameter with which to specify an allocator to use for deallocating the external buffer when the string is deallocated. If you want to assume responsibility for deallocating this memory, specify [`kCFAllocatorNull`](kcfallocatornull.md) for this parameter.

If at creation time CFString decides it can’t use the buffer, and there is a `contentsDeallocator`, it will use this allocator to free the buffer at that time.

##### Special Considerations

If an error occurs during the creation of the string, then `chars` is not deallocated. In this case, the caller is responsible for freeing the buffer. This allows the caller to continue trying to create a string with the buffer, without having the buffer deallocated.

## Parameters

- `alloc`: The allocator to use to allocate memory for the new string. Pass   or   to use the current default allocator.
- `chars`: The Unicode buffer that has been allocated and initialized with Unicode characters.
- `numChars`: The number of characters in the buffer pointed to by  . Only this number of characters will be copied to internal storage.
- `contentsDeallocator`: The allocator to use to deallocate the external buffer when it is no longer needed. You can pass   or   to request the default allocator for this purpose. If the buffer does not need to be deallocated, or if you want to assume responsibility for deallocating the buffer (and not have the string deallocate it), pass  .

## See Also

- [func CFStringCreateArrayBySeparatingStrings(CFAllocator!, CFString!, CFString!) -> CFArray!](cfstringcreatearraybyseparatingstrings(_:_:_:).md)
  Creates an array of CFString objects from a single CFString object.
- [func CFStringCreateByCombiningStrings(CFAllocator!, CFArray!, CFString!) -> CFString!](cfstringcreatebycombiningstrings(_:_:_:).md)
  Creates a single string from the individual CFString objects that comprise the elements of an array.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringcreatewithcharactersnocopy(_:_:_:_:))*