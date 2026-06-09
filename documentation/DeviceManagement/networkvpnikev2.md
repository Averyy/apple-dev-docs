# NetworkVPNIKEV2

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure a VPN using the IKEv2 sub-type.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNIKEV2
```

#### Discussion

Specify `com.apple.configuration.network.vpn.ikev2` as the declaration type.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, tvOS, visionOS |
| Allowed in device enrollment | iOS, Shared iPad, tvOS, visionOS |
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | iOS, macOS, Shared iPad, tvOS, visionOS |
| Allowed in system scope | iOS, macOS, Shared iPad, tvOS, visionOS |
| Allowed in user scope | macOS |
| Apply | Multiple configurations are applied separately |

##### Configuration Examples

**Shared secret**:

This configuration sets up an IKEv2 VPN using a shared-secret credential asset for authentication.

```json
{
    "Type": "com.apple.configuration.network.vpn.ikev2",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "VisibleName": "Corporate IKEv2 VPN",
        "HostName": "vpn.example.com",
        "LocalIdentifier": "device@example.com",
        "RemoteIdentifier": "vpn.example.com",
        "Authentication": {
            "Method": "SharedSecret",
            "CredentialsAssetReference": "64BF8F5C-8CFD-40AA-9082-A0B594D4E100"
        }
    }
}
```

**Certificate**:

This configuration sets up an IKEv2 VPN using certificate-based machine authentication and EAP-MSCHAPv2 for extended user authentication.

```json
{
    "Type": "com.apple.configuration.network.vpn.ikev2",
    "Identifier": "2A3B4C5D-6E7F-8A9B-0C1D-2E3F4A5B6C7D",
    "ServerToken": "F1E2D3C4-B5A6-7890-ABCD-EF1234567890",
    "Payload": {
        "VisibleName": "Corporate IKEv2 VPN (Certificate)",
        "HostName": "vpn.example.com",
        "LocalIdentifier": "device@example.com",
        "RemoteIdentifier": "vpn.example.com",
        "Authentication": {
            "Method": "Certificate",
            "IdentityAssetReference": "CB3E6C7F-2318-437B-8A9E-D50C69376DE4",
            "IdentityCertificateType": "RSA",
            "ExtendedAuth": {
                "Enabled": true,
                "CredentialsAssetReference": "64BF8F5C-8CFD-40AA-9082-A0B594D4E100",
                "ServerCertificateIssuerCommonName": "Example Corp CA",
                "TLSMinimumVersion": "1.2"
            }
        }
    }
}
```

## Topics

### Objects
- [object NetworkVPNIKEV2AuthenticationObject](networkvpnikev2authenticationobject.md)
  Settings that control authentication.
- [object NetworkVPNIKEV2DNSObject](networkvpnikev2dnsobject.md)
  A dictionary to use for all VPN types.
- [object NetworkVPNIKEV2IdleObject](networkvpnikev2idleobject.md)
  Specifies details about how the system handles idle VPN connections.
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

## Properties

- `Authentication` (NetworkVPNIKEV2AuthenticationObject) *(required)*: Settings that control authentication.
- `ChildSecurityAssociationParameters` (NetworkVPNIKEV2SecurityAssociationParametersObject): The `ChildSecurityAssociationParameters` dictionaries.
- `DisableMOBIKE` (boolean): If `true`, the system disables MOBIKE.
- `DisableRedirect` (boolean): If `true`, the system disables IKEv2 redirect. If not set, the system redirects an IKEv2 connection when it receives a redirect request from the server.
- `DNS` (NetworkVPNIKEV2DNSObject): A dictionary to use for all VPN types.
- `EnableCertificateRevocationCheck` (boolean): If `true`, the system performs a certificate revocation check for IKEv2 connections. This is a best-effort revocation check and server response timeouts won’t cause it to fail.
- `EnableFallback` (boolean): If `true`, the system enables a tunnel over cellular data to carry traffic that’s eligible for Wi-Fi Assist and also requires VPN. Enabling fallback requires that the server support multiple tunnels for a single user. Available: iOS 27+ | iPadOS 27+ | tvOS 27+ | visionOS 27+
- `EnableNATKeepAliveOffload` (boolean): If `true`, enables NAT keepalive offload for Always On VPN IKEv2 connections. The device sends keepalive packets to maintain NAT mappings for IKEv2 connections that have a NAT on the path. It sends keepalive packets at regular intervals when the device is awake. If `NATKeepAliveOffloadEnable` is `true`, the system offloads keepalive packets to hardware while the device is asleep. NAT keepalive offload has an impact on the battery life due to the extra workload during sleep. The default interval for the keepalive offload packets is 20 seconds over Wi-Fi and 110 seconds over Cellular interface. The default NAT keepalive works well on networks with small NAT mapping timeouts but imposes a potential battery impact. If a network has larger NAT mapping timeouts, larger keepalive intervals may be safely used to minimize battery impact. Modify the keepalive interval through the `NATKeepAliveInterval` key.
- `EnablePFS` (boolean): If `true`,  enables Perfect Forward Secrecy (PFS) for IKEv2 Connections.
- `EnforceStrictAlgorithmSelection` (boolean): If set to `true`, the device doesn’t allow DES, 3DES, and Diffie-Hellman groups less than 14. Also the device requires the encryption algorithm specified in `IKESecurityAssociationParameters` to be at least as cryptographically strong as the algorithm specified in `ChildSecurityAssociationParameters`. The device rejects this configuration if these requirements are not met.
- `HostName` (string) *(required)*: The IP address or hostname of the VPN server.
- `Idle` (NetworkVPNIKEV2IdleObject): Specifies details about how the system handles idle VPN connections.
- `IKESecurityAssociationParameters` (NetworkVPNIKEV2SecurityAssociationParametersObject): These parameters apply to Child Security Association unless `ChildSecurityAssociationParameters` is specified.
- `LocalIdentifier` (string) *(required)*: Identifier of the IKEv2 client.
- `MTU` (integer): The Maximum Transmission Unit (MTU) specifies the maximum size in bytes of each packet that the system sends over the IKEv2 VPN interface.
- `NATKeepAliveInterval` (integer): The NAT Keepalive interval for Always On VPN IKEv2 connections. This value controls the interval that the device sends keepalive offload packets. The minimum value is 20 seconds. If no key is specified, the default is 20 seconds over Wi-Fi and 110 seconds over a cellular interface.
- `NetworkRouting` (NetworkVPNIKEV2NetworkRoutingObject): Specifies details about how the VPN routes different types of network traffic. Available: iOS 27+ | iPadOS 27+ | macOS 27+ | visionOS 27+
- `OnDemand` (NetworkVPNIKEV2OnDemandObject): Specifies details about how the system controls on-demand VPN.
- `PostQuantumKeyExchange` (NetworkVPNIKEV2PostQuantumKeyExchangeObject): Post Quantum Key Exchange settings.
- `Provider` (NetworkVPNIKEV2ProviderObject): Specifies details about the provider.
- `Proxies` (NetworkVPNIKEV2ProxiesObject): The dictionary to use to configure `Proxies` for use with `VPN`.
- `RemoteIdentifier` (string) *(required)*: The remote identifier.
- `UseConfigurationAttributeInternalIPSubnet` (boolean): If `true`, negotiations should use IKEv2 Configuration Attribute `INTERNAL_IP4_SUBNET` and `INTERNAL_IP6_SUBNET`.
- `VisibleName` (string) *(required)*: The name of the VPN connection that the system displays on the device.

## See Also

- [object AccountCalDAV](accountcaldav.md)
  The declaration to configure a Calendar account.
- [object AccountCardDAV](accountcarddav.md)
  The declaration to configure a Contacts account.
- [object AccountExchange](accountexchange.md)
  The declaration to configure an Exchange account.
- [object AccountGoogle](accountgoogle.md)
  The declaration to configure a Google account.
- [object AccountLDAP](accountldap.md)
  The declaration to configure a Lightweight Directory Access Protocol (LDAP) account.
- [object AccountMail](accountmail.md)
  The declaration to configure a Mail account.
- [object AccountSubscribedCalendar](accountsubscribedcalendar.md)
  The declaration to configure a subscribed calendar.
- [object AppManaged](appmanaged.md)
  The declaration to configure a managed app.
- [object AppSettings](appsettings.md)
  The declaration to configure app settings.
- [object AudioAccessorySettings](audioaccessorysettings.md)
  The declaration to configure audio accessory settings.
- [object ContentCaching](contentcaching.md)
  The declaration to configure the Content Caching service.
- [object DiskManagementSettings](diskmanagementsettings.md)
  The declaration to configure disk management settings on the device.
- [object ExtensibleSSO](extensiblesso.md)
  The declaration to configure Extensible Single Sign-On.
- [object ExternalIntelligenceSettings](externalintelligencesettings.md)
  The declaration to configure External Intelligence Integrations settings.
- [object IntelligenceSettings](intelligencesettings.md)
  The declaration to configure Apple Intelligence settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnikev2)*