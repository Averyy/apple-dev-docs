# user(percentEncoded:)

**Framework**: Foundation  
**Kind**: method

Returns the user component of the URL, optionally removing any percent-encoding.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func user(percentEncoded: Bool = true) -> String?
```

#### Return Value

The system doesn’t allow certain characters in the URL user component, so [`URL`](url.md) percent-encodes those characters to create a valid URL. Calling this function with `percentEncoded = false` removes any percent-encoding and returns the unencoded user.

If the URL doesn’t contain a user component according to [`RFC 3986`](https://developer.apple.comhttps://www.ietf.org/rfc/rfc3986.txt), this function returns `nil`.

## Parameters

- `percentEncoded`: A Boolean value that indicates whether the URL percent-encodes any unreserved characters. Defaults to  .

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
- [var path: String](url/path.md)
  The path component of the URL if the URL conforms to RFC 3986; otherwise, an empty string.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/user(percentencoded:))*