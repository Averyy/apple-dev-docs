# path

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The path URL component, or nil if not present.

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
var path: String? { get set }
```

```objc
@property (copy, nullable) NSString * path;
```

#### Discussion

For example, in the URL `http://www.example.com/index.html`, the path is `/index.html`.

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
- [var port: NSNumber?](./port.md)
  The port number URL component, or nil if not present.
- [var query: String?](./query.md)
  The query URL component as a string, or nil if not present.
- [var queryItems: [URLQueryItem]?](./queryitems.md)
  The query URL component as an array of name/value pairs.
- [var scheme: String?](./scheme.md)
  The scheme URL component, or nil if not present.
- [var user: String?](./user.md)
  The username URL subcomponent, or nil if not present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlcomponents/path)*