# CFStringGetFileSystemRepresentation(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Extracts the contents of a string as a `NULL`-terminated 8-bit string appropriate for passing to POSIX APIs.

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
func CFStringGetFileSystemRepresentation(_ string: CFString!, _ buffer: UnsafeMutablePointer<CChar>!, _ maxBufLen: CFIndex) -> Bool
```

#### Return Value

`true` if the string is correctly converted; `false` if the conversion fails, or the results don’t fit into the buffer.

#### Discussion

You can use [`CFStringGetMaximumSizeOfFileSystemRepresentation(_:)`](cfstringgetmaximumsizeoffilesystemrepresentation(_:).md) if you want to make sure the buffer is of sufficient length.

## Parameters

- `string`: The string to convert.
- `buffer`: The C string buffer into which to copy the string. The buffer must be at least   bytes in length. On return, the buffer contains the converted characters.
- `maxBufLen`: The maximum length of the buffer.

## See Also

- [func CFStringCreateWithFileSystemRepresentation(CFAllocator!, UnsafePointer<CChar>!) -> CFString!](cfstringcreatewithfilesystemrepresentation(_:_:).md)
  Creates a CFString from a zero-terminated POSIX file system representation.
- [func CFStringGetMaximumSizeOfFileSystemRepresentation(CFString!) -> CFIndex](cfstringgetmaximumsizeoffilesystemrepresentation(_:).md)
  Determines the upper bound on the number of bytes required to hold the file system representation of the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringgetfilesystemrepresentation(_:_:_:))*