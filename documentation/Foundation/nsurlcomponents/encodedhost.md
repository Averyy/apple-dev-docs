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

- [var fragment: String?](nsurlcomponents/fragment.md)
  The fragment URL component (the part after a `#` symbol), or nil if not present.
- [var host: String?](nsurlcomponents/host.md)
  The host URL subcomponent, or nil if not present.
- [var password: String?](nsurlcomponents/password.md)
  The password URL subcomponent, or nil if not present.
- [var path: String?](nsurlcomponents/path.md)
  The path URL component, or nil if not present.
- [var port: NSNumber?](nsurlcomponents/port.md)
  The port number URL component, or nil if not present.
- [var query: String?](nsurlcomponents/query.md)
  The query URL component as a string, or nil if not present.
- [var queryItems: [URLQueryItem]?](nsurlcomponents/queryitems.md)
  The query URL component as an array of name/value pairs.
- [var scheme: String?](nsurlcomponents/scheme.md)
  The scheme URL component, or nil if not present.
- [var user: String?](nsurlcomponents/user.md)
  The username URL subcomponent, or nil if not present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlcomponents/encodedhost)*