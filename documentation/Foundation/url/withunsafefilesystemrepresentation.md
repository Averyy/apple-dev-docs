# withUnsafeFileSystemRepresentation(_:)

**Framework**: Foundation  
**Kind**: method

Passes the URL’s path in the file system representation to a closure.

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
func withUnsafeFileSystemRepresentation<ResultType>(_ block: (UnsafePointer<Int8>?) throws -> ResultType) rethrows -> ResultType
```

#### Return Value

The value returned by your closure, if any.

#### Discussion

The file system representation is a null-terminated C string with canonical UTF-8 encoding.

> **Note**:  The pointer is not valid outside the context of the closure.

## Parameters

- `block`: The parameter passed to the closure is   if the URL cannot be represented by the file system. For example, if the URL contains an accented character and the file system only supports ASCII, no file system representation is possible.

## See Also

- [var isFileURL: Bool](url/isfileurl.md)
  A Boolean that is true if the scheme is `file:`.
- [var hasDirectoryPath: Bool](url/hasdirectorypath.md)
  A Boolean that is true if the URL path represents a directory.
- [func resolveSymlinksInPath()](url/resolvesymlinksinpath.md)
  Resolves any symlinks in the path of a file URL.
- [func resolvingSymlinksInPath() -> URL](url/resolvingsymlinksinpath.md)
  Resolves any symlinks in the path of a file URL.
- [func standardize()](url/standardize.md)
  Standardizes the path of a file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/withunsafefilesystemrepresentation(_:))*