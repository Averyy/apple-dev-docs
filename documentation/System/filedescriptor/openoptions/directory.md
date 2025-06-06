# directory

**Framework**: System  
**Kind**: property

Indicates that opening the file only succeeds if the file is a directory.

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
static var directory: FileDescriptor.OpenOptions { get }
```

#### Discussion

If you specify this option and the file path you pass to doc:FileDescriptor/open(_:_:options:permissions:retryOnInterrupt:)-2266j is a not a directory, then that open operation fails.

The corresponding C constant is `O_DIRECTORY`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/openoptions/directory)*