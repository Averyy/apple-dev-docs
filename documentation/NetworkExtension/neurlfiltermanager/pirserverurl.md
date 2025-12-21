# pirServerURL

**Framework**: Network Extension  
**Kind**: property

A URL that contains the domain name of the PIR server.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
var pirServerURL: URL? { get }
```

#### Discussion

Have your URL filter app implementation set up a PIR server, which hosts a URL dataset, that’s reachable at this URL. When making an HTTP request with any of the system networking frameworks, NetworkExtension validates the URL with the specified PIR server before sending the request.

To use the PIR server for URL filtering, make sure the server contains a PIR use case with the name format “.url.filtering” where  is the bundle identifier of your URL filter app.

## See Also

- [var pirPrivacyPassIssuerURL: URL?](neurlfiltermanager/pirprivacypassissuerurl.md)
  A URL that contains the domain name of Privacy Pass issuer.
- [var pirAuthenticationToken: String?](neurlfiltermanager/pirauthenticationtoken.md)
  A PIR per-user authentication token string.
- [func refreshPIRParameters() async throws](neurlfiltermanager/refreshpirparameters.md)
  Refetches PIR parameters from the server.
- [func resetPIRCache() async throws](neurlfiltermanager/resetpircache.md)
  Resets the PIR on-device cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/pirserverurl)*