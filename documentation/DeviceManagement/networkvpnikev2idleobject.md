# NetworkVPNIKEV2IdleObject

**Framework**: Device Management  
**Kind**: dictionary

Specifies details about how the system handles idle VPN connections.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNIKEV2IdleObject
```

## Properties

- `DeadPeerDetectionRate` (string): One of the following: - `None`: No keepalive.
- `Low`: Send keepalive every 30 minutes.
- `Medium`: Send keepalive every 10 minutes.
- `High`: Send keepalive every 1 minute.
- `Disconnect` (boolean): If `true`, disconnects after an on-demand connection idles.
- `Timer` (integer): The length of time to wait, in seconds, before disconnecting an on-demand connection.

## See Also

- [object NetworkVPNIKEV2AuthenticationObject](networkvpnikev2authenticationobject.md)
  Settings that control authentication.
- [object NetworkVPNIKEV2DNSObject](networkvpnikev2dnsobject.md)
  A dictionary to use for all VPN types.
- [object NetworkVPNIKEV2NetworkRoutingObject](networkvpnikev2networkroutingobject.md)
  Specifies details about how the VPN routes different types of network traffic.
- [object NetworkVPNIKEV2OnDemandObject](networkvpnikev2ondemandobject.md)
  Specifies details about how the system controls on-demand VPN.
- [object NetworkVPNIKEV2PostQuantumKeyExchangeObject](networkvpnikev2postquantumkeyexchangeobject.md)
  Post Quantum Key Exchange settings.
- [object NetworkVPNIKEV2ProviderObject](networkvpnikev2providerobject.md)
  Specifies details about the provider.
- [object NetworkVPNIKEV2ProxiesObject](networkvpnikev2proxiesobject.md)
  The dictionary to use to configure `Proxies` for use with `VPN`.
- [object NetworkVPNIKEV2SecurityAssociationParametersObject](networkvpnikev2securityassociationparametersobject.md)
  These parameters apply to Child Security Association unless `ChildSecurityAssociationParameters` is specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnikev2idleobject)*