# NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_Authentication_ExtendedAuthObject

**Framework**: Device Management  
**Kind**: dictionary

Specifies details about how the VPN routes different types of network traffic.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_Authentication_ExtendedAuthObject
```

## Properties

- `CredentialsAssetReference` (string): The identifier of an asset declaration that contains the credentials (user name and password) to authenticate with the VPN server. Required when `Enabled` is set to `true`. Implies the use of EAP-MSCHAPv2.
- `Enabled` (boolean): If `true`, enables EAP-only authentication.
- `ServerCertificateCommonName` (string): The common name of the server certificate. The system uses this name to validate the certificate sent by the IKE server. If not set, the system uses the remote identifier to validate the certificate.
- `ServerCertificateIssuerCommonName` (string): Common Name of the server certificate issuer. If set, this field causes IKE to send a certificate request based on this certificate issuer to the server. This key is required if the `IdentityCertificateType` key is included and the `ExtendedAuth.Enabled` key is `true`.
- `TLSMaximumVersion` (string): The maximum TLS version to use with EAP-TLS authentication.
- `TLSMinimumVersion` (string): The minimum TLS version to use with EAP-TLS authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnalwaysontunnelconfigurationelement_ikev2_authentication_extendedauthobject)*