# NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_OnDemandObject

**Framework**: Device Management  
**Kind**: dictionary

Specifies details about how the system controls on-demand VPN.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_OnDemandObject
```

## Topics

### Objects
- [object NetworkVPNAlwaysOnRulesElementObject](networkvpnalwaysonruleselementobject.md)
  An array of dictionaries defining On Demand Rules.

## Properties

- `DisableUserOverride` (boolean): If `true`, the Connect On Demand toggle in Settings is disabled for this configuration.
- `Enabled` (boolean): If `true`, enables VPN On Demand.
- `Rules` ([NetworkVPNAlwaysOnRulesElementObject]): An array of dictionaries defining On Demand Rules.

## See Also

- [object NetworkVPNAlwaysOnSecurityAssociationParametersObject](networkvpnalwaysonsecurityassociationparametersobject.md)
  These parameters apply to Child Security Association unless `ChildSecurityAssociationParameters` is specified.
- [object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_AuthenticationObject](networkvpnalwaysontunnelconfigurationelement_ikev2_authenticationobject.md)
  Settings that control authentication.
- [object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_IdleObject](networkvpnalwaysontunnelconfigurationelement_ikev2_idleobject.md)
  Specifies details about how the system handles idle VPN connections.
- [object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_PostQuantumKeyExchangeObject](networkvpnalwaysontunnelconfigurationelement_ikev2_postquantumkeyexchangeobject.md)
  Post Quantum Key Exchange settings.
- [object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_ProviderObject](networkvpnalwaysontunnelconfigurationelement_ikev2_providerobject.md)
  Specifies details about the provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnalwaysontunnelconfigurationelement_ikev2_ondemandobject)*