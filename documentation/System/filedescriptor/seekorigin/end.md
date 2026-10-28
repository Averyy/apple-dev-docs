# end

**Framework**: System  
**Kind**: property  
**Role**: Type Property

Indicates that the offset should be set to the size of the file plus the specified number of bytes.

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
static var end: FileDescriptor.SeekOrigin { get }
```

## Mentions

- [Adopting Swift File Options](../../adopting-file-options.md)

## Discussion

The corresponding C constant is `SEEK_END`.

## See Also

### Creating a Seek Origin
- [static var current: FileDescriptor.SeekOrigin](./current.md)
  Indicates that the offset should be set to the specified number of bytes after the current location.
- [static var nextHole: FileDescriptor.SeekOrigin](./nexthole.md)
  Indicates that the offset should be set to the next hole after the specified number of bytes.
- [static var nextData: FileDescriptor.SeekOrigin](./nextdata.md)
  Indicates that the offset should be set to the start of the next file region that isn’t a hole and is greater than or equal to the supplied offset.
- [static var start: FileDescriptor.SeekOrigin](./start.md)
  Indicates that the offset should be set to the specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/seekorigin/end)*