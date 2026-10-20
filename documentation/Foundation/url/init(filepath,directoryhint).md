# init(filePath:directoryHint:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a file URL that references a file path.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init?(filePath path: FilePath, directoryHint: URL.DirectoryHint = .inferFromPath)
```

## Parameters

- `path`: The location in the file system.
- `directoryHint`: A hint to the initializer to indicate whether the path is a directory, or to instruct the initializer to make this determination.

## See Also

### Creating a file URL from a string path
- [init(filePath: String, directoryHint: URL.DirectoryHint, relativeTo: URL?)](./init%28filepath,directoryhint,relativeto%29.md)
  Creates a file URL that references a path you specify as a string.
- [enum DirectoryHint](./directoryhint.md)
  A hint to URL file APIs for handling paths that may reference directories.
- [init(fileURLWithPath: String)](./init%28fileurlwithpath%29.md)
  Creates a file URL that references the local file or directory at the given path.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/init(filepath:directoryhint:))*