# query(percentEncoded:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the query component of the URL, optionally removing any percent-encoding.

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
func query(percentEncoded: Bool = true) -> String?
```

## Return Value

The query component of the URL, optionally percent-encoding any unreserved characters.

## Discussion

The system doesn’t allow certain characters in the URL query component, so [`URL`](../url.md) percent-encodes those characters to create a valid URL. Calling this function with `percentEncoded = false` removes any percent-encoding and returns the unencoded query.

If the URL doesn’t contain a query component according to [RFC 3986](https://www.ietf.org/rfc/rfc3986.txt), this function returns `nil`.

## Parameters

- `percentEncoded`: A Boolean value that indicates whether the URL percent-encodes any unreserved characters. Defaults to `true`.

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
- [var query: String?](./query.md)
  The query of the URL if the URL conforms to RFC 3986; otherwise, nil.
- [var scheme: String?](./scheme.md)
  The scheme of the URL.
- [func user(percentEncoded: Bool) -> String?](./user%28percentencoded%29.md)
  Returns the user component of the URL, optionally removing any percent-encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/query(percentencoded:))*