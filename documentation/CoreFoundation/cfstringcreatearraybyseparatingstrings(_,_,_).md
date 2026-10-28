# CFStringCreateArrayBySeparatingStrings(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates an array of CFString objects from a single CFString object.

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
func CFStringCreateArrayBySeparatingStrings(_ alloc: CFAllocator!, _ theString: CFString!, _ separatorString: CFString!) -> CFArray!
```

```c
extern CFArrayRefCFStringCreateArrayBySeparatingStrings(CFAllocatorRef alloc, CFStringRef theString, CFStringRef separatorString);
```

## Return Value

A new array that contains CFString objects that represent substrings of `theString`, or `NULL` if there was a problem creating the object. The order of elements in the array is identical to the order of the substrings in `theString`. If `separatorString` does not occur in `theString`, the result is an array containing `theString`. If `separatorString` is equal to `theString`, then the result is an array containing two empty strings. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

This function provides a convenient way to convert units of data captured in a single string to a form (an array) suitable for iterative processing. One or more delimiter characters (or “separator string”) separates the substrings in the source string—these characters are frequently whitespace characters such as tabs and newlines (carriage returns). For example, you might have a file containing a localized list of place names with each name separated by a tab character. You could create a CFString object from this file and call this function on the string to obtain a CFArray object whose elements are these place names.

`separatorString` is treated as a complete unit. If you specify `XYZ` as the separator string, then if `theString` is `aXbYZcXYZe`, then the returned array contains `aXbYZc` and `e`.

See also [`CFStringCreateByCombiningStrings(_:_:_:)`](./cfstringcreatebycombiningstrings%28_,_,_%29.md).

## Parameters

- `alloc`: The allocator to use to allocate memory for the new CFArray object. Pass `NULL` or [`kCFAllocatorDefault`](./kcfallocatordefault.md) to use the current default allocator.
- `theString`: The string to be divided into substrings. The substrings should be separated by `separatorString`.
- `separatorString`: The string used to separate the substrings in `theString`.

## See Also

### Creating a CFString
- [func CFStringCreateByCombiningStrings(CFAllocator!, CFArray!, CFString!) -> CFString!](./cfstringcreatebycombiningstrings%28_,_,_%29.md)
  Creates a single string from the individual CFString objects that comprise the elements of an array.
- [func CFStringCreateCopy(CFAllocator!, CFString!) -> CFString!](./cfstringcreatecopy%28_,_%29.md)
  Creates an immutable copy of a string.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringcreatearraybyseparatingstrings(_:_:_:))*