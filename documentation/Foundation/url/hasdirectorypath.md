# hasDirectoryPath

**Framework**: Foundation  
**Kind**: property

A Boolean that is true if the URL path represents a directory.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var hasDirectoryPath: Bool { get }
```

## See Also

- [var isFileURL: Bool](url/isfileurl.md)
  A Boolean that is true if the scheme is `file:`.
- [func withUnsafeFileSystemRepresentation<ResultType>((UnsafePointer<Int8>?) throws -> ResultType) rethrows -> ResultType](url/withunsafefilesystemrepresentation(_:).md)
  Passes the URL’s path in the file system representation to a closure.
- [func resolveSymlinksInPath()](url/resolvesymlinksinpath.md)
  Resolves any symlinks in the path of a file URL.
- [func resolvingSymlinksInPath() -> URL](url/resolvingsymlinksinpath.md)
  Resolves any symlinks in the path of a file URL.
- [func standardize()](url/standardize.md)
  Standardizes the path of a file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/hasdirectorypath)*