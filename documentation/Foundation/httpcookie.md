# HTTPCookie

**Framework**: Foundation  
**Kind**: class

A representation of an HTTP cookie.

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
class HTTPCookie
```

#### Overview

An [`HTTPCookie`](httpcookie.md) object is immutable, initialized from a dictionary that contains the attributes of the cookie. This class supports two different cookie versions:

- Version 0: The original cookie format defined by Netscape. Most cookies are in this format.
- Version 1: The cookie format defined in [`RFC 6265`](https://developer.apple.comhttps://tools.ietf.org/html/rfc6265), HTTP State Management Mechanism.

## Topics

### Creating cookies
- [class func cookies(withResponseHeaderFields: [String : String], for: URL) -> [HTTPCookie]](httpcookie/cookies(withresponseheaderfields:for:).md)
  Creates an array of HTTP cookies that corresponds to the provided response header fields for the provided URL.
- [init?(properties: [HTTPCookiePropertyKey : Any])](httpcookie/init(properties:).md)
  Initializes an HTTP cookie object with the given cookie properties.
### Converting cookies to request headers
- [class func requestHeaderFields(with: [HTTPCookie]) -> [String : String]](httpcookie/requestheaderfields(with:).md)
  Converts an array of cookies to a dictionary of header fields.
### Getting cookie host properties
- [var domain: String](httpcookie/domain.md)
  The domain of the cookie.
- [var path: String](httpcookie/path.md)
  The cookie’s path.
- [var portList: [NSNumber]?](httpcookie/portlist.md)
  The cookie’s port list.
### Getting cookie metadata
- [var name: String](httpcookie/name.md)
  The cookie’s name.
- [var value: String](httpcookie/value.md)
  The cookie’s string value.
- [var version: Int](httpcookie/version.md)
  The cookie’s version.
### Determining cookie lifespan
- [var expiresDate: Date?](httpcookie/expiresdate.md)
  The cookie’s expiration date.
- [var isSessionOnly: Bool](httpcookie/issessiononly.md)
  A Boolean value that indicates whether the cookie should be discarded at the end of the session (regardless of expiration date).
### Securing cookies
- [var isHTTPOnly: Bool](httpcookie/ishttponly.md)
  A Boolean value that indicates whether the cookie should only be sent to HTTP servers.
- [var isSecure: Bool](httpcookie/issecure.md)
  A Boolean value that indicates whether the cookie may only be sent over secure channels.
- [var sameSitePolicy: HTTPCookieStringPolicy?](httpcookie/samesitepolicy.md)
  A Boolean value that indicates whether to restrict the cookie to requests sent back to the same site that created it.
- [struct HTTPCookieStringPolicy](httpcookiestringpolicy.md)
  Values that indicate whether to restrict the cookie to requests sent back to the same site that created it.
### Accessing cookie properties as key-value pairs
- [var properties: [HTTPCookiePropertyKey : Any]?](httpcookie/properties.md)
  The cookie’s properties.
- [struct HTTPCookiePropertyKey](httpcookiepropertykey.md)
  Constants that define the supported keys in a cookie attributes dictionary.
### Getting user-readable cookie metadata
- [var comment: String?](httpcookie/comment.md)
  The cookie’s comment string.
- [var commentURL: URL?](httpcookie/commenturl.md)
  The cookie’s comment URL.
### Accepting cookies
- [HTTPCookie.AcceptPolicy](httpcookie/acceptpolicy.md)
  Cookie acceptance policies implemented by the [`HTTPCookieStorage`](httpcookiestorage.md) class.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class HTTPCookieStorage](httpcookiestorage.md)
  A container that manages the storage of cookies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookie)*