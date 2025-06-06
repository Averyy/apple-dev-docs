# appendingPathComponent(_:isDirectory:)

**Framework**: Foundation  
**Kind**: method

Returns a URL by appending the specified path component to self, specifying whether the resulting path is a directory.

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
func appendingPathComponent(_ pathComponent: String, isDirectory: Bool) -> URL
```

#### Return Value

A new URL with the path component appended.

#### Discussion

The URL syntax for a directory and for a file at otherwise the same location are slightly different — directory URLs must end in `/`. If you append the path component `second` to the URL `http://www.example.com/first/`, if `isDirectory` is `true`, the resulting URL is `http://www.example.com/first/second/.` If `isDirectory` is `false`, the resulting URL is `http://www.example.com/first/second`.

This difference is particularly important if you resolve another URL against this new URL. For example, the path component `file.html` relative to `http://www.example.com/first/second` is `http://www.apple.com/first/file.html`, whereas relative to `http://www.example.com/first/second/`, it’s `http://www.example.com/first/second/file.html`.

New code should use [`appending(path:directoryHint:)`](url/appending(path:directoryhint:).md) instead of this method.

## Parameters

- `pathComponent`: The path component to add.
- `isDirectory`: If  , the method treats the path component as a directory.

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
- [func appendingPathComponent(String) -> URL](url/appendingpathcomponent(_:).md)
  Returns a URL by appending the specified path component to self.
- [func append<S>(components: S..., directoryHint: URL.DirectoryHint)](url/append(components:directoryhint:).md)
  Appends multiple path components to the URL, with a hint for handling directory awareness.
- [func appending<S>(components: S..., directoryHint: URL.DirectoryHint) -> URL](url/appending(components:directoryhint:).md)
  Returns a new URL by appending multiple path components to the URL, with a hint for handling directory awareness.
- [func appendPathComponent(String, conformingTo: UTType)](url/appendpathcomponent(_:conformingto:).md)
  Appends a path component to the URL that conforms to a uniform type identifier.
- [func appendingPathComponent(String, conformingTo: UTType) -> URL](url/appendingpathcomponent(_:conformingto:).md)
  Returns a URL by appending the specified path component that conforms to a uniform type identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/appendingpathcomponent(_:isdirectory:))*