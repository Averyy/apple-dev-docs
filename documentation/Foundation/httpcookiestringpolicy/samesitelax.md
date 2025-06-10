# sameSiteLax

**Framework**: Foundation  
**Kind**: property

A policy that allows certain cross-site requests to include the cookie.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static let sameSiteLax: HTTPCookieStringPolicy
```

#### Discussion

When a cookie has this policy, a request includes the cookie if the request is “top-level,”, meaning one that changes the URL in the address bar.

## See Also

- [static let sameSiteStrict: HTTPCookieStringPolicy](httpcookiestringpolicy/samesitestrict.md)
  A policy that prohibits a cross-site request from including the cookie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookiestringpolicy/samesitelax)*