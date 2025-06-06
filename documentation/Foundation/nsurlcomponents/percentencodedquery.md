# percentEncodedQuery

**Framework**: Foundation  
**Kind**: property

The query URL component expressed as a URL-encoded string, or `nil` if not present.

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
var percentEncodedQuery: String? { get set }
```

#### Discussion

For example, in the URL `http://www.example.com/index.php?key1=value1&key2=value2`, the query string is `key1=value1&key2=value2`.

If you set this value to something that is not a valid, percent-encoded string, this class throws an exception.

## See Also

- [var percentEncodedFragment: String?](nsurlcomponents/percentencodedfragment.md)
  The fragment URL component (the part after a `#` symbol) expressed as a URL-encoded string, or `nil` if not present.
- [var percentEncodedHost: String?](nsurlcomponents/percentencodedhost.md)
  The host URL subcomponent expressed as a URL-encoded string, or `nil` if not present.
- [var percentEncodedPassword: String?](nsurlcomponents/percentencodedpassword.md)
  The password URL subcomponent expressed as a URL-encoded string, or `nil` if not present.
- [var percentEncodedPath: String?](nsurlcomponents/percentencodedpath.md)
  The path URL component expressed as a URL-encoded string, or `nil` if not present.
- [var percentEncodedUser: String?](nsurlcomponents/percentencodeduser.md)
  The username URL subcomponent expressed as a URL-encoded string, or `nil` if not present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlcomponents/percentencodedquery)*