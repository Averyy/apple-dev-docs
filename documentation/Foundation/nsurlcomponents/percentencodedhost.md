# percentEncodedHost

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The host URL subcomponent expressed as a URL-encoded string, or `nil` if not present.

**Availability**:
- iOS 7.0+ - Deprecated in 27.2
- iPadOS 7.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.9+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use encodedHost instead

## Declaration

```swift
var percentEncodedHost: String? { get set }
```

```objc
@property (copy, nullable) NSString * percentEncodedHost;
```

#### Discussion

For example, in the URL `http://www.example.com/index.html`, the host is `www.example.com`.

If you set this value to something that is not a valid, percent-encoded string, this class throws an exception.

## See Also

### Accessing components in URL-encoded format
- [var percentEncodedFragment: String?](./percentencodedfragment.md)
  The fragment URL component (the part after a `#` symbol) expressed as a URL-encoded string, or `nil` if not present.
- [var percentEncodedPassword: String?](./percentencodedpassword.md)
  The password URL subcomponent expressed as a URL-encoded string, or `nil` if not present.
- [var percentEncodedPath: String?](./percentencodedpath.md)
  The path URL component expressed as a URL-encoded string, or `nil` if not present.
- [var percentEncodedQuery: String?](./percentencodedquery.md)
  The query URL component expressed as a URL-encoded string, or `nil` if not present.
- [var percentEncodedUser: String?](./percentencodeduser.md)
  The username URL subcomponent expressed as a URL-encoded string, or `nil` if not present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlcomponents/percentencodedhost)*