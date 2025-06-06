# URL.DirectoryHint

**Framework**: Foundation  
**Kind**: enum

A hint to URL file APIs for handling paths that may reference directories.

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
enum DirectoryHint
```

## Topics

### Hints
- [URL.DirectoryHint.isDirectory](url/directoryhint/isdirectory.md)
  A hint that specifies that a given path is a directory.
- [URL.DirectoryHint.notDirectory](url/directoryhint/notdirectory.md)
  A hint that specifies that a given path isn’t a directory.
- [URL.DirectoryHint.checkFileSystem](url/directoryhint/checkfilesystem.md)
  A hint that directs a URL call to consult the file system to determine whether the path references a directory.
- [URL.DirectoryHint.inferFromPath](url/directoryhint/inferfrompath.md)
  A hint that directs a URL call to infer whether a path references a directory based on whether it has a trailing slash.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [init(filePath: String, directoryHint: URL.DirectoryHint, relativeTo: URL?)](url/init(filepath:directoryhint:relativeto:).md)
  Creates a file URL that references a path you specify as a string.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/directoryhint)*