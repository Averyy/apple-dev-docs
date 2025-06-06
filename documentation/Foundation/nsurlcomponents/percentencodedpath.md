# percentEncodedPath

**Framework**: Foundation  
**Kind**: property

The path URL component expressed as a URL-encoded string, or `nil` if not present.

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
var percentEncodedPath: String? { get set }
```

#### Discussion

For example, in the URL `http://www.example.com/index.html`, the path is `/index.html`.

If you set this value to something that is not a valid, percent-encoded string, this class throws an exception.

> **Note**:  Although an unencoded semicolon is a valid character in a percent-encoded path, for compatibility with the [`NSURL`](nsurl.md) class, you should always percent-encode it. To properly encode a string for use in the path component of a URL, use the character set returned by the `URLPathAllowedCharacterSet` method in conjunction with the [`addingPercentEncoding(withAllowedCharacters:)`](nsstring/addingpercentencoding(withallowedcharacters:).md) method.

## See Also

- [var percentEncodedFragment: String?](nsurlcomponents/percentencodedfragment.md)
  The fragment URL component (the part after a `#` symbol) expressed as a URL-encoded string, or `nil` if not present.
- [var percentEncodedHost: String?](nsurlcomponents/percentencodedhost.md)
  The host URL subcomponent expressed as a URL-encoded string, or `nil` if not present.
- [var percentEncodedPassword: String?](nsurlcomponents/percentencodedpassword.md)
  The password URL subcomponent expressed as a URL-encoded string, or `nil` if not present.
- [var percentEncodedQuery: String?](nsurlcomponents/percentencodedquery.md)
  The query URL component expressed as a URL-encoded string, or `nil` if not present.
- [var percentEncodedUser: String?](nsurlcomponents/percentencodeduser.md)
  The username URL subcomponent expressed as a URL-encoded string, or `nil` if not present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlcomponents/percentencodedpath)*