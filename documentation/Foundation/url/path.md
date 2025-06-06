# path

**Framework**: Foundation  
**Kind**: property

The path component of the URL if the URL conforms to RFC 3986; otherwise, an empty string.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var path: String { get }
```

#### Return Value

The path, or an empty string if the URL has an empty path.

#### Discussion

> **Note**:  This function resolves against the base `URL`.

New code should use [`path(percentEncoded:)`](url/path(percentencoded:).md) instead of this property.

## See Also

- [func fragment(percentEncoded: Bool) -> String?](url/fragment(percentencoded:).md)
  Returns the fragment component of the URL, optionally removing any percent-encoding.
- [var fragment: String?](url/fragment.md)
  The fragment component of the URL if the URL conforms to RFC 3986; otherwise, nil.
- [func host(percentEncoded: Bool) -> String?](url/host(percentencoded:).md)
  Returns the host component of the URL, optionally removing any percent-encoding.
- [var host: String?](url/host.md)
  The host component of a URL if the URL conforms to RFC 3986; otherwise, nil.
- [var lastPathComponent: String](url/lastpathcomponent.md)
  The last path component of the URL, or an empty string if the path is an empty string.
- [func path(percentEncoded: Bool) -> String](url/path(percentencoded:).md)
  Returns the path component of the URL, optionally removing any percent-encoding.
- [func password(percentEncoded: Bool) -> String?](url/password(percentencoded:).md)
  Returns the password component of the URL, optionally removing any percent-encoding.
- [var password: String?](url/password.md)
  The password component of the URL if the URL conforms to RFC 3986; otherwise, nil.
- [var pathComponents: [String]](url/pathcomponents.md)
  The path components of the URL, or an empty array if the path is an empty string.
- [var pathExtension: String](url/pathextension.md)
  The path extension of the URL, or an empty string if the path is an empty string.
- [var port: Int?](url/port.md)
  The port component of the URL if the URL conforms to RFC 3986; otherwise, nil.
- [func query(percentEncoded: Bool) -> String?](url/query(percentencoded:).md)
  Returns the query component of the URL, optionally removing any percent-encoding.
- [var query: String?](url/query.md)
  The query of the URL if the URL conforms to RFC 3986; otherwise, nil.
- [var scheme: String?](url/scheme.md)
  The scheme of the URL.
- [func user(percentEncoded: Bool) -> String?](url/user(percentencoded:).md)
  Returns the user component of the URL, optionally removing any percent-encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/path)*