# open(_:_:options:permissions:retryOnInterrupt:)

**Framework**: System  
**Kind**: method

Opens or creates a file for reading or writing.

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
static func open(_ path: UnsafePointer<CChar>, _ mode: FileDescriptor.AccessMode, options: FileDescriptor.OpenOptions = FileDescriptor.OpenOptions(), permissions: FilePermissions? = nil, retryOnInterrupt: Bool = true) throws -> FileDescriptor
```

#### Return Value

A file descriptor for the open file

#### Discussion

The corresponding C function is `open`.

## Parameters

- `path`: The location of the file to open.
- `mode`: The read and write access to use.
- `options`: The behavior for opening the file.
- `permissions`: The file permissions to use for created files.
- `retryOnInterrupt`: Whether to retry the open operation   if it throws  .   The default is  .   Pass   to try only once and throw an error upon interruption.

## See Also

- [static func open(FilePath, FileDescriptor.AccessMode, options: FileDescriptor.OpenOptions, permissions: FilePermissions?, retryOnInterrupt: Bool) throws -> FileDescriptor](filedescriptor/open(_:_:options:permissions:retryoninterrupt:)-4ql4b.md)
  Opens or creates a file for reading or writing.
- [FileDescriptor.AccessMode](filedescriptor/accessmode.md)
  The desired read and write access for a newly opened file.
- [FileDescriptor.OpenOptions](filedescriptor/openoptions.md)
  Options that specify behavior for a newly-opened file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/open(_:_:options:permissions:retryoninterrupt:)-5t3xn)*