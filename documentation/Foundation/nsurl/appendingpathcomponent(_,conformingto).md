# appendingPathComponent(_:conformingTo:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a URL by appending the specified path component with the file extension for a uniform type identifier.

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

```objc
- (NSURL *) URLByAppendingPathComponent:(NSString *) partialName conformingToType:(UTType *) contentType;
```

## Return Value

A new URL with the partial name and the type’s preferred extension appended.

## Discussion

Use this method when you want to mix partial input from a user or other source, and need to produce a complete filename suitable for that input. For example, if you download a file from the internet and know its MIME type, you can use this method to ensure the URL has the correct filename extension where you save the file.

If `partialName` already has a path extension, and that path extension is valid for file system objects of type `contentType`, the function doesn’t add an extension before appending it to the URL. For example, if the inputs are `puppy.jpg` and [`image`](../../UniformTypeIdentifiers/uttype-swift.struct/image.md), respectively, the function returns a URL with an appended path component of `puppy.jpg`. However, if the inputs are `puppy.jpg` and [`plainText`](../../UniformTypeIdentifiers/uttype-swift.struct/plaintext.md), respectively, the function returns a URL with an appended path component of `puppy.jpg.txt`. If you want to replace any existing path extension, use the [`deletePathExtension()`](../url/deletepathextension%28%29.md) method first.

If the function can’t append the path component, it returns an unchanged URL.

> **Note**:  The modified URL has a directory path if `contentType` conforms to [`directory`](../../UniformTypeIdentifiers/uttype-swift.struct/directory.md).

For more information about types, see [Uniform Type Identifiers](../../UniformTypeIdentifiers/UniformTypeIdentifiers.md).

## Parameters

- `partialName`: The partial name to append.
- `contentType`: A uniform type identifier the resulting conforms to.

## See Also

### Modifying and Converting a File URL
- [var filePathURL: URL?](./filepathurl.md)
  A file path URL that points to the same resource as the URL object. (read-only)
- [func fileReferenceURL() -> URL?](./filereferenceurl%28%29.md)
  Returns a new file reference URL that points to the same resource as the receiver.
- [func appendingPathComponent(String) -> URL?](./appendingpathcomponent%28_%29.md)
  Returns a new URL by appending a path component to the original URL.
- [func appendingPathComponent(String, isDirectory: Bool) -> URL?](./appendingpathcomponent%28_,isdirectory%29.md)
  Returns a new URL by appending a path component to the original URL, along with a trailing slash if the component is a directory.
- [func appendingPathExtension(String) -> URL?](./appendingpathextension%28_%29.md)
  Returns a new URL by appending a path extension to the original URL.
- [func appendingPathExtension(for: UTType) -> URL](./appendingpathextension%28for%29.md)
  Returns a URL by appending the path extension for a uniform type identifier.
- [var deletingLastPathComponent: URL?](./deletinglastpathcomponent.md)
  A URL you create by removing the last path component from the receiver. (read-only)
- [var deletingPathExtension: URL?](./deletingpathextension.md)
  A URL you create by removing the path extension from the receiver, if any. (read-only)
- [var resolvingSymlinksInPath: URL?](./resolvingsymlinksinpath.md)
  A URL that points to the same resource as the receiver and includes no symbolic links. (read-only)
- [var standardizingPath: URL?](./standardizingpath.md)
  A URL that points to the same resource as the original URL using an absolute path. (read-only)
- [var hasDirectoryPath: Bool](./hasdirectorypath.md)
  A Boolean value that indicates whether the URL string’s path represents a directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/appendingpathcomponent(_:conformingto:))*