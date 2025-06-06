# appendingPathExtension(_:)

**Framework**: Foundation  
**Kind**: method

Returns a new URL by appending a path extension to the original URL.

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
func appendingPathExtension(_ pathExtension: String) -> URL?
```

#### Return Value

A new URL with `pathExtension` appended.

#### Discussion

If the original URL ends with one or more forward slashes, these are removed from the returned URL. A period is inserted between the two parts of the new URL.

## Parameters

- `pathExtension`: The path extension to add to the URL.

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/appendingpathextension(_:))*