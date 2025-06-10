# resetPIRCache()

**Framework**: Network Extension  
**Kind**: method

Resets the PIR on-device cache.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
func resetPIRCache() async throws
```

#### Discussion

The PIR system on device caches previous PIR queries and responses to minimize exchanges with the PIR server. When there is a dataset change on the PIR server, perform a reset of the on-device cache to avoid using stale cache entries.

## See Also

- [var pirServerURL: URL?](neurlfiltermanager/pirserverurl.md)
  A URL that contains the domain name of the PIR server.
- [var pirPrivacyPassIssuerURL: URL?](neurlfiltermanager/pirprivacypassissuerurl.md)
  A URL that contains the domain name of Privacy Pass issuer.
- [var pirAuthenticationToken: String?](neurlfiltermanager/pirauthenticationtoken.md)
  A PIR per-user authentication token string.
- [func refreshPIRParameters() async throws](neurlfiltermanager/refreshpirparameters.md)
  Refetches PIR parameters from the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/resetpircache())*