# percentEncodedPassword

**Framework**: Foundation  
**Kind**: property

The password subcomponent, percent-encoded.

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
var percentEncodedPassword: String? { get set }
```

#### Discussion

The getter for this property retains any percent encoding this component may have. Setting this properties assumes the component string is already correctly percent encoded. Attempting to set an incorrectly percent encoded string will cause a `fatalError`. Although ‘;’ is a legal path character, it is recommended that it be percent-encoded for best compatibility with `URL` (`String.addingPercentEncoding(withAllowedCharacters:)` will percent-encode any ‘;’ characters if you pass `CharacterSet.urlPasswordAllowed`).

## See Also

- [var percentEncodedFragment: String?](urlcomponents/percentencodedfragment.md)
  The fragment subcomponent, percent-encoded.
- [var percentEncodedHost: String?](urlcomponents/percentencodedhost.md)
  The host subcomponent, percent-encoded.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcomponents/percentencodedpassword)*