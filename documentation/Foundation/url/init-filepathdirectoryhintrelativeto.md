# init(filePath:directoryHint:relativeTo:)

**Framework**: Foundation  
**Kind**: init

Creates a file URL that references a path you specify as a string.

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
init(filePath path: String, directoryHint: URL.DirectoryHint = .inferFromPath, relativeTo base: URL? = nil)
```

## Mentions

- [Improving performance and stability when accessing the file system](improving-performance-and-stability-when-accessing-the-file-system.md)

## Parameters

- `path`: The location in the file system, as a string.
- `directoryHint`: A hint to the initializer to indicate whether the path is a directory, or to instruct the initializer to make this determination.
- `base`: A URL that provides a file system location that the path extends.

## See Also

- [enum DirectoryHint](url/directoryhint.md)
  A hint to URL file APIs for handling paths that may reference directories.
- [init(fileURLWithPath: String)](url/init(fileurlwithpath:).md)
  Creates a file URL that references the local file or directory at the given path.
- [init(fileURLWithPath: String, isDirectory: Bool)](url/init(fileurlwithpath:isdirectory:).md)
  Creates a file URL that references the local file or directory at the given path.
- [init(fileURLWithPath: String, relativeTo: URL?)](url/init(fileurlwithpath:relativeto:).md)
  Creates a file URL that references the local file or directory at the given path, relative to a base URL.
- [init(fileURLWithPath: String, isDirectory: Bool, relativeTo: URL?)](url/init(fileurlwithpath:isdirectory:relativeto:).md)
  Creates a file URL that references the local file or directory at the given path, relative to a base URL.
- [init(fileURLWithFileSystemRepresentation: UnsafePointer<Int8>, isDirectory: Bool, relativeTo: URL?)](url/init(fileurlwithfilesystemrepresentation:isdirectory:relativeto:).md)
  Creates a file URL that references the local file or directory for the file system representation of the path.
- [init(fileReferenceLiteralResourceName: String)](url/init(filereferenceliteralresourcename:).md)
  Creates a URL from a playground file literal.
- [init?(filePath: FilePath, directoryHint: URL.DirectoryHint)](url/init(filepath:directoryhint:).md)
  Creates a file URL that references a file path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/init(filepath:directoryhint:relativeto:))*