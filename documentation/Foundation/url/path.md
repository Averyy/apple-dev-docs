# path

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The path component of the URL if the URL conforms to RFC 3986; otherwise, an empty string.

**Availability**:
- iOS 8.0+ - Deprecated in 27.2
- iPadOS 8.0+ - Deprecated in 27.2
- Mac Catalyst 8.0+ - Deprecated in 27.2
- macOS 10.10+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use path(percentEncoded:) instead

## Declaration

```swift
var path: String { get }
```

## Return Value

The path, or an empty string if the URL has an empty path.

## Discussion

> **Note**:  This function resolves against the base `URL`.

New code should use [`path(percentEncoded:)`](./path%28percentencoded%29.md) instead of this property.

## See Also

### Accessing the parts of a URL
- [func fragment(percentEncoded: Bool) -> String?](./fragment%28percentencoded%29.md)
  Returns the fragment component of the URL, optionally removing any percent-encoding.
- [var fragment: String?](./fragment.md)
  The fragment component of the URL if the URL conforms to RFC 3986; otherwise, nil.
- [func host(percentEncoded: Bool) -> String?](./host%28percentencoded%29.md)
  Returns the host component of the URL, optionally removing any percent-encoding.
- [var host: String?](./host.md)
  The host component of a URL if the URL conforms to RFC 3986; otherwise, nil.
- [var lastPathComponent: String](./lastpathcomponent.md)
  The last path component of the URL, or an empty string if the path is an empty string.
- [func path(percentEncoded: Bool) -> String](./path%28percentencoded%29.md)
  Returns the path component of the URL, optionally removing any percent-encoding.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/path)*