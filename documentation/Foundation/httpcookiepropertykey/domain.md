# domain

**Framework**: Foundation  
**Kind**: property

An `NSString` object containing the domain for the cookie.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let domain: HTTPCookiePropertyKey
```

#### Discussion

If this cookie attribute is missing, the domain is inferred from the value for `NSHTTPCookieOriginURL`. If you do not specify a value for `NSHTTPCookieOriginURL`, you  specify a value for `NSHTTPCookieDomain`.

## See Also

- [static let comment: HTTPCookiePropertyKey](httpcookiepropertykey/comment.md)
  An `NSString` object containing the comment for the cookie.
- [static let commentURL: HTTPCookiePropertyKey](httpcookiepropertykey/commenturl.md)
  An `NSURL` object or `NSString` object containing the comment URL for the cookie.
- [static let discard: HTTPCookiePropertyKey](httpcookiepropertykey/discard.md)
  An `NSString` object stating whether the cookie should be discarded at the end of the session.
- [static let expires: HTTPCookiePropertyKey](httpcookiepropertykey/expires.md)
  An `NSDate` object or `NSString` object specifying the expiration date for the cookie.
- [static let maximumAge: HTTPCookiePropertyKey](httpcookiepropertykey/maximumage.md)
  An `NSString` object containing an integer value stating how long in seconds the cookie should be kept, at most.
- [static let name: HTTPCookiePropertyKey](httpcookiepropertykey/name.md)
  An `NSString` object containing the name of the cookie (required).
- [static let originURL: HTTPCookiePropertyKey](httpcookiepropertykey/originurl.md)
  An NSURL or `NSString` object containing the URL that set this cookie.
- [static let path: HTTPCookiePropertyKey](httpcookiepropertykey/path.md)
  An `NSString` object containing the path for the cookie.
- [static let port: HTTPCookiePropertyKey](httpcookiepropertykey/port.md)
  An `NSString` object containing comma-separated integer values specifying the ports for the cookie.
- [static let sameSitePolicy: HTTPCookiePropertyKey](httpcookiepropertykey/samesitepolicy.md)
  A string indicating the same-site policy for the cookie.
- [static let secure: HTTPCookiePropertyKey](httpcookiepropertykey/secure.md)
  An `NSString` object indicating that the cookie should be transmitted only over secure channels.
- [static let value: HTTPCookiePropertyKey](httpcookiepropertykey/value.md)
  An `NSString` object containing the value of the cookie.
- [static let version: HTTPCookiePropertyKey](httpcookiepropertykey/version.md)
  An `NSString` object that specifies the version of the cookie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookiepropertykey/domain)*