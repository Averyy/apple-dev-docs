# CFStringCreateCopy(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates an immutable copy of a string.

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
func CFStringCreateCopy(_ alloc: CFAllocator!, _ theString: CFString!) -> CFString!
```

```c
extern CFStringRefCFStringCreateCopy(CFAllocatorRef alloc, CFStringRef theString);
```

## Return Value

An immutable string whose contents are identical to `theString`. Returns `NULL` if there was a problem copying the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

The resulting object has the same Unicode contents as the original object, but it is always immutable. It might also have different storage characteristics, and hence might reply differently to functions such as [`CFStringGetCStringPtr(_:_:)`](./cfstringgetcstringptr%28_,_%29.md). Also, if the specified allocator and the allocator of the original object are the same, and the string is already immutable, this function may simply increment the retention count without making a true copy. However, the resulting object is a true immutable copy, except the operation was a lot more efficient.

You should use this function in situations where a string is or could be mutable, and you need to take a snapshot of its current value. For example, you might decide to pass a copy of a string to a function that stores its current value in a list for later use.

## Parameters

- `alloc`: The allocator to use to allocate memory for the new string. Pass `NULL` or [`kCFAllocatorDefault`](./kcfallocatordefault.md) to use the current default allocator.
- `theString`: The string to copy.

## See Also

### Creating a CFString
- [func CFStringCreateArrayBySeparatingStrings(CFAllocator!, CFString!, CFString!) -> CFArray!](./cfstringcreatearraybyseparatingstrings%28_,_,_%29.md)
  Creates an array of CFString objects from a single CFString object.
- [func CFStringCreateByCombiningStrings(CFAllocator!, CFArray!, CFString!) -> CFString!](./cfstringcreatebycombiningstrings%28_,_,_%29.md)
  Creates a single string from the individual CFString objects that comprise the elements of an array.
- [func CFStringCreateFromExternalRepresentation(CFAllocator!, CFData!, CFStringEncoding) -> CFString!](./cfstringcreatefromexternalrepresentation%28_,_,_%29.md)
  Creates a string from its “external representation.”
- [func CFStringCreateWithBytes(CFAllocator!, UnsafePointer<UInt8>!, CFIndex, CFStringEncoding, Bool) -> CFString!](./cfstringcreatewithbytes%28_,_,_,_,_%29.md)
  Creates a string from a buffer containing characters in a specified encoding.
- [func CFStringCreateWithBytesNoCopy(CFAllocator!, UnsafePointer<UInt8>!, CFIndex, CFStringEncoding, Bool, CFAllocator!) -> CFString!](./cfstringcreatewithbytesnocopy%28_,_,_,_,_,_%29.md)
  Creates a string from a buffer, containing characters in a specified encoding, that might serve as the backing store for the new string.
- [func CFStringCreateWithCharacters(CFAllocator!, UnsafePointer<UniChar>!, CFIndex) -> CFString!](./cfstringcreatewithcharacters%28_,_,_%29.md)
  Creates a string from a buffer of Unicode characters.
- [func CFStringCreateWithCharactersNoCopy(CFAllocator!, UnsafePointer<UniChar>!, CFIndex, CFAllocator!) -> CFString!](./cfstringcreatewithcharactersnocopy%28_,_,_,_%29.md)
  Creates a string from a buffer of Unicode characters that might serve as the backing store for the object.
- [func CFStringCreateWithCString(CFAllocator!, UnsafePointer<CChar>!, CFStringEncoding) -> CFString!](./cfstringcreatewithcstring%28_,_,_%29.md)
  Creates an immutable string from a C string.
- [func CFStringCreateWithCStringNoCopy(CFAllocator!, UnsafePointer<CChar>!, CFStringEncoding, CFAllocator!) -> CFString!](./cfstringcreatewithcstringnocopy%28_,_,_,_%29.md)
  Creates a CFString object from an external C string buffer that might serve as the backing store for the object.
- [func CFStringCreateWithFormatAndArguments(CFAllocator!, CFDictionary!, CFString!, CVaListPointer) -> CFString!](./cfstringcreatewithformatandarguments%28_,_,_,_%29.md)
  Creates an immutable string from a formatted string and a variable number of arguments (specified in a parameter of type `va_list`).
- [func CFStringCreateWithPascalString(CFAllocator!, ConstStr255Param!, CFStringEncoding) -> CFString!](./cfstringcreatewithpascalstring%28_,_,_%29.md)
  Creates an immutable CFString object from a Pascal string.
- [func CFStringCreateWithPascalStringNoCopy(CFAllocator!, ConstStr255Param!, CFStringEncoding, CFAllocator!) -> CFString!](./cfstringcreatewithpascalstringnocopy%28_,_,_,_%29.md)
  Creates a CFString object from an external Pascal string buffer that might serve as the backing store for the object.
- [func CFStringCreateWithSubstring(CFAllocator!, CFString!, CFRange) -> CFString!](./cfstringcreatewithsubstring%28_,_,_%29.md)
  Creates an immutable string from a segment (substring) of an existing string.
- [CFSTR](./cfstr.md)
  Creates an immutable string from a constant compile-time string.
- [CFStringCreateWithFormat](./cfstringcreatewithformat.md)
  Creates an immutable string from a formatted string and a variable number of arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringcreatecopy(_:_:))*