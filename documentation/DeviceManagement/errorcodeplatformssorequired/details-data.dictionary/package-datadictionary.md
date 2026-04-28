# ErrorCodePlatformSSORequired.Details.Package

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that specifies the package that the device uses to install an app with the SSO app extension used for Platform SSO.

**Availability**:
- macOS 26.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ErrorCodePlatformSSORequired.Details.Package
```

## Properties

- `ManifestURL` (string) *(required)*: The URL of the app manifest, which needs to begin with `https:`.
- `PinningCerts` ([data]): An array of DER-encoded certificates to pin the connection when fetching the `ManifestURL`.
- `PinningRevocationCheckRequired` (boolean): If `true`, certificate revocation checks require a positive response when using certificate pinning with `PinningCerts`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/errorcodeplatformssorequired/details-data.dictionary/package-data.dictionary)*