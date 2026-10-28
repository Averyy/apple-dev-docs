# originURL

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

An NSURL or `NSString` object containing the URL that set this cookie.

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
static let originURL: HTTPCookiePropertyKey
```

```c
extern NSHTTPCookiePropertyKey const NSHTTPCookieOriginURL;
```

## Discussion

If you do not provide a value for `NSHTTPCookieOriginURL`, you must provide a value for `NSHTTPCookieDomain`.

## See Also

### Cookie property keys
- [static let comment: HTTPCookiePropertyKey](./comment.md)
  An `NSString` object containing the comment for the cookie.
- [static let commentURL: HTTPCookiePropertyKey](./commenturl.md)
  An `NSURL` object or `NSString` object containing the comment URL for the cookie.
- [static let discard: HTTPCookiePropertyKey](./discard.md)
  An `NSString` object stating whether the cookie should be discarded at the end of the session.
- [static let domain: HTTPCookiePropertyKey](./domain.md)
  An `NSString` object containing the domain for the cookie.
- [static let expires: HTTPCookiePropertyKey](./expires.md)
  An `NSDate` object or `NSString` object specifying the expiration date for the cookie.
- [static let maximumAge: HTTPCookiePropertyKey](./maximumage.md)
  An `NSString` object containing an integer value stating how long in seconds the cookie should be kept, at most.
- [static let name: HTTPCookiePropertyKey](./name.md)
  An `NSString` object containing the name of the cookie (required).
- [static let path: HTTPCookiePropertyKey](./path.md)
  An `NSString` object containing the path for the cookie.
- [static let port: HTTPCookiePropertyKey](./port.md)
  An `NSString` object containing comma-separated integer values specifying the ports for the cookie.
- [static let sameSitePolicy: HTTPCookiePropertyKey](./samesitepolicy.md)
  A string indicating the same-site policy for the cookie.
- [static let secure: HTTPCookiePropertyKey](./secure.md)
  An `NSString` object indicating that the cookie should be transmitted only over secure channels.
- [static let value: HTTPCookiePropertyKey](./value.md)
  An `NSString` object containing the value of the cookie.
- [static let version: HTTPCookiePropertyKey](./version.md)
  An `NSString` object that specifies the version of the cookie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookiepropertykey/originurl)*