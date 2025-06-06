# appendingPathComponent(_:conformingTo:)

**Framework**: Foundation  
**Kind**: method

Returns a URL by appending the specified path component that conforms to a uniform type identifier.

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
func appendingPathComponent(_ partialName: String, conformingTo contentType: UTType) -> URL
```

#### Return Value

A new URL with the partial name and the type’s preferred extension appended.

#### Discussion

Use this method when you want to mix partial input from a user or other source, and need to produce a complete filename suitable for that input. For example, if you download a file from the internet and know its MIME type, you can use this method to ensure the URL has the correct filename extension where you save the file.

If `partialName` already has a path extension, and that path extension is valid for file system objects of type `contentType`, the function doesn’t add an extension before appending it to the URL. For example, if the inputs are `puppy.jpg` and [`jpeg`](https://developer.apple.com/documentation/UniformTypeIdentifiers/UTType-swift.struct/jpeg), respectively, the function returns a URL with an appended path component of `puppy.jpg`. However, if the inputs are `puppy.jpg` and [`plainText`](https://developer.apple.com/documentation/UniformTypeIdentifiers/UTType-swift.struct/plainText), respectively, the function returns a URL with an appended path component of `puppy.jpg.txt`. If you want to replace any existing path extension, use the [`deletePathExtension()`](url/deletepathextension().md) method first.

If the function can’t append the path component, it returns an unchanged URL.

> **Note**:  The modified URL has a directory path if `contentType` conforms to [`directory`](https://developer.apple.com/documentation/UniformTypeIdentifiers/UTType-swift.struct/directory).

For more information about types, see [`Uniform Type Identifiers`](https://developer.apple.com/documentation/UniformTypeIdentifiers).

## Parameters

- `partialName`: The name of path component without the type.
- `contentType`: A uniform type identifier that determines the default extension.

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
- [func appendingPathComponent(String, isDirectory: Bool) -> URL](url/appendingpathcomponent(_:isdirectory:).md)
  Returns a URL by appending the specified path component to self, specifying whether the resulting path is a directory.
- [func append<S>(components: S..., directoryHint: URL.DirectoryHint)](url/append(components:directoryhint:).md)
  Appends multiple path components to the URL, with a hint for handling directory awareness.
- [func appending<S>(components: S..., directoryHint: URL.DirectoryHint) -> URL](url/appending(components:directoryhint:).md)
  Returns a new URL by appending multiple path components to the URL, with a hint for handling directory awareness.
- [func appendPathComponent(String, conformingTo: UTType)](url/appendpathcomponent(_:conformingto:).md)
  Appends a path component to the URL that conforms to a uniform type identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/appendingpathcomponent(_:conformingto:))*