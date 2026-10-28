# appendingPathComponent(_:isDirectory:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a URL by appending the specified path component to self, specifying whether the resulting path is a directory.

**Availability**:
- iOS 8.0+ - Deprecated in 27.2
- iPadOS 8.0+ - Deprecated in 27.2
- Mac Catalyst 8.0+ - Deprecated in 27.2
- macOS 10.10+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use appending(path:directoryHint:) instead

## Declaration

```swift
func appendingPathComponent(_ pathComponent: String, isDirectory: Bool) -> URL
```

## Return Value

A new URL with the path component appended.

## Discussion

The URL syntax for a directory and for a file at otherwise the same location are slightly different — directory URLs must end in `/`. If you append the path component `second` to the URL `http://www.example.com/first/`, if `isDirectory` is `true`, the resulting URL is `http://www.example.com/first/second/.` If `isDirectory` is `false`, the resulting URL is `http://www.example.com/first/second`.

This difference is particularly important if you resolve another URL against this new URL. For example, the path component `file.html` relative to `http://www.example.com/first/second` is `http://www.apple.com/first/file.html`, whereas relative to `http://www.example.com/first/second/`, it’s `http://www.example.com/first/second/file.html`.

New code should use [`appending(path:directoryHint:)`](./appending%28path,directoryhint%29.md) instead of this method.

## Parameters

- `pathComponent`: The path component to add.
- `isDirectory`: If `true`, the method treats the path component as a directory.

## See Also

### Adding path components
- [func append<S>(path: S, directoryHint: URL.DirectoryHint)](./append%28path,directoryhint%29.md)
  Appends a path to the URL, with a hint for handling directory awareness.
- [func append<S>(component: S, directoryHint: URL.DirectoryHint)](./append%28component,directoryhint%29.md)
  Appends a path component to the URL, with a hint for handling directory awareness.
- [func appendPathComponent(String)](./appendpathcomponent%28_%29.md)
  Appends a path component to the URL.
- [func appendPathComponent(String, isDirectory: Bool)](./appendpathcomponent%28_,isdirectory%29.md)
  Appends a path component to the URL, specifying whether the resulting path is a directory.
- [func appending<S>(path: S, directoryHint: URL.DirectoryHint) -> URL](./appending%28path,directoryhint%29.md)
  Returns a URL by appending the specified path to the URL, with a hint for handling directory awareness.
- [func appending<S>(component: S, directoryHint: URL.DirectoryHint) -> URL](./appending%28component,directoryhint%29.md)
  Returns a URL by appending the specified path component to the URL, with a hint for handling directory awareness.
- [func appendingPathComponent(String) -> URL](./appendingpathcomponent%28_%29.md)
  Returns a URL by appending the specified path component to self.
- [func append<S>(components: S..., directoryHint: URL.DirectoryHint)](./append%28components,directoryhint%29.md)
  Appends multiple path components to the URL, with a hint for handling directory awareness.
- [func appending<S>(components: S..., directoryHint: URL.DirectoryHint) -> URL](./appending%28components,directoryhint%29.md)
  Returns a new URL by appending multiple path components to the URL, with a hint for handling directory awareness.
- [func appendPathComponent(String, conformingTo: UTType)](./appendpathcomponent%28_,conformingto%29.md)
  Appends a path component to the URL that conforms to a uniform type identifier.
- [func appendingPathComponent(String, conformingTo: UTType) -> URL](./appendingpathcomponent%28_,conformingto%29.md)
  Returns a URL by appending the specified path component that conforms to a uniform type identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/appendingpathcomponent(_:isdirectory:))*