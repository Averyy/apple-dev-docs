# init(fileURLWithFileSystemRepresentation:isDirectory:relativeTo:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a file URL that references the local file or directory for the file system representation of the path.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(fileURLWithFileSystemRepresentation path: UnsafePointer<Int8>, isDirectory: Bool, relativeTo base: URL?)
```

## Discussion

File system representation is a null-terminated C string with canonical UTF-8 encoding.

## Parameters

- `path`: The location in the file system.
- `isDirectory`: A Boolean value that indicates whether the location is a directory.

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
- [init(fileReferenceLiteralResourceName: String)](./init%28filereferenceliteralresourcename%29.md)
  Creates a URL from a playground file literal.
- [init?(filePath: FilePath, directoryHint: URL.DirectoryHint)](./init%28filepath,directoryhint%29.md)
  Creates a file URL that references a file path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/init(fileurlwithfilesystemrepresentation:isdirectory:relativeto:))*