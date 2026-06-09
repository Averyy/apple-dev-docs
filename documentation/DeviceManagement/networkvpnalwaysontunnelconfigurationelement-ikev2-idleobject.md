# NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_IdleObject

**Framework**: Device Management  
**Kind**: dictionary

Specifies details about how the system handles idle VPN connections.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_IdleObject
```

## Properties

- `DeadPeerDetectionRate` (string): One of the following: - `None`: No keepalive.
- `Low`: Send keepalive every 30 minutes.
- `Medium`: Send keepalive every 10 minutes.
- `High`: Send keepalive every 1 minute.
- `Disconnect` (boolean): If `true`, disconnects after an on-demand connection idles.
- `Timer` (integer): The length of time to wait, in seconds, before disconnecting an on-demand connection.

## See Also

- [object NetworkVPNAlwaysOnSecurityAssociationParametersObject](networkvpnalwaysonsecurityassociationparametersobject.md)
  These parameters apply to Child Security Association unless `ChildSecurityAssociationParameters` is specified.
- [object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_AuthenticationObject](networkvpnalwaysontunnelconfigurationelement_ikev2_authenticationobject.md)
  Settings that control authentication.
- [object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_NetworkRoutingObject](networkvpnalwaysontunnelconfigurationelement_ikev2_networkroutingobject.md)
  Specifies details about how the VPN routes different types of network traffic.
- [object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_OnDemandObject](networkvpnalwaysontunnelconfigurationelement_ikev2_ondemandobject.md)
  Specifies details about how the system controls on-demand VPN.
- [object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_PostQuantumKeyExchangeObject](networkvpnalwaysontunnelconfigurationelement_ikev2_postquantumkeyexchangeobject.md)
  Post Quantum Key Exchange settings.
- [object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_ProviderObject](networkvpnalwaysontunnelconfigurationelement_ikev2_providerobject.md)
  Specifies details about the provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnalwaysontunnelconfigurationelement_ikev2_idleobject)*