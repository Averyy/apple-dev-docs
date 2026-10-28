# NSRequiresCertificateTransparency

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

An obsolete Boolean value indicating whether to require Certificate Transparency.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- macOS 10.11+
- visionOS 1.0+

## Details

- **Name**: `NSRequiresCertificateTransparency`
- **Type**: boolean



**Default**: `NO`

## Discussion

Certificate Transparency (CT) is a protocol that ATS can use to identify mistakenly or maliciously issued X.509 certificates. Earlier versions of the system used this key to enable or disable CT for a given domain. Specifically, CT requires a domain’s server certificates to have support from signed CT timestamps from at least two CT logs trusted by Apple. For more information about Certificate Transparency, see [RFC 6962](https://tools.ietf.org/html/rfc6962).

The system now requires this behavior in all cases, making the key irrelevant.

> ⚠️ **Warning**:  Don’t use this key. The current system enforces this behavior, and new certificates can’t meet the requirement on older systems.

## See Also

### Exceptions
- [NSExceptionAllowsInsecureHTTPLoads](./nsexceptionallowsinsecurehttploads.md)
  A Boolean value indicating whether to allow insecure HTTP loads.
- [NSExceptionMinimumTLSVersion](./nsexceptionminimumtlsversion.md)
  The minimum Transport Layer Security (TLS) version for network connections.
- [NSExceptionRequiresForwardSecrecy](./nsexceptionrequiresforwardsecrecy.md)
  A Boolean value indicating whether to override the perfect forward secrecy requirement.
- [NSExceptionRequiresNIAPTLSPackageVersion](./nsexceptionrequiresniaptlspackageversion.md)
  A string that indicates the version to use for the NIAP Functional Package for TLS, applied to an exception domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsrequirescertificatetransparency)*