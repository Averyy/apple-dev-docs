# appending(component:directoryHint:)

**Framework**: Foundation  
**Kind**: method

Returns a URL by appending the specified path component to the URL, with a hint for handling directory awareness.

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
func appending<S>(component: S, directoryHint: URL.DirectoryHint = .inferFromPath) -> URL where S : StringProtocol
```

#### Return Value

A new URL that appends the specified path to the original URL.

#### Discussion

This method percent-encodes any path separators (`/`) in the path component before appending the component to the path. If you don’t want this encoding, use [`appending(path:directoryHint:)`](url/appending(path:directoryhint:).md) instead.

## Parameters

- `component`: The path component to add.
- `directoryHint`: A hint to the initializer to indicate whether the path is a directory, or to instruct the method to make this determination. Defaults to  .

## See Also

- [func append<S>(path: S, directoryHint: URL.DirectoryHint)](url/append(path:directoryhint:).md)
  Appends a path to the URL, with a hint for handling directory awareness.
- [func append<S>(component: S, directoryHint: URL.DirectoryHint)](url/append(component:directoryhint:).md)
  Appends a path component to the URL, with a hint for handling directory awareness.
- [func appendPathComponent(String)](url/appendpathcomponent(_:).md)
  Appends a path component to the URL.
- [func appendPathComponent(String, isDirectory: Bool)](url/appendpathcomponent(_:isdirectory:).md)
  Appends a path component to the URL, specifying whether the resulting path is a directory.
- [func appending<S>(path: S, directoryHint: URL.DirectoryHint) -> URL](url/appending(path:directoryhint:).md)
  Returns a URL by appending the specified path to the URL, with a hint for handling directory awareness.
- [func appendingPathComponent(String) -> URL](url/appendingpathcomponent(_:).md)
  Returns a URL by appending the specified path component to self.
- [func appendingPathComponent(String, isDirectory: Bool) -> URL](url/appendingpathcomponent(_:isdirectory:).md)
  Returns a URL by appending the specified path component to self, specifying whether the resulting path is a directory.
- [func append<S>(components: S..., directoryHint: URL.DirectoryHint)](url/append(components:directoryhint:).md)
  Appends multiple path components to the URL, with a hint for handling directory awareness.
- [func appending<S>(components: S..., directoryHint: URL.DirectoryHint) -> URL](url/appending(components:directoryhint:).md)
  Returns a new URL by appending multiple path components to the URL, with a hint for handling directory awareness.
- [func appendPathComponent(String, conformingTo: UTType)](url/appendpathcomponent(_:conformingto:).md)
  Appends a path component to the URL that conforms to a uniform type identifier.
- [func appendingPathComponent(String, conformingTo: UTType) -> URL](url/appendingpathcomponent(_:conformingto:).md)
  Returns a URL by appending the specified path component that conforms to a uniform type identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/appending(component:directoryhint:))*