# CFStringCreateWithFileSystemRepresentation(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a CFString from a zero-terminated POSIX file system representation.

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
func CFStringCreateWithFileSystemRepresentation(_ alloc: CFAllocator!, _ buffer: UnsafePointer<CChar>!) -> CFString!
```

#### Return Value

A string that represents `buffer`. The result is `NULL` if there was a problem in creating the string (possible if the conversion fails due to bytes in the buffer not being a valid sequence of bytes for the appropriate character encoding). Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `alloc`: The allocator to use to allocate memory for the new string. Pass   or   to use the current default allocator.
- `buffer`: The C string that you want to convert.

## See Also

- [func CFStringGetFileSystemRepresentation(CFString!, UnsafeMutablePointer<CChar>!, CFIndex) -> Bool](cfstringgetfilesystemrepresentation(_:_:_:).md)
  Extracts the contents of a string as a `NULL`-terminated 8-bit string appropriate for passing to POSIX APIs.
- [func CFStringGetMaximumSizeOfFileSystemRepresentation(CFString!) -> CFIndex](cfstringgetmaximumsizeoffilesystemrepresentation(_:).md)
  Determines the upper bound on the number of bytes required to hold the file system representation of the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringcreatewithfilesystemrepresentation(_:_:))*