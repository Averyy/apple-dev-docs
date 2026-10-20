# fragment

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The fragment component of the URL if the URL conforms to RFC 3986; otherwise, nil.

**Availability**:
- iOS 8.0+ - Deprecated in 27.2
- iPadOS 8.0+ - Deprecated in 27.2
- Mac Catalyst 8.0+ - Deprecated in 27.2
- macOS 10.10+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use fragment(percentEncoded:) instead

## Declaration

```swift
var fragment: String? { get }
```

#### Discussion

> **Note**:  This function resolves against the base `URL`.

New code should use [`fragment(percentEncoded:)`](./fragment%28percentencoded%29.md) instead of this property.

## See Also

### Accessing the parts of a URL
- [func fragment(percentEncoded: Bool) -> String?](./fragment%28percentencoded%29.md)
  Returns the fragment component of the URL, optionally removing any percent-encoding.
- [func host(percentEncoded: Bool) -> String?](./host%28percentencoded%29.md)
  Returns the host component of the URL, optionally removing any percent-encoding.
- [var host: String?](./host.md)
  The host component of a URL if the URL conforms to RFC 3986; otherwise, nil.
- [var lastPathComponent: String](./lastpathcomponent.md)
  The last path component of the URL, or an empty string if the path is an empty string.
- [func path(percentEncoded: Bool) -> String](./path%28percentencoded%29.md)
  Returns the path component of the URL, optionally removing any percent-encoding.
- [var path: String](./path.md)
  The path component of the URL if the URL conforms to RFC 3986; otherwise, an empty string.
- [func password(percentEncoded: Bool) -> String?](./password%28percentencoded%29.md)
  Returns the password component of the URL, optionally removing any percent-encoding.
- [var password: String?](./password.md)
  The password component of the URL if the URL conforms to RFC 3986; otherwise, nil.
- [var pathComponents: [String]](./pathcomponents.md)
  The path components of the URL, or an empty array if the path is an empty string.
- [var pathExtension: String](./pathextension.md)
  The path extension of the URL, or an empty string if the path is an empty string.
- [var port: Int?](./port.md)
  The port component of the URL if the URL conforms to RFC 3986; otherwise, nil.
- [func query(percentEncoded: Bool) -> String?](./query%28percentencoded%29.md)
  Returns the query component of the URL, optionally removing any percent-encoding.
- [var query: String?](./query.md)
  The query of the URL if the URL conforms to RFC 3986; otherwise, nil.
- [var scheme: String?](./scheme.md)
  The scheme of the URL.
- [func user(percentEncoded: Bool) -> String?](./user%28percentencoded%29.md)
  Returns the user component of the URL, optionally removing any percent-encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/fragment)*