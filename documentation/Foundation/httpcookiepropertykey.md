# HTTPCookiePropertyKey

**Framework**: Foundation  
**Kind**: struct

Constants that define the supported keys in a cookie attributes dictionary.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct HTTPCookiePropertyKey
```

## Topics

### Cookie property keys
- [static let comment: HTTPCookiePropertyKey](httpcookiepropertykey/comment.md)
  An `NSString` object containing the comment for the cookie.
- [static let commentURL: HTTPCookiePropertyKey](httpcookiepropertykey/commenturl.md)
  An `NSURL` object or `NSString` object containing the comment URL for the cookie.
- [static let discard: HTTPCookiePropertyKey](httpcookiepropertykey/discard.md)
  An `NSString` object stating whether the cookie should be discarded at the end of the session.
- [static let domain: HTTPCookiePropertyKey](httpcookiepropertykey/domain.md)
  An `NSString` object containing the domain for the cookie.
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
### Creating custom cookie property keys
- [init(String)](httpcookiepropertykey/init(_:).md)
  Creates an HTTP cookie property key using the given string.
- [init(rawValue: String)](httpcookiepropertykey/init(rawvalue:).md)
  Creates an HTTP cookie property key using the given string.
### Type Properties
- [static let setByJavaScript: HTTPCookiePropertyKey](httpcookiepropertykey/setbyjavascript.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var properties: [HTTPCookiePropertyKey : Any]?](httpcookie/properties.md)
  The cookie’s properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookiepropertykey)*