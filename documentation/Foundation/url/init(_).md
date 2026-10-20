# init(_:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a file URL that references the local file or directory at the file path you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 16.0 (renamed: init(filePath:))
- iPadOS 14.0+ - Deprecated in 16.0 (renamed: init(filePath:))
- Mac Catalyst 14.0+ - Deprecated in 16.0 (renamed: init(filePath:))
- macOS 11.0+ - Deprecated in 13.0 (renamed: init(filePath:))
- tvOS 14.0+ - Deprecated in 16.0 (renamed: init(filePath:))
- watchOS 7.0+ - Deprecated in 9.0 (renamed: init(filePath:))

## Declaration

```swift
init?(_ path: FilePath)
```

#### Discussion

This method may perform file system I/O to determine if the path is to a directory. If you know the path is to a directory, use [`init(_:isDirectory:)`](./init%28_,isdirectory%29.md) to avoid the file system I/O.

## Parameters

- `path`: The location in the file system.

## See Also

### Creating a file URL from a file path
- [init?(FilePath, isDirectory: Bool)](./init%28_,isdirectory%29.md)
  Creates a file URL that references the local file or directory at the file path you specify.
- [struct FilePath](../../System/filepath.md)
  Represents a location in the file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/init(_:))*