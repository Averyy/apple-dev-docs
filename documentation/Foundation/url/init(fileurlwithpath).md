# init(fileURLWithPath:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a file URL that references the local file or directory at the given path.

**Availability**:
- iOS 8.0+ - Deprecated in 27.2
- iPadOS 8.0+ - Deprecated in 27.2
- Mac Catalyst 8.0+ - Deprecated in 27.2
- macOS 10.10+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [`init(filePath:directoryHint:relativeTo:)`](./init%28filepath,directoryhint,relativeto%29.md) instead.

## Declaration

```swift
init(fileURLWithPath path: String)
```

## Discussion

If the path is an empty string, the system interprets it as “.”.

## Parameters

- `path`: The location in the file system.

## See Also

### Creating a file URL from a string path
- [init(filePath: String, directoryHint: URL.DirectoryHint, relativeTo: URL?)](./init%28filepath,directoryhint,relativeto%29.md)
  Creates a file URL that references a path you specify as a string.
- [enum DirectoryHint](./directoryhint.md)
  A hint to URL file APIs for handling paths that may reference directories.
- [init(fileURLWithPath: String, isDirectory: Bool)](./init%28fileurlwithpath,isdirectory%29.md)
  Creates a file URL that references the local file or directory at the given path.
- [init(fileURLWithPath: String, relativeTo: URL?)](./init%28fileurlwithpath,relativeto%29.md)
  Creates a file URL that references the local file or directory at the given path, relative to a base URL.
- [init(fileURLWithPath: String, isDirectory: Bool, relativeTo: URL?)](./init%28fileurlwithpath,isdirectory,relativeto%29.md)
  Creates a file URL that references the local file or directory at the given path, relative to a base URL.
- [init(fileURLWithFileSystemRepresentation: UnsafePointer<Int8>, isDirectory: Bool, relativeTo: URL?)](./init%28fileurlwithfilesystemrepresentation,isdirectory,relativeto%29.md)
  Creates a file URL that references the local file or directory for the file system representation of the path.
- [init(fileReferenceLiteralResourceName: String)](./init%28filereferenceliteralresourcename%29.md)
  Creates a URL from a playground file literal.
- [init?(filePath: FilePath, directoryHint: URL.DirectoryHint)](./init%28filepath,directoryhint%29.md)
  Creates a file URL that references a file path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/init(fileurlwithpath:))*