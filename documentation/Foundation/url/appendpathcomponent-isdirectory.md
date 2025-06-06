# appendPathComponent(_:isDirectory:)

**Framework**: Foundation  
**Kind**: method

Appends a path component to the URL, specifying whether the resulting path is a directory.

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
mutating func appendPathComponent(_ pathComponent: String, isDirectory: Bool)
```

#### Discussion

New code should use [`append(path:directoryHint:)`](url/append(path:directoryhint:).md) instead of this method.

## Parameters

- `pathComponent`: The path component to add.
- `isDirectory`: Use   if the resulting path is a directory.

## See Also

- [func append<S>(path: S, directoryHint: URL.DirectoryHint)](url/append(path:directoryhint:).md)
  Appends a path to the URL, with a hint for handling directory awareness.
- [func append<S>(component: S, directoryHint: URL.DirectoryHint)](url/append(component:directoryhint:).md)
  Appends a path component to the URL, with a hint for handling directory awareness.
- [func appendPathComponent(String)](url/appendpathcomponent(_:).md)
  Appends a path component to the URL.
- [func appending<S>(path: S, directoryHint: URL.DirectoryHint) -> URL](url/appending(path:directoryhint:).md)
  Returns a URL by appending the specified path to the URL, with a hint for handling directory awareness.
- [func appending<S>(component: S, directoryHint: URL.DirectoryHint) -> URL](url/appending(component:directoryhint:).md)
  Returns a URL by appending the specified path component to the URL, with a hint for handling directory awareness.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/appendpathcomponent(_:isdirectory:))*