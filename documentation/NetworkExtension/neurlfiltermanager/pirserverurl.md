# pirServerURL

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A URL that contains the domain name of the PIR server.

**Availability**:
- iOS 26.0+ - Deprecated in 27.2
- iPadOS 26.0+ - Deprecated in 27.2
- Mac Catalyst 26.0+ - Deprecated in 27.2
- macOS 26.0+ - Deprecated in 27.2

> **Deprecated**: Set the PIR server URL in your information property list in the `NSPIRConfiguration` dictionary.

## Declaration

```swift
var pirServerURL: URL? { get }
```

## Discussion

Have your URL filter app implementation set up a PIR server, which hosts a URL dataset, that’s reachable at this URL. When making an HTTP request with any of the system networking frameworks, NetworkExtension validates the URL with the specified PIR server before sending the request.

To use the PIR server for URL filtering, make sure the server contains a PIR use case with the name format “*bundleidentifier*.url.filtering” where *bundleidentifier* is the bundle identifier of your URL filter app.

## See Also

### Working with a Private Information Retrieval server
- [var pirAuthenticationToken: String?](./pirauthenticationtoken.md)
  A PIR per-user authentication token string.
- [func refreshPIRParameters() async throws](./refreshpirparameters%28%29.md)
  Refetches PIR parameters from the server.
- [func resetPIRCache() async throws](./resetpircache%28%29.md)
  Resets the PIR on-device cache.
- [var pirPrivacyPassIssuerURL: URL?](./pirprivacypassissuerurl.md)
  A URL that contains the domain name of Privacy Pass issuer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/pirserverurl)*