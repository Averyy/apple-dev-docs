# fileSystemRepresentation

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A C string containing the URL’s file system path. (read-only)

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var fileSystemRepresentation: UnsafePointer<CChar> { get }
```

```objc
@property (readonly) const char * fileSystemRepresentation;
```

## Discussion

This returns a null-terminated C string in file system representation.

This string is automatically freed in the same way that a returned object would be released. The caller must either copy the string or use [`getFileSystemRepresentation(_:maxLength:)`](./getfilesystemrepresentation%28_,maxlength%29.md) if it needs to store the representation outside of the autorelease context in which the value was obtained.

The file system representation format is described in File Encodings and Fonts.

## See Also

### Accessing the Parts of the URL
- [var absoluteString: String?](./absolutestring.md)
  The URL string for the receiver as an absolute URL. (read-only)
- [var absoluteURL: URL?](./absoluteurl.md)
  An absolute URL that refers to the same resource as the receiver. (read-only)
- [var baseURL: URL?](./baseurl.md)
  The base URL. (read-only)
- [var fragment: String?](./fragment.md)
  The fragment identifier, conforming to RFC 1808. (read-only)
- [var host: String?](./host.md)
  The host, conforming to RFC 1808. (read-only)
- [var lastPathComponent: String?](./lastpathcomponent.md)
  The last path component. (read-only)
- [var parameterString: String?](./parameterstring.md)
  The parameter string conforming to RFC 1808. (read-only)
- [var password: String?](./password.md)
  The password conforming to RFC 1808. (read-only)
- [var path: String?](./path.md)
  The path, conforming to RFC 1808. (read-only)
- [var pathComponents: [String]?](./pathcomponents.md)
  An array containing the  path components. (read-only)
- [var pathExtension: String?](./pathextension.md)
  The path extension. (read-only)
- [var port: NSNumber?](./port.md)
  The port, conforming to RFC 1808.
- [var query: String?](./query.md)
  The query string, conforming to RFC 1808.
- [var relativePath: String?](./relativepath.md)
  The relative path, conforming to RFC 1808. (read-only)
- [var relativeString: String](./relativestring.md)
  A string representation of the relative portion of the URL. (read-only)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/filesystemrepresentation)*