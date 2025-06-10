# httpCookieAcceptPolicy

**Framework**: Foundation  
**Kind**: property

A policy constant that determines when cookies should be accepted.

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
var httpCookieAcceptPolicy: HTTPCookie.AcceptPolicy { get set }
```

#### Discussion

This property determines the cookie accept policy for all tasks within sessions based on this configuration.

The default value is [`HTTPCookie.AcceptPolicy.onlyFromMainDocumentDomain`](httpcookie/acceptpolicy/onlyfrommaindocumentdomain.md). You can change it to any of the constants defined in the [`HTTPCookie.AcceptPolicy`](httpcookie/acceptpolicy.md) enumerated type.

If you want more direct control over what cookies are accepted, set this value to [`HTTPCookie.AcceptPolicy.never`](httpcookie/acceptpolicy/never.md) and then use the [`allHeaderFields`](httpurlresponse/allheaderfields.md) and [`cookies(withResponseHeaderFields:for:)`](httpcookie/cookies(withresponseheaderfields:for:).md) methods to extract cookies from the URL response object yourself.

## See Also

- [var httpShouldSetCookies: Bool](urlsessionconfiguration/httpshouldsetcookies.md)
  A Boolean value that determines whether requests should contain cookies from the cookie store.
- [var httpCookieStorage: HTTPCookieStorage?](urlsessionconfiguration/httpcookiestorage.md)
  The cookie store for storing cookies within this session.
- [class HTTPCookie](httpcookie.md)
  A representation of an HTTP cookie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/httpcookieacceptpolicy)*