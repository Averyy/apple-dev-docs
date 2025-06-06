# appendingPathComponent(_:)

**Framework**: Foundation  
**Kind**: method

Returns a new URL by appending a path component to the original URL.

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
func appendingPathComponent(_ pathComponent: String) -> URL?
```

## Mentions

- [Improving performance and stability when accessing the file system](improving-performance-and-stability-when-accessing-the-file-system.md)

#### Return Value

A new URL with `pathComponent` appended.

#### Discussion

If the original URL does not end with a forward slash and `pathComponent` does not begin with a forward slash, a forward slash is inserted between the two parts of the returned URL, unless the original URL is the empty string.

If the receiver is a file URL and `pathComponent` does not end with a trailing slash, this method may read file metadata to determine whether the resulting path is a directory. This is done synchronously, and may have significant performance costs if the receiver is a location on a network mounted filesystem. You can instead call the [`appendingPathComponent(_:isDirectory:)`](nsurl/appendingpathcomponent(_:isdirectory:).md) method if you know whether the resulting path is a directory to avoid this file metadata operation.

## Parameters

- `pathComponent`: The path component to add to the URL, in its original form (not URL encoded).

## See Also

- [var filePathURL: URL?](nsurl/filepathurl.md)
  A file path URL that points to the same resource as the URL object. (read-only)
- [func fileReferenceURL() -> URL?](nsurl/filereferenceurl.md)
  Returns a new file reference URL that points to the same resource as the receiver.
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
- [var standardizingPath: URL?](nsurl/standardizingpath.md)
  A URL that points to the same resource as the original URL using an absolute path. (read-only)
- [var hasDirectoryPath: Bool](nsurl/hasdirectorypath.md)
  A Boolean value that indicates whether the URL string’s path represents a directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/appendingpathcomponent(_:))*