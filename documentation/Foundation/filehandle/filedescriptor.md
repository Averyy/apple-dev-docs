# fileDescriptor

**Framework**: Foundation  
**Kind**: property

The POSIX file descriptor associated with the receiver.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var fileDescriptor: Int32 { get }
```

#### Discussion

You can use this method to retrieve the file descriptor while it is open. If the file handle object owns the file descriptor, you must not close it yourself. However, you can use the [`closeFile()`](filehandle/closefile().md) method to close the file descriptor programmatically. If you do call the [`closeFile()`](filehandle/closefile().md) method, subsequent calls to this method raise an exception.

## See Also

- [convenience init(fileDescriptor: Int32)](filehandle/init(filedescriptor:).md)
  Creates and returns a file handle object associated with the specified file descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/filedescriptor)*