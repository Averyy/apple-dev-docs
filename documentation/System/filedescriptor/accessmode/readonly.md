# readOnly

**Framework**: System  
**Kind**: property

Opens the file for reading only.

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
static var readOnly: FileDescriptor.AccessMode { get }
```

## Mentions

- [Adopting Swift File Options](adopting-file-options.md)

#### Discussion

The corresponding C constant is `O_RDONLY`.

## See Also

- [static var readWrite: FileDescriptor.AccessMode](filedescriptor/accessmode/readwrite.md)
  Opens the file for reading and writing.
- [static var writeOnly: FileDescriptor.AccessMode](filedescriptor/accessmode/writeonly.md)
  Opens the file for writing only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/accessmode/readonly)*