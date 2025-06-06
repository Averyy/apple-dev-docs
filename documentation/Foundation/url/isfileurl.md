# isFileURL

**Framework**: Foundation  
**Kind**: property

A Boolean that is true if the scheme is `file:`.

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
var isFileURL: Bool { get }
```

## See Also

- [var hasDirectoryPath: Bool](url/hasdirectorypath.md)
  A Boolean that is true if the URL path represents a directory.
- [func withUnsafeFileSystemRepresentation<ResultType>((UnsafePointer<Int8>?) throws -> ResultType) rethrows -> ResultType](url/withunsafefilesystemrepresentation(_:).md)
  Passes the URL’s path in the file system representation to a closure.
- [func resolveSymlinksInPath()](url/resolvesymlinksinpath.md)
  Resolves any symlinks in the path of a file URL.
- [func resolvingSymlinksInPath() -> URL](url/resolvingsymlinksinpath.md)
  Resolves any symlinks in the path of a file URL.
- [func standardize()](url/standardize.md)
  Standardizes the path of a file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/isfileurl)*