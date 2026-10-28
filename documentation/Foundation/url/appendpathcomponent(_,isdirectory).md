# appendPathComponent(_:isDirectory:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Appends a path component to the URL, specifying whether the resulting path is a directory.

**Availability**:
- iOS 8.0+ - Deprecated in 27.2
- iPadOS 8.0+ - Deprecated in 27.2
- Mac Catalyst 8.0+ - Deprecated in 27.2
- macOS 10.10+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use append(path:directoryHint:) instead

## Declaration

```swift
mutating func appendPathComponent(_ pathComponent: String, isDirectory: Bool)
```

## Discussion

New code should use [`append(path:directoryHint:)`](./append%28path,directoryhint%29.md) instead of this method.

## Parameters

- `pathComponent`: The path component to add.
- `isDirectory`: Use `true` if the resulting path is a directory.

## See Also

### Adding path components
- [func append<S>(path: S, directoryHint: URL.DirectoryHint)](./append%28path,directoryhint%29.md)
  Appends a path to the URL, with a hint for handling directory awareness.
- [func append<S>(component: S, directoryHint: URL.DirectoryHint)](./append%28component,directoryhint%29.md)
  Appends a path component to the URL, with a hint for handling directory awareness.
- [func appendPathComponent(String)](./appendpathcomponent%28_%29.md)
  Appends a path component to the URL.
- [func appending<S>(path: S, directoryHint: URL.DirectoryHint) -> URL](./appending%28path,directoryhint%29.md)
  Returns a URL by appending the specified path to the URL, with a hint for handling directory awareness.
- [func appending<S>(component: S, directoryHint: URL.DirectoryHint) -> URL](./appending%28component,directoryhint%29.md)
  Returns a URL by appending the specified path component to the URL, with a hint for handling directory awareness.
- [func appendingPathComponent(String) -> URL](./appendingpathcomponent%28_%29.md)
  Returns a URL by appending the specified path component to self.
- [func appendingPathComponent(String, isDirectory: Bool) -> URL](./appendingpathcomponent%28_,isdirectory%29.md)
  Returns a URL by appending the specified path component to self, specifying whether the resulting path is a directory.
- [func append<S>(components: S..., directoryHint: URL.DirectoryHint)](./append%28components,directoryhint%29.md)
  Appends multiple path components to the URL, with a hint for handling directory awareness.
- [func appending<S>(components: S..., directoryHint: URL.DirectoryHint) -> URL](./appending%28components,directoryhint%29.md)
  Returns a new URL by appending multiple path components to the URL, with a hint for handling directory awareness.
- [func appendPathComponent(String, conformingTo: UTType)](./appendpathcomponent%28_,conformingto%29.md)
  Appends a path component to the URL that conforms to a uniform type identifier.
- [func appendingPathComponent(String, conformingTo: UTType) -> URL](./appendingpathcomponent%28_,conformingto%29.md)
  Returns a URL by appending the specified path component that conforms to a uniform type identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/appendpathcomponent(_:isdirectory:))*