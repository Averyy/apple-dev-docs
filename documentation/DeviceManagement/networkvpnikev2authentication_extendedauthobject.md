# NetworkVPNIKEV2Authentication_ExtendedAuthObject

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Object

Specifies details about extended authentication (EAP).

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```
object NetworkVPNIKEV2Authentication_ExtendedAuthObject
```

## Properties

- `CredentialsAssetReference` (string): The identifier of an asset declaration that contains the credentials (user name and password) to authenticate with the VPN server. Required when `Enabled` is set to `true`. Implies the use of EAP-MSCHAPv2.
- `Enabled` (boolean): If `true`, enables EAP-only authentication.

  **Default**: `false`
- `ServerCertificateCommonName` (string): The common name of the server certificate. The system uses this name to validate the certificate sent by the IKE server. If not set, the system uses the remote identifier to validate the certificate.
- `ServerCertificateIssuerCommonName` (string): Common Name of the server certificate issuer. If set, this field causes IKE to send a certificate request based on this certificate issuer to the server. This key is required if the `IdentityCertificateType` key is included and the `ExtendedAuth.Enabled` key is `true`.
- `TLSMaximumVersion` (string): The maximum TLS version to use with EAP-TLS authentication.

  **Default**: `1.2`; **Allowed Values**: `1.0`, `1.1`, `1.2`, `1.3`
- `TLSMinimumVersion` (string): The minimum TLS version to use with EAP-TLS authentication.

  **Default**: `1.0`; **Allowed Values**: `1.0`, `1.1`, `1.2`, `1.3`


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnikev2authentication_extendedauthobject)*