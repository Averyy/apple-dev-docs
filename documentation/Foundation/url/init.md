# init(_:)

**Framework**: Foundation  
**Kind**: init

Creates a file URL that references the local file or directory at the file path you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- watchOS 7.0+

## Declaration

```swift
init?(_ path: FilePath)
```

#### Discussion

This method may perform file system I/O to determine if the path is to a directory. If you know the path is to a directory, use [`init(_:isDirectory:)`](url/init(_:isdirectory:).md) to avoid the file system I/O.

## Parameters

- `path`: The location in the file system.

## See Also

- [init?(FilePath, isDirectory: Bool)](url/init(_:isdirectory:).md)
  Creates a file URL that references the local file or directory at the file path you specify.
- [struct FilePath](../System/FilePath.md)
  Represents a location in the file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/init(_:))*