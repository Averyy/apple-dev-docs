# NSExceptionAllowsInsecureHTTPLoads

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value indicating whether to allow insecure HTTP loads.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- macOS 10.11+
- visionOS 1.0+

#### Discussion

Set the value for this key to `YES` to allow insecure HTTP loads for the given domain, or to be able to loosen the server trust evaluation requirements for HTTPS connections to the domain, as described in [`Performing manual server trust authentication`](https://developer.apple.com/documentation/Foundation/performing-manual-server-trust-authentication).

Using this key doesn’t by itself change default server trust evaluation requirements for HTTPS connections, described in `Ensure the Network Server Meets Minimum Requirements`. Using only this key also doesn’t change the TLS or forward secrecy requirements imposed by ATS. As a result, you might need to combine this key with the [`NSExceptionMinimumTLSVersion`](information-property-list/nsexceptionminimumtlsversion.md) or [`NSExceptionRequiresForwardSecrecy`](information-property-list/nsexceptionrequiresforwardsecrecy.md) key in certain cases.

This key is optional. The default value is `NO`.

> ❗ **Important**:  You must supply a justification during App Store review if you set the key’s value to YES, as described in `Provide Justification for Exceptions`.

## See Also

- [NSExceptionMinimumTLSVersion](information-property-list/nsexceptionminimumtlsversion.md)
  The minimum Transport Layer Security (TLS) version for network connections.
- [NSExceptionRequiresForwardSecrecy](information-property-list/nsexceptionrequiresforwardsecrecy.md)
  A Boolean value indicating whether to override the perfect forward secrecy requirement.
- [NSRequiresCertificateTransparency](information-property-list/nsrequirescertificatetransparency.md)
  An obsolete Boolean value indicating whether to require Certificate Transparency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsexceptionallowsinsecurehttploads)*