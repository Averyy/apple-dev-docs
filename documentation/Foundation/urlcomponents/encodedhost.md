# encodedHost

**Framework**: Foundation  
**Kind**: property

The host subcomponent, percent-encoded.

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
var encodedHost: String? { get set }
```

#### Discussion

The getter for this property retains any percent-encoding this component may have. Setting this property assumes the component string already has the correct percent-encoding. Attempting to set an incorrectly percent-encoded string raises [`fatalError(_:file:line:)`](https://developer.apple.com/documentation/Swift/fatalError(_:file:line:)).

## See Also

- [var fragment: String?](urlcomponents/fragment.md)
  The fragment subcomponent.
- [var host: String?](urlcomponents/host.md)
  The host subcomponent.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcomponents/encodedhost)*