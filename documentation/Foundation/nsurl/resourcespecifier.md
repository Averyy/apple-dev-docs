# resourceSpecifier

**Framework**: Foundation  
**Kind**: property

The resource specifier. (read-only)

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var resourceSpecifier: String? { get }
```

#### Discussion

This property contains the resource specifier. Any percent-encoded characters are not unescaped. For example, in the URL `http://www.example.com/index.html?key1=value1#jumplink`, the resource specifier is `//www.example.com/index.html?key1=value1#jumplink` (everything after the colon).

> ❗ **Important**:  If the receiver does not specify a net location portion of the URL, as returned by the toll-free bridged `CFURL` function [`CFURLCopyNetLocation(_:)`](https://developer.apple.com/documentation/CoreFoundation/CFURLCopyNetLocation(_:)), then this method returns only the path of the receiver. For example, in the URL `file:///file.txt`, the resource specifier is `/file.txt`.

## See Also

- [var absoluteString: String?](nsurl/absolutestring.md)
  The URL string for the receiver as an absolute URL. (read-only)
- [var absoluteURL: URL?](nsurl/absoluteurl.md)
  An absolute URL that refers to the same resource as the receiver. (read-only)
- [var baseURL: URL?](nsurl/baseurl.md)
  The base URL. (read-only)
- [var fileSystemRepresentation: UnsafePointer<CChar>](nsurl/filesystemrepresentation.md)
  A C string containing the URL’s file system path. (read-only)
- [var fragment: String?](nsurl/fragment.md)
  The fragment identifier, conforming to RFC 1808. (read-only)
- [var host: String?](nsurl/host.md)
  The host, conforming to RFC 1808. (read-only)
- [var lastPathComponent: String?](nsurl/lastpathcomponent.md)
  The last path component. (read-only)
- [var parameterString: String?](nsurl/parameterstring.md)
  The parameter string conforming to RFC 1808. (read-only)
- [var password: String?](nsurl/password.md)
  The password conforming to RFC 1808. (read-only)
- [var path: String?](nsurl/path.md)
  The path, conforming to RFC 1808. (read-only)
- [var pathComponents: [String]?](nsurl/pathcomponents.md)
  An array containing the  path components. (read-only)
- [var pathExtension: String?](nsurl/pathextension.md)
  The path extension. (read-only)
- [var port: NSNumber?](nsurl/port.md)
  The port, conforming to RFC 1808.
- [var query: String?](nsurl/query.md)
  The query string, conforming to RFC 1808.
- [var relativePath: String?](nsurl/relativepath.md)
  The relative path, conforming to RFC 1808. (read-only)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/resourcespecifier)*