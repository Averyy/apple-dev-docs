# pirAuthenticationToken

**Framework**: Network Extension  
**Kind**: property

A PIR per-user authentication token string.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
var pirAuthenticationToken: String? { get }
```

#### Discussion

This value is an HTTP bearer token that authenticates the person using your app. The system uses this token to attest that it is a valid user when requesting anonymous authentication tokens.

## See Also

- [var pirServerURL: URL?](neurlfiltermanager/pirserverurl.md)
  A URL that contains the domain name of the PIR server.
- [var pirPrivacyPassIssuerURL: URL?](neurlfiltermanager/pirprivacypassissuerurl.md)
  A URL that contains the domain name of Privacy Pass issuer.
- [func refreshPIRParameters() async throws](neurlfiltermanager/refreshpirparameters.md)
  Refetches PIR parameters from the server.
- [func resetPIRCache() async throws](neurlfiltermanager/resetpircache.md)
  Resets the PIR on-device cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/pirauthenticationtoken)*