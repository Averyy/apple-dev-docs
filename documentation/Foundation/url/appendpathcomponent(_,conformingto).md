# appendPathComponent(_:conformingTo:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Appends a path component to the URL that conforms to a uniform type identifier.

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
mutating func appendPathComponent(_ partialName: String, conformingTo contentType: UTType)
```

## Discussion

Use this method when you want to mix partial input from a user or other source, and need to produce a complete filename suitable for that input. For example, if you download a file from the internet and know its MIME type, you can use this method to ensure the URL has the correct filename extension where you save the file.

If `partialName` already has a path extension, and that path extension is valid for file system objects of type `contentType`, the function doesn’t add an extension before appending it to the URL. For example, if the inputs are `puppy.jpg` and [`jpeg`](../../UniformTypeIdentifiers/uttype-swift.struct/jpeg.md), respectively, the function returns a URL with an appended path component of `puppy.jpg`. However, if the inputs are `puppy.jpg` and [`plainText`](../../UniformTypeIdentifiers/uttype-swift.struct/plaintext.md), respectively, the function returns a URL with an appended path component of `puppy.jpg.txt`. If you want to replace any existing path extension, use the [`deletePathExtension()`](./deletepathextension%28%29.md) method first.

If the function can’t append the path component, it returns an unchanged URL.

> **Note**:  The modified URL has a directory path if `contentType` conforms to [`directory`](../../UniformTypeIdentifiers/uttype-swift.struct/directory.md).

For more information about types, see [Uniform Type Identifiers](../../UniformTypeIdentifiers/UniformTypeIdentifiers.md).

## Parameters

- `partialName`: The name of path component without the type.
- `contentType`: A uniform type identifier that determines the default extension.

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
- [func appendingPathComponent(String, isDirectory: Bool) -> URL](./appendingpathcomponent%28_,isdirectory%29.md)
  Returns a URL by appending the specified path component to self, specifying whether the resulting path is a directory.
- [func append<S>(components: S..., directoryHint: URL.DirectoryHint)](./append%28components,directoryhint%29.md)
  Appends multiple path components to the URL, with a hint for handling directory awareness.
- [func appending<S>(components: S..., directoryHint: URL.DirectoryHint) -> URL](./appending%28components,directoryhint%29.md)
  Returns a new URL by appending multiple path components to the URL, with a hint for handling directory awareness.
- [func appendingPathComponent(String, conformingTo: UTType) -> URL](./appendingpathcomponent%28_,conformingto%29.md)
  Returns a URL by appending the specified path component that conforms to a uniform type identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/appendpathcomponent(_:conformingto:))*