# isFileURL

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

### Working with file URLs
- [var hasDirectoryPath: Bool](./hasdirectorypath.md)
  A Boolean that is true if the URL path represents a directory.
- [func withUnsafeFileSystemRepresentation<ResultType>((UnsafePointer<Int8>?) throws -> ResultType) rethrows -> ResultType](./withunsafefilesystemrepresentation%28_%29.md)
  Passes the URL’s path in the file system representation to a closure.
- [func resolveSymlinksInPath()](./resolvesymlinksinpath%28%29.md)
  Resolves any symlinks in the path of a file URL.
- [func resolvingSymlinksInPath() -> URL](./resolvingsymlinksinpath%28%29.md)
  Resolves any symlinks in the path of a file URL.
- [func standardize()](./standardize%28%29.md)
  Standardizes the path of a file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/isfileurl)*