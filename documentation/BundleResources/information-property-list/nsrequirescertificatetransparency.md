# NSRequiresCertificateTransparency

**Framework**: Bundle Resources  
**Kind**: typealias

An obsolete Boolean value indicating whether to require Certificate Transparency.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- macOS 10.11+
- visionOS 1.0+

#### Discussion

Certificate Transparency (CT) is a protocol that ATS can use to identify mistakenly or maliciously issued X.509 certificates. Earlier versions of the system used this key to enable or disable CT for a given domain. Specifically, CT requires a domain’s server certificates to have support from signed CT timestamps from at least two CT logs trusted by Apple. For more information about Certificate Transparency, see [`RFC 6962`](https://developer.apple.comhttps://tools.ietf.org/html/rfc6962).

The system now requires this behavior in all cases, making the key irrelevant.

> ⚠️ **Warning**:  Don’t use this key. The current system enforces this behavior, and new certificates can’t meet the requirement on older systems.

 Don’t use this key. The current system enforces this behavior, and new certificates can’t meet the requirement on older systems.

## See Also

- [NSExceptionAllowsInsecureHTTPLoads](information-property-list/nsexceptionallowsinsecurehttploads.md)
  A Boolean value indicating whether to allow insecure HTTP loads.
- [NSExceptionMinimumTLSVersion](information-property-list/nsexceptionminimumtlsversion.md)
  The minimum Transport Layer Security (TLS) version for network connections.
- [NSExceptionRequiresForwardSecrecy](information-property-list/nsexceptionrequiresforwardsecrecy.md)
  A Boolean value indicating whether to override the perfect forward secrecy requirement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsrequirescertificatetransparency)*