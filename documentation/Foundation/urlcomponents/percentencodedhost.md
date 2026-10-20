# percentEncodedHost

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The host subcomponent, percent-encoded.

**Availability**:
- iOS 8.0+ - Deprecated in 27.2
- iPadOS 8.0+ - Deprecated in 27.2
- Mac Catalyst 8.0+ - Deprecated in 27.2
- macOS 10.10+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [`encodedHost`](./encodedhost.md) instead.

## Declaration

```swift
var percentEncodedHost: String? { get set }
```

#### Discussion

The getter for this property retains any percent encoding this component may have. Setting this properties assumes the component string is already correctly percent encoded. Attempting to set an incorrectly percent encoded string will cause a `fatalError`. Although ‘;’ is a legal path character, it is recommended that it be percent-encoded for best compatibility with `URL` (`String.addingPercentEncoding(withAllowedCharacters:)` will percent-encode any ‘;’ characters if you pass `CharacterSet.urlHostAllowed`).

## See Also

### Accessing components in URL-encoded format
- [var percentEncodedFragment: String?](./percentencodedfragment.md)
  The fragment subcomponent, percent-encoded.
- [var percentEncodedPassword: String?](./percentencodedpassword.md)
  The password subcomponent, percent-encoded.
- [var percentEncodedPath: String](./percentencodedpath.md)
  The path subcomponent, percent-encoded.
- [var percentEncodedQuery: String?](./percentencodedquery.md)
  The query subcomponent, percent-encoded.
- [var percentEncodedQueryItems: [URLQueryItem]?](./percentencodedqueryitems.md)
  The query subcomponent, as an array of percent-encoded query items.
- [struct URLQueryItem](../urlqueryitem.md)
  A single name-value pair from the query portion of a URL.
- [var percentEncodedUser: String?](./percentencodeduser.md)
  The user subcomponent, percent-encoded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcomponents/percentencodedhost)*