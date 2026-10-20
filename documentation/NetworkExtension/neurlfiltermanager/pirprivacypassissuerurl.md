# pirPrivacyPassIssuerURL

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A URL that contains the domain name of Privacy Pass issuer.

**Availability**:
- iOS 26.0+ - Deprecated in 27.2
- iPadOS 26.0+ - Deprecated in 27.2
- Mac Catalyst 26.0+ - Deprecated in 27.2
- macOS 26.0+ - Deprecated in 27.2

> **Deprecated**: Set the PIR privacy pass-issuer URL in your information property list in the `NSPIRConfiguration` dictionary.

## Declaration

```swift
var pirPrivacyPassIssuerURL: URL? { get }
```

## See Also

### Working with a Private Information Retrieval server
- [var pirAuthenticationToken: String?](./pirauthenticationtoken.md)
  A PIR per-user authentication token string.
- [func refreshPIRParameters() async throws](./refreshpirparameters%28%29.md)
  Refetches PIR parameters from the server.
- [func resetPIRCache() async throws](./resetpircache%28%29.md)
  Resets the PIR on-device cache.
- [var pirServerURL: URL?](./pirserverurl.md)
  A URL that contains the domain name of the PIR server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/pirprivacypassissuerurl)*