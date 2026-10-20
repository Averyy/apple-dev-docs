# port

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The port number URL component, or nil if not present.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var port: NSNumber? { get set }
```

```objc
@property (copy, nullable) NSNumber * port;
```

#### Discussion

For example, in the URL `http://www.example.com:8080/index.php`, the port number is `8080`.

If you attempt to set the port to a negative port number, this class throws an exception.

## See Also

### Accessing components in native format
- [var fragment: String?](./fragment.md)
  The fragment URL component (the part after a `#` symbol), or nil if not present.
- [var host: String?](./host.md)
  The host URL subcomponent, or nil if not present.
- [var encodedHost: String?](./encodedhost.md)
  The host subcomponent, percent-encoded.
- [var password: String?](./password.md)
  The password URL subcomponent, or nil if not present.
- [var path: String?](./path.md)
  The path URL component, or nil if not present.
- [var query: String?](./query.md)
  The query URL component as a string, or nil if not present.
- [var queryItems: [URLQueryItem]?](./queryitems.md)
  The query URL component as an array of name/value pairs.
- [var scheme: String?](./scheme.md)
  The scheme URL component, or nil if not present.
- [var user: String?](./user.md)
  The username URL subcomponent, or nil if not present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlcomponents/port)*