# init(_:isDirectory:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a file URL that references the local file or directory at the file path you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 16.0
- iPadOS 14.0+ - Deprecated in 16.0
- Mac Catalyst 14.0+ - Deprecated in 16.0
- macOS 11.0+ - Deprecated in 13.0
- tvOS 14.0+ - Deprecated in 16.0
- watchOS 7.0+ - Deprecated in 9.0

> **Deprecated**: Use init?(filePath:directoryHint:) instead

## Declaration

```swift
init?(_ path: FilePath, isDirectory: Bool)
```

## Discussion

> **Note**:  This method avoids file system I/O to determine if the path is to a directory. When you know that information, prefer this method to initializers without the parameter.

## Parameters

- `path`: The location in the file system.
- `isDirectory`: A Boolean value that indicates whether the location is a directory.

## See Also

### Creating a file URL from a file path
- [init?(FilePath)](./init%28_%29.md)
  Creates a file URL that references the local file or directory at the file path you specify.
- [struct FilePath](../../System/filepath.md)
  Represents a location in the file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/init(_:isdirectory:))*