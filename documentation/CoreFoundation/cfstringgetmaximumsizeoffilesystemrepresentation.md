# CFStringGetMaximumSizeOfFileSystemRepresentation(_:)

**Framework**: Core Foundation  
**Kind**: func

Determines the upper bound on the number of bytes required to hold the file system representation of the string.

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
func CFStringGetMaximumSizeOfFileSystemRepresentation(_ string: CFString!) -> CFIndex
```

#### Return Value

The upper bound on the number of bytes required to hold the file system representation of the string.

#### Discussion

The result is returned quickly as a rough approximation, and could be much larger than the actual space required. The result includes space for the zero termination. If you are allocating a buffer for long-term storage, you should reallocate it to be the right size after calling [`CFStringGetFileSystemRepresentation(_:_:_:)`](cfstringgetfilesystemrepresentation(_:_:_:).md).

## Parameters

- `string`: The string to convert.

## See Also

- [func CFStringCreateWithFileSystemRepresentation(CFAllocator!, UnsafePointer<CChar>!) -> CFString!](cfstringcreatewithfilesystemrepresentation(_:_:).md)
  Creates a CFString from a zero-terminated POSIX file system representation.
- [func CFStringGetFileSystemRepresentation(CFString!, UnsafeMutablePointer<CChar>!, CFIndex) -> Bool](cfstringgetfilesystemrepresentation(_:_:_:).md)
  Extracts the contents of a string as a `NULL`-terminated 8-bit string appropriate for passing to POSIX APIs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringgetmaximumsizeoffilesystemrepresentation(_:))*