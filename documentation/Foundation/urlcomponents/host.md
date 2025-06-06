# host

**Framework**: Foundation  
**Kind**: property

The host subcomponent.

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
var host: String? { get set }
```

#### Discussion

The getter for this property removes any percent encoding this component may have (if the component allows percent encoding). Setting this property assumes the subcomponent or component string is not percent encoded and will add percent encoding (if the component allows percent encoding).

## See Also

- [var fragment: String?](urlcomponents/fragment.md)
  The fragment subcomponent.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcomponents/host)*