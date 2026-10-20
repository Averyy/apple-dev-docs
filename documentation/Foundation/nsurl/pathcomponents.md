# pathComponents

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

An array containing the  path components. (read-only)

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
var pathComponents: [String]? { get }
```

```objc
@property (copy, readonly, nullable) NSArray<NSString *> * pathComponents;
```

#### Discussion

This property contains an array containing the individual path components of the URL, each unescaped using the [`replacingPercentEscapes(using:)`](../nsstring/replacingpercentescapes%28using%29.md) method. For example, in the URL `file:///directory/directory%202/file`, the path components array would be `@[@"/", @"directory", @"directory 2", @"file"]`.

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
- [var parameterString: String?](./parameterstring.md)
  The parameter string conforming to RFC 1808. (read-only)
- [var password: String?](./password.md)
  The password conforming to RFC 1808. (read-only)
- [var path: String?](./path.md)
  The path, conforming to RFC 1808. (read-only)
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/pathcomponents)*