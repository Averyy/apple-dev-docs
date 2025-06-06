# current

**Framework**: System  
**Kind**: property

Indicates that the offset should be set to the specified number of bytes after the current location.

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
static var current: FileDescriptor.SeekOrigin { get }
```

## Mentions

- [Adopting Swift File Options](adopting-file-options.md)

#### Discussion

The corresponding C constant is `SEEK_CUR`.

## See Also

- [static var end: FileDescriptor.SeekOrigin](filedescriptor/seekorigin/end.md)
  Indicates that the offset should be set to the size of the file plus the specified number of bytes.
- [static var nextHole: FileDescriptor.SeekOrigin](filedescriptor/seekorigin/nexthole.md)
  Indicates that the offset should be set to the next hole after the specified number of bytes.
- [static var nextData: FileDescriptor.SeekOrigin](filedescriptor/seekorigin/nextdata.md)
  Indicates that the offset should be set to the start of the next file region that isn’t a hole and is greater than or equal to the supplied offset.
- [static var start: FileDescriptor.SeekOrigin](filedescriptor/seekorigin/start.md)
  Indicates that the offset should be set to the specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/seekorigin/current)*