# resolvingSymlinksInPath

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A URL that points to the same resource as the receiver and includes no symbolic links. (read-only)

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var resolvingSymlinksInPath: URL? { get }
```

```objc
@property (copy, readonly, nullable) NSURL * URLByResolvingSymlinksInPath;
```

#### Discussion

If the receiver has no symbolic links, this property contains a copy of the original URL.

If some symbolic links cannot be resolved, this property contains those broken symbolic links.

If the name of the receiving path begins with `/private`, this property strips off the `/private` designator, provided the result is the name of an existing file.

This property only works on URLs with the `file:` path scheme. For all other URLs, it contains a copy of the receiver.

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
- [func appendingPathComponent(String, conformingTo: UTType) -> URL](./appendingpathcomponent%28_,conformingto%29.md)
  Returns a URL by appending the specified path component with the file extension for a uniform type identifier.
- [func appendingPathExtension(String) -> URL?](./appendingpathextension%28_%29.md)
  Returns a new URL by appending a path extension to the original URL.
- [func appendingPathExtension(for: UTType) -> URL](./appendingpathextension%28for%29.md)
  Returns a URL by appending the path extension for a uniform type identifier.
- [var deletingLastPathComponent: URL?](./deletinglastpathcomponent.md)
  A URL you create by removing the last path component from the receiver. (read-only)
- [var deletingPathExtension: URL?](./deletingpathextension.md)
  A URL you create by removing the path extension from the receiver, if any. (read-only)
- [var standardizingPath: URL?](./standardizingpath.md)
  A URL that points to the same resource as the original URL using an absolute path. (read-only)
- [var hasDirectoryPath: Bool](./hasdirectorypath.md)
  A Boolean value that indicates whether the URL string’s path represents a directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/resolvingsymlinksinpath)*