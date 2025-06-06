# scheme

**Framework**: Foundation  
**Kind**: property

The scheme. (read-only)

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
var scheme: String? { get }
```

#### Discussion

This property contains the scheme. Any percent-encoded characters are not unescaped. For example, in the URL `http://www.example.com/index.html`, the scheme is `http`.

The full URL is the concatenation of the scheme, a colon (`:`), and the value of [`resourceSpecifier`](nsurl/resourcespecifier.md).

> **Note**:  The term “protocol” is also sometimes used when talking about network-based URL schemes. However, not all URL schemes are networking protocols—`data://` URLs, for example.

 The term “protocol” is also sometimes used when talking about network-based URL schemes. However, not all URL schemes are networking protocols—`data://` URLs, for example.

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/scheme)*