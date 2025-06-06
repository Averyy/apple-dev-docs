# appendingPathComponent(_:)

**Framework**: Foundation  
**Kind**: method

Returns a URL by appending the specified path component to self.

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
func appendingPathComponent(_ pathComponent: String) -> URL
```

#### Discussion

For file URLs, this method may perform file system I/O to determine if the path component is a directory, and, if so, it appends a trailing slash `/`. Use [`appendingPathComponent(_:isDirectory:)`](url/appendingpathcomponent(_:isdirectory:).md) if you know the component’s file system object type in advance.

New code should use [`appending(path:directoryHint:)`](url/appending(path:directoryhint:).md) instead of this method.

## Parameters

- `pathComponent`: The path component to add.

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
- [func appending<S>(component: S, directoryHint: URL.DirectoryHint) -> URL](url/appending(component:directoryhint:).md)
  Returns a URL by appending the specified path component to the URL, with a hint for handling directory awareness.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/appendingpathcomponent(_:))*