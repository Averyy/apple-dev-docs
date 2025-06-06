# seek(offset:from:)

**Framework**: System  
**Kind**: method

Repositions the offset for the given file descriptor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@discardableResult
func seek(offset: Int64, from whence: FileDescriptor.SeekOrigin) throws -> Int64
```

#### Return Value

The file’s offset location, in bytes from the beginning of the file.

#### Discussion

The corresponding C function is `lseek`.

## Parameters

- `offset`: The new offset for the file descriptor.
- `whence`: The origin of the new offset.

## See Also

- [FileDescriptor.SeekOrigin](filedescriptor/seekorigin.md)
  Options for specifying what a file descriptor’s offset is relative to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/seek(offset:from:))*