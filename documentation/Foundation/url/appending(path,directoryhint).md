# appending(path:directoryHint:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a URL by appending the specified path to the URL, with a hint for handling directory awareness.

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
func appending<S>(path: S, directoryHint: URL.DirectoryHint = .inferFromPath) -> URL where S : StringProtocol
```

## Mentions

- [Improving performance and stability when accessing the file system](../improving-performance-and-stability-when-accessing-the-file-system.md)

#### Return Value

A new URL that appends the specified path to the original URL.

#### Discussion

This method doesn’t percent-encode any path separators (`/`) in the path component before appending the component to the path. If you want this encoding, use [`appending(component:directoryHint:)`](./appending%28component,directoryhint%29.md) instead.

## Parameters

- `path`: The path to add.
- `directoryHint`: A hint to the method to indicate whether the path is a directory, or to instruct the method to make this determination. Defaults to [`URL.DirectoryHint.inferFromPath`](./directoryhint/inferfrompath.md).

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/appending(path:directoryhint:))*