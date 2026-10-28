# parameterString

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The parameter string conforming to RFC 1808. (read-only)

**Availability**:
- iOS 2.0+ - Deprecated in 13.0
- iPadOS 2.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.15
- tvOS 9.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 6.0

> **Deprecated**: The parameterString method is deprecated. Post deprecation for applications linked with or after the macOS 10.15, and for all iOS, watchOS, and tvOS applications, parameterString will always return nil, and the path method will return the complete path including the semicolon separator and params component if the URL string contains them.

## Declaration

```swift
var parameterString: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * parameterString;
```

## Discussion

This property contains the parameter string. Any percent-encoded characters are not unescaped. If the receiver does not conform to RFC 1808, this property contains `nil`.  For example, in the URL `file:///path/to/file;foo`, the parameter string is `foo`.

This property should not be confused with the [`query`](./query.md) property, which also often contains a string of parameters.

## See Also

### Accessing the Parts of the URL
- [var absoluteString: String?](./absolutestring.md)
  The URL string for the receiver as an absolute URL. (read-only)
- [var absoluteURL: URL?](./absoluteurl.md)
  An absolute URL that refers to the same resource as the receiver. (read-only)
- [var baseURL: URL?](./baseurl.md)
  The base URL. (read-only)
- [var fileSystemRepresentation: UnsafePointer<CChar>](./filesystemrepresentation.md)
  A C string containing the URL’s file system path. (read-only)
- [var fragment: String?](./fragment.md)
  The fragment identifier, conforming to RFC 1808. (read-only)
- [var host: String?](./host.md)
  The host, conforming to RFC 1808. (read-only)
- [var lastPathComponent: String?](./lastpathcomponent.md)
  The last path component. (read-only)
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/parameterstring)*