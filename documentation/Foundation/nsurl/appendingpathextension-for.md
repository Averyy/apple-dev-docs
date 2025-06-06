# appendingPathExtension(for:)

**Framework**: Foundation  
**Kind**: method

Returns a URL by appending the path extension for a uniform type identifier.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func appendingPathExtension(for contentType: UTType) -> URL
```

#### Return Value

A new URL with the type’s preferred extension appended.

#### Discussion

For more information about types, see [`Uniform Type Identifiers`](https://developer.apple.com/documentation/UniformTypeIdentifiers).

## Parameters

- `contentType`: The uniform type identifer to use for the extension.

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/appendingpathextension(for:))*