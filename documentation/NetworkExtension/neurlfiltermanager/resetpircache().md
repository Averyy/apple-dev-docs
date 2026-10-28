# resetPIRCache()

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Resets the PIR on-device cache.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
func resetPIRCache() async throws
```

## Discussion

The PIR system on device caches previous PIR queries and responses to minimize exchanges with the PIR server. When there is a dataset change on the PIR server, perform a reset of the on-device cache to avoid using stale cache entries.

## See Also

### Working with a Private Information Retrieval server
- [var pirAuthenticationToken: String?](./pirauthenticationtoken.md)
  A PIR per-user authentication token string.
- [func refreshPIRParameters() async throws](./refreshpirparameters%28%29.md)
  Refetches PIR parameters from the server.
- [var pirServerURL: URL?](./pirserverurl.md)
  A URL that contains the domain name of the PIR server.
- [var pirPrivacyPassIssuerURL: URL?](./pirprivacypassissuerurl.md)
  A URL that contains the domain name of Privacy Pass issuer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/resetpircache())*