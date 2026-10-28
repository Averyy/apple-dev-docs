# httpShouldSetCookies

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether requests should contain cookies from the cookie store.

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
var httpShouldSetCookies: Bool { get set }
```

```objc
@property BOOL HTTPShouldSetCookies;
```

## Discussion

This property controls whether tasks within sessions based on this configuration should automatically provide cookies from the shared cookie store when making requests.

If you want to provide cookies yourself, set this value to [`false`](../../Swift/false.md) and provide a `Cookie` header either through the session’s [`httpAdditionalHeaders`](./httpadditionalheaders.md) property or on a per-request level using a custom [`NSURLRequest`](../nsurlrequest.md) object.

The default value is [`true`](../../Swift/true.md).

## See Also

### Setting cookie policies
- [var httpCookieAcceptPolicy: HTTPCookie.AcceptPolicy](./httpcookieacceptpolicy.md)
  A policy constant that determines when cookies should be accepted.
- [var httpCookieStorage: HTTPCookieStorage?](./httpcookiestorage.md)
  The cookie store for storing cookies within this session.
- [class HTTPCookie](../httpcookie.md)
  A representation of an HTTP cookie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/httpshouldsetcookies)*