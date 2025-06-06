# init(_:isDirectory:)

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
init?(_ path: FilePath, isDirectory: Bool)
```

#### Discussion

> **Note**:  This method avoids file system I/O to determine if the path is to a directory. When you know that information, prefer this method to initializers without the parameter.

## Parameters

- `path`: The location in the file system.
- `isDirectory`: A Boolean value that indicates whether the location is a directory.

## See Also

- [init?(FilePath)](url/init(_:).md)
  Creates a file URL that references the local file or directory at the file path you specify.
- [struct FilePath](../System/FilePath.md)
  Represents a location in the file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/init(_:isdirectory:))*