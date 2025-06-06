# standardizingPath

**Framework**: Foundation  
**Kind**: property

A URL that points to the same resource as the original URL using an absolute path. (read-only)

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var standardizingPath: URL? { get }
```

#### Discussion

This property only works on URLs with the `file:` path scheme. For all other URLs, it returns a copy of the original URL.

Like [`standardizingPath`](nsstring/standardizingpath.md), this property can make the following changes in the provided URL:

- Expand an initial tilde expression using [`expandingTildeInPath`](nsstring/expandingtildeinpath.md).
- Reduce empty components and references to the current directory (that is, the sequences “//” and “/./”) to single path separators.
- In absolute paths only, resolve references to the parent directory (that is, the component “..”) to the real parent directory if possible using [`resolvingSymlinksInPath`](nsstring/resolvingsymlinksinpath.md), which consults the file system to resolve each potential symbolic link.

In relative paths, because symbolic links can’t be resolved, references to the parent directory are left in place.

- Remove an initial component of “/private” from the path if the result still indicates an existing file or directory (checked by consulting the file system).

Note that the path contained by this property may still have symbolic link components in it. Note also that this property only works with file paths (not, for example, string representations of URLs).

## See Also

- [var filePathURL: URL?](nsurl/filepathurl.md)
  A file path URL that points to the same resource as the URL object. (read-only)
- [func fileReferenceURL() -> URL?](nsurl/filereferenceurl.md)
  Returns a new file reference URL that points to the same resource as the receiver.
- [func appendingPathComponent(String) -> URL?](nsurl/appendingpathcomponent(_:).md)
  Returns a new URL by appending a path component to the original URL.
- [func appendingPathComponent(String, isDirectory: Bool) -> URL?](nsurl/appendingpathcomponent(_:isdirectory:).md)
  Returns a new URL by appending a path component to the original URL, along with a trailing slash if the component is a directory.
- [func appendingPathComponent(String, conformingTo: UTType) -> URL](nsurl/appendingpathcomponent(_:conformingto:).md)
  Returns a URL by appending the specified path component with the file extension for a uniform type identifier.
- [func appendingPathExtension(String) -> URL?](nsurl/appendingpathextension(_:).md)
  Returns a new URL by appending a path extension to the original URL.
- [func appendingPathExtension(for: UTType) -> URL](nsurl/appendingpathextension(for:).md)
  Returns a URL by appending the path extension for a uniform type identifier.
- [var deletingLastPathComponent: URL?](nsurl/deletinglastpathcomponent.md)
  A URL you create by removing the last path component from the receiver. (read-only)
- [var deletingPathExtension: URL?](nsurl/deletingpathextension.md)
  A URL you create by removing the path extension from the receiver, if any. (read-only)
- [var resolvingSymlinksInPath: URL?](nsurl/resolvingsymlinksinpath.md)
  A URL that points to the same resource as the receiver and includes no symbolic links. (read-only)
- [var hasDirectoryPath: Bool](nsurl/hasdirectorypath.md)
  A Boolean value that indicates whether the URL string’s path represents a directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/standardizingpath)*