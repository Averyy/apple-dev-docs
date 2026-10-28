# NSExceptionMinimumTLSVersion

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The minimum Transport Layer Security (TLS) version for network connections.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- macOS 10.11+
- visionOS 1.0+

## Details

- **Name**: `NSExceptionMinimumTLSVersion`
- **Type**: string

## Possible Values

- `TLSv1.0`: Require a minimum TLS version of 1.0.
- `TLSv1.1`: Require a minimum TLS version of 1.1.
- `TLSv1.2`: Require a minimum TLS version of 1.2.
- `TLSv1.3`: Require a minimum TLS version of 1.3.



**Default**: `TLSv1.2`

## Discussion

This key is optional. The value is a string, with a default value of `TLSv1.2`.

> ❗ **Important**:  You must supply a justification during App Store review if you use this key to set a protocol version lower than 1.2, as described in `Provide Justification for Exceptions`.

## See Also

### Exceptions
- [NSExceptionAllowsInsecureHTTPLoads](./nsexceptionallowsinsecurehttploads.md)
  A Boolean value indicating whether to allow insecure HTTP loads.
- [NSExceptionRequiresForwardSecrecy](./nsexceptionrequiresforwardsecrecy.md)
  A Boolean value indicating whether to override the perfect forward secrecy requirement.
- [NSRequiresCertificateTransparency](./nsrequirescertificatetransparency.md)
  An obsolete Boolean value indicating whether to require Certificate Transparency.
- [NSExceptionRequiresNIAPTLSPackageVersion](./nsexceptionrequiresniaptlspackageversion.md)
  A string that indicates the version to use for the NIAP Functional Package for TLS, applied to an exception domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsexceptionminimumtlsversion)*