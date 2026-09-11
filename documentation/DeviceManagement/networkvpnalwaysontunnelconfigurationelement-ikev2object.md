# NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2Object

**Framework**: Device Management  
**Kind**: dictionary

The IKEv2 configuration for this tunnel.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- visionOS 27.0+

## Declaration

```swift
object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2Object
```

## Topics

### Objects
- [object NetworkVPNAlwaysOnSecurityAssociationParametersObject](networkvpnalwaysonsecurityassociationparametersobject.md)
  These parameters apply to Child Security Association unless `ChildSecurityAssociationParameters` is specified.
- [object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_AuthenticationObject](networkvpnalwaysontunnelconfigurationelement_ikev2_authenticationobject.md)
  Settings that control authentication.
- [object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_IdleObject](networkvpnalwaysontunnelconfigurationelement_ikev2_idleobject.md)
  Specifies details about how the system handles idle VPN connections.
- [object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_PostQuantumKeyExchangeObject](networkvpnalwaysontunnelconfigurationelement_ikev2_postquantumkeyexchangeobject.md)
  Post Quantum Key Exchange settings.

## Properties

- `Authentication` (NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_AuthenticationObject) *(required)*: Settings that control authentication.
- `ChildSecurityAssociationParameters` (NetworkVPNAlwaysOnSecurityAssociationParametersObject): The `ChildSecurityAssociationParameters` dictionaries.
- `DisableMOBIKE` (boolean): If `true`, the system disables MOBIKE.
- `DisableRedirect` (boolean): If `true`, the system disables IKEv2 redirect. If not set, the system redirects an IKEv2 connection when it receives a redirect request from the server.
- `EnableCertificateRevocationCheck` (boolean): If `true`, the system performs a certificate revocation check for IKEv2 connections. This is a best-effort revocation check and server response timeouts won’t cause it to fail.
- `EnableNATKeepAliveOffload` (boolean): If `true`, enables NAT keepalive offload for Always On VPN IKEv2 connections. The device sends keepalive packets to maintain NAT mappings for IKEv2 connections that have a NAT on the path. It sends keepalive packets at regular intervals when the device is awake. If `NATKeepAliveOffloadEnable` is `true`, the system offloads keepalive packets to hardware while the device is asleep. NAT keepalive offload has an impact on the battery life due to the extra workload during sleep. The default interval for the keepalive offload packets is 20 seconds over Wi-Fi and 110 seconds over Cellular interface. The default NAT keepalive works well on networks with small NAT mapping timeouts but imposes a potential battery impact. If a network has larger NAT mapping timeouts, larger keepalive intervals may be safely used to minimize battery impact. Modify the keepalive interval through the `NATKeepAliveInterval` key.
- `EnablePFS` (boolean): If `true`,  enables Perfect Forward Secrecy (PFS) for IKEv2 Connections.
- `EnforceStrictAlgorithmSelection` (boolean): If set to `true`, the device doesn’t allow DES, 3DES, and Diffie-Hellman groups less than 14. Also the device requires the encryption algorithm specified in `IKESecurityAssociationParameters` to be at least as cryptographically strong as the algorithm specified in `ChildSecurityAssociationParameters`. The device rejects this configuration if these requirements aren’t met.
- `HostName` (string) *(required)*: The IP address or hostname of the VPN server.
- `Idle` (NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_IdleObject): Specifies details about how the system handles idle VPN connections.
- `IKESecurityAssociationParameters` (NetworkVPNAlwaysOnSecurityAssociationParametersObject): These parameters apply to Child Security Association unless `ChildSecurityAssociationParameters` is specified.
- `LocalIdentifier` (string) *(required)*: Identifier of the IKEv2 client.
- `MTU` (integer): The Maximum Transmission Unit (MTU) specifies the maximum size in bytes of each packet that the system sends over the IKEv2 VPN interface.
- `NATKeepAliveInterval` (integer): The NAT Keepalive interval for Always On VPN IKEv2 connections. This value controls the interval that the device sends keepalive offload packets. The minimum value is 20 seconds. If no key is specified, the default is 20 seconds over Wi-Fi and 110 seconds over a cellular interface.
- `PostQuantumKeyExchange` (NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_PostQuantumKeyExchangeObject): Post Quantum Key Exchange settings.
- `RemoteIdentifier` (string) *(required)*: The remote identifier.
- `UseConfigurationAttributeInternalIPSubnet` (boolean): If `true`, negotiations should use IKEv2 Configuration Attribute `INTERNAL_IP4_SUBNET` and `INTERNAL_IP6_SUBNET`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnalwaysontunnelconfigurationelement_ikev2object)*