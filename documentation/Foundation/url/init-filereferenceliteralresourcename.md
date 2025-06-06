# init(fileReferenceLiteralResourceName:)

**Framework**: Foundation  
**Kind**: init

Creates a URL from a playground file literal.

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
init(fileReferenceLiteralResourceName name: String)
```

## Parameters

- `name`: The playground file literal name, as a string.

## See Also

- [init(filePath: String, directoryHint: URL.DirectoryHint, relativeTo: URL?)](url/init(filepath:directoryhint:relativeto:).md)
  Creates a file URL that references a path you specify as a string.
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
- [init?(filePath: FilePath, directoryHint: URL.DirectoryHint)](url/init(filepath:directoryhint:).md)
  Creates a file URL that references a file path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/init(filereferenceliteralresourcename:))*