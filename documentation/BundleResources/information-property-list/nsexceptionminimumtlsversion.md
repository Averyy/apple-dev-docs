# NSExceptionMinimumTLSVersion

**Framework**: Bundle Resources  
**Kind**: typealias

The minimum Transport Layer Security (TLS) version for network connections.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- macOS 10.11+
- visionOS 1.0+

#### Discussion

This key is optional. The value is a string, with a default value of `TLSv1.2`.

> ❗ **Important**:  You must supply a justification during App Store review if you use this key to set a protocol version lower than 1.2, as described in `Provide Justification for Exceptions`.

## See Also

- [NSExceptionAllowsInsecureHTTPLoads](information-property-list/nsexceptionallowsinsecurehttploads.md)
  A Boolean value indicating whether to allow insecure HTTP loads.
- [NSExceptionRequiresForwardSecrecy](information-property-list/nsexceptionrequiresforwardsecrecy.md)
  A Boolean value indicating whether to override the perfect forward secrecy requirement.
- [NSRequiresCertificateTransparency](information-property-list/nsrequirescertificatetransparency.md)
  An obsolete Boolean value indicating whether to require Certificate Transparency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsexceptionminimumtlsversion)*