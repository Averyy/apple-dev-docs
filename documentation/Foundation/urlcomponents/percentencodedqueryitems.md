# percentEncodedQueryItems

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The query subcomponent, as an array of percent-encoded query items.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var percentEncodedQueryItems: [URLQueryItem]? { get set }
```

#### Discussion

The setter combines an array containing any number of [`URLQueryItem`](../urlqueryitem.md) key-value pairs into a query string and sets the `URLComponents` query property. This property assumes the query item names and values are already correctly percent-encoded. It also assumes that the query item names don’t contain the query item delimiter characters `&` and `=`. Attempting to set an incorrectly percent-encoded query item or a query item name with the query item delimiter characters `&` and `=` raises [`fatalError(_:file:line:)`](../../Swift/fatalerror%28_,file,line%29.md).

## See Also

### Accessing components in URL-encoded format
- [var percentEncodedFragment: String?](./percentencodedfragment.md)
  The fragment subcomponent, percent-encoded.
- [var percentEncodedHost: String?](./percentencodedhost.md)
  The host subcomponent, percent-encoded.
- [var percentEncodedPassword: String?](./percentencodedpassword.md)
  The password subcomponent, percent-encoded.
- [var percentEncodedPath: String](./percentencodedpath.md)
  The path subcomponent, percent-encoded.
- [var percentEncodedQuery: String?](./percentencodedquery.md)
  The query subcomponent, percent-encoded.
- [struct URLQueryItem](../urlqueryitem.md)
  A single name-value pair from the query portion of a URL.
- [var percentEncodedUser: String?](./percentencodeduser.md)
  The user subcomponent, percent-encoded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcomponents/percentencodedqueryitems)*