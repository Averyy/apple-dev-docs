# NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_AuthenticationObject

**Framework**: Device Management  
**Kind**: dictionary

Settings that control authentication.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_AuthenticationObject
```

## Topics

### Objects
- [object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_Authentication_ExtendedAuthObject](networkvpnalwaysontunnelconfigurationelement_ikev2_authentication_extendedauthobject.md)
  Specifies details about how the VPN routes different types of network traffic.

## Properties

- `CredentialsAssetReference` (string): The identifier of an asset declaration that contains the credentials (password) to authenticate with the VPN server. Required when `Authentication.Method` is set to `SharedSecret`.
- `ExtendedAuth` (NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_Authentication_ExtendedAuthObject): Specifies details about how the VPN routes different types of network traffic.
- `IdentityAssetReference` (string): The identifier of a credential asset declaration that contains the identity that this account requires to authenticate with the VPN server. If the value of `AuthenticationMethod` is `Certificate`, the system sends this certificate out for IKEv2 machine authentication. If extended authentication (EAP) is used, the system sends this certificate out for EAP-TLS authentication. Required when `Authentication.Method` is set to `Certificate`.
- `IdentityCertificateType` (string): The type of key used by the identity set in the `IdentityAssetReference` to use for IKEv2 machine authentication. If this key is included, the system requires a value for `ServerCertificateIssuerCommonName`.
- `Method` (string) *(required)*: The type of authentication method for the VPN. To enable EAP-only authentication, set this to `None` and `ExtendedAuthEnabled` to `true`. If this is `None` and the `ExtendedAuthEnabled` key isn’t set, the authentication configuration defaults to `SharedSecret`.

## See Also

- [object NetworkVPNAlwaysOnSecurityAssociationParametersObject](networkvpnalwaysonsecurityassociationparametersobject.md)
  These parameters apply to Child Security Association unless `ChildSecurityAssociationParameters` is specified.
- [object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_IdleObject](networkvpnalwaysontunnelconfigurationelement_ikev2_idleobject.md)
  Specifies details about how the system handles idle VPN connections.
- [object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_OnDemandObject](networkvpnalwaysontunnelconfigurationelement_ikev2_ondemandobject.md)
  Specifies details about how the system controls on-demand VPN.
- [object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_PostQuantumKeyExchangeObject](networkvpnalwaysontunnelconfigurationelement_ikev2_postquantumkeyexchangeobject.md)
  Post Quantum Key Exchange settings.
- [object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_ProviderObject](networkvpnalwaysontunnelconfigurationelement_ikev2_providerobject.md)
  Specifies details about the provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnalwaysontunnelconfigurationelement_ikev2_authenticationobject)*