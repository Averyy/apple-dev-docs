# writeOnly

**Framework**: System  
**Kind**: property

Opens the file for writing only.

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
static var writeOnly: FileDescriptor.AccessMode { get }
```

## Mentions

- [Adopting Swift File Options](adopting-file-options.md)

#### Discussion

The corresponding C constant is `O_WRONLY`.

## See Also

- [static var readOnly: FileDescriptor.AccessMode](filedescriptor/accessmode/readonly.md)
  Opens the file for reading only.
- [static var readWrite: FileDescriptor.AccessMode](filedescriptor/accessmode/readwrite.md)
  Opens the file for reading and writing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/accessmode/writeonly)*