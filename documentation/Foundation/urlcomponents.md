# URLComponents

**Framework**: Foundation  
**Kind**: struct

A structure that parses URLs into and constructs URLs from their constituent parts.

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
struct URLComponents
```

#### Overview

This structure parses and constructs URLs according to [`RFC 3986`](https://developer.apple.comhttp://www.ietf.org/rfc/rfc3986.txt). Its behavior differs subtly from that of the [`URL`](url.md) structure, which conforms to older RFCs. However, you can easily obtain a [`URL`](url.md) value based on the contents of a [`URLComponents`](urlcomponents.md) value or vice versa.

## Topics

### Creating URL components
- [init()](urlcomponents/init.md)
  Creates a URL components instance without defining any of the components.
- [init?(string: String)](urlcomponents/init(string:).md)
  Creates a URL components instance from a URL string.
- [init?(string: String, encodingInvalidCharacters: Bool)](urlcomponents/init(string:encodinginvalidcharacters:).md)
  Creates a URL components instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
- [init?(url: URL, resolvingAgainstBaseURL: Bool)](urlcomponents/init(url:resolvingagainstbaseurl:).md)
  Creates a URL components instance from a URL string, optionally resolving against a base URL.
### Getting the URL
- [var url: URL?](urlcomponents/url.md)
  A URL created from the components.
- [func url(relativeTo: URL?) -> URL?](urlcomponents/url(relativeto:).md)
  Returns a URL based on the component settings and relative to a given base URL.
- [var string: String?](urlcomponents/string.md)
  A URL derived from the components object, in string form.
### Accessing components in native format
- [var fragment: String?](urlcomponents/fragment.md)
  The fragment subcomponent.
- [var host: String?](urlcomponents/host.md)
  The host subcomponent.
- [var encodedHost: String?](urlcomponents/encodedhost.md)
  The host subcomponent, percent-encoded.
- [var password: String?](urlcomponents/password.md)
  The password subcomponent of the URL.
- [var path: String](urlcomponents/path.md)
  The path subcomponent.
- [var port: Int?](urlcomponents/port.md)
  The port subcomponent.
- [var query: String?](urlcomponents/query.md)
  The query subcomponent.
- [var queryItems: [URLQueryItem]?](urlcomponents/queryitems.md)
  An array of query items for the URL in the order in which they appear in the original query string.
- [var scheme: String?](urlcomponents/scheme.md)
  The scheme subcomponent of the URL.
- [var user: String?](urlcomponents/user.md)
  The user subcomponent of the URL.
### Accessing components in URL-encoded format
- [var percentEncodedFragment: String?](urlcomponents/percentencodedfragment.md)
  The fragment subcomponent, percent-encoded.
- [var percentEncodedHost: String?](urlcomponents/percentencodedhost.md)
  The host subcomponent, percent-encoded.
- [var percentEncodedPassword: String?](urlcomponents/percentencodedpassword.md)
  The password subcomponent, percent-encoded.
- [var percentEncodedPath: String](urlcomponents/percentencodedpath.md)
  The path subcomponent, percent-encoded.
- [var percentEncodedQuery: String?](urlcomponents/percentencodedquery.md)
  The query subcomponent, percent-encoded.
- [var percentEncodedQueryItems: [URLQueryItem]?](urlcomponents/percentencodedqueryitems.md)
  The query subcomponent, as an array of percent-encoded query items.
- [struct URLQueryItem](urlqueryitem.md)
  A single name-value pair from the query portion of a URL.
- [var percentEncodedUser: String?](urlcomponents/percentencodeduser.md)
  The user subcomponent, percent-encoded.
### Locating components in the URL string representation
- [var rangeOfFragment: Range<String.Index>?](urlcomponents/rangeoffragment.md)
  Returns the character range of the fragment in the string returned by the string property.
- [var rangeOfHost: Range<String.Index>?](urlcomponents/rangeofhost.md)
  Returns the character range of the host in the string returned by the string property.
- [var rangeOfPassword: Range<String.Index>?](urlcomponents/rangeofpassword.md)
  Returns the character range of the password in the string returned by the string property.
- [var rangeOfPath: Range<String.Index>?](urlcomponents/rangeofpath.md)
  Returns the character range of the path in the string returned by the string property.
- [var rangeOfPort: Range<String.Index>?](urlcomponents/rangeofport.md)
  Returns the character range of the port in the string returned by the string property.
- [var rangeOfQuery: Range<String.Index>?](urlcomponents/rangeofquery.md)
  Returns the character range of the query in the string returned by the string property.
- [var rangeOfScheme: Range<String.Index>?](urlcomponents/rangeofscheme.md)
  Returns the character range of the scheme in the string returned by the string property.
- [var rangeOfUser: Range<String.Index>?](urlcomponents/rangeofuser.md)
  Returns the character range of the user in the string returned by the string property.
### Using reference types
- [class NSURLComponents](nsurlcomponents.md)
  An object that parses URLs into and constructs URLs from their constituent parts.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [ReferenceConvertible](referenceconvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct URL](url.md)
  A value that identifies the location of a resource, such as an item on a remote server or the path to a local file.
- [struct URLQueryItem](urlqueryitem.md)
  A single name-value pair from the query portion of a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcomponents)*