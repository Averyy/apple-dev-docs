# pirPrivacyPassIssuerURL

**Framework**: Network Extension  
**Kind**: property

A URL that contains the domain name of Privacy Pass issuer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
var pirPrivacyPassIssuerURL: URL? { get }
```

## See Also

- [var pirServerURL: URL?](neurlfiltermanager/pirserverurl.md)
  A URL that contains the domain name of the PIR server.
- [var pirAuthenticationToken: String?](neurlfiltermanager/pirauthenticationtoken.md)
  A PIR per-user authentication token string.
- [func refreshPIRParameters() async throws](neurlfiltermanager/refreshpirparameters.md)
  Refetches PIR parameters from the server.
- [func resetPIRCache() async throws](neurlfiltermanager/resetpircache.md)
  Resets the PIR on-device cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/pirprivacypassissuerurl)*