# VPN.IKEv2

**Framework**: Device Management  
**Kind**: dictionary

The dictionary to use for an IKEv2 VPN type.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
object VPN.IKEv2
```

## Topics

### Objects
- [object VPN.IKEv2.ChildSecurityAssociationParameters](vpn/ikev2-data.dictionary/childsecurityassociationparameters-data.dictionary.md)
  The dictionary that contains child security association parameters.
- [object VPN.IKEv2.IKESecurityAssociationParameters](vpn/ikev2-data.dictionary/ikesecurityassociationparameters-data.dictionary.md)
  The dictionary that contains security association parameters.

## Properties

- `AllowPostQuantumKeyExchangeFallback` (integer): If set to `0`, the VPN doesn’t establish a connection if the server does not support or doesn’t allow post-quantum key exchanges. Thd device ignores this key if `PostQuantumKeyExchangeMethods` is not present in `IKESecurityAssociationParameters` or `ChildSecurityAssociationParameters`.
- `AuthenticationMethod` (string) *(required)*: The type of authentication method for the VPN. To enable EAP-only authentication, set this to `None` and `ExtendedAuthEnabled` to `1`. If this is `None` and the `ExtendedAuthEnabled` key isn’t set, the authentication configuration defaults to `SharedSecret`.
- `AuthName` (string): The user name to use for authentication.
- `AuthPassword` (string): The password to use for authentication.
- `CertificateType` (string): The type of `PayloadCertificateUUID` to use for IKEv2 machine authentication. If this key is included, the system requires a value for `ServerCertificateIssuerCommonName`.
- `ChildSecurityAssociationParameters` (VPN.IKEv2.ChildSecurityAssociationParameters): The `ChildSecurityAssociationParameters` dictionaries.
- `DeadPeerDetectionRate` (string): One of the following: - `None`: No keepalive.
- `Low`: Send keepalive every 30 minutes.
- `Medium`: Send keepalive every 10 minutes.
- `High`: Send keepalive every 1 minute. Not available in watchOS.
- `DisableMOBIKE` (integer): If `1`, the system disables MOBIKE.
- `DisableRedirect` (integer): If `1`, the system disables IKEv2 redirect. If not set, the system redirects an IKEv2 connection when it receives a redirect request from the server.
- `DisconnectOnIdle` (integer): If `1`, the VPN disconnects automatically after a period defined by `DisconnectOnIdleTimer`.
- `DisconnectOnIdleTimer` (integer): Only used if `DisconnectOnIdle` is `1`. The number of seconds before the VPN disconnects. On watchOS, maximum allowed value is 15 seconds
- `EnableCertificateRevocationCheck` (integer): If `1`, the system performs a certificate revocation check for IKEv2 connections. This is a best-effort revocation check and server response timeouts won’t cause it to fail.
- `EnableFallback` (integer): If `1`, the system enables a tunnel over cellular data to carry traffic that’s eligible for Wi-Fi Assist and also requires VPN. Enabling fallback requires that the server support multiple tunnels for a single user. This field is available in iOS 13 and later, and tvOS 17 and later. Not available in watchOS.
- `EnablePFS` (integer): If `1`,  enables Perfect Forward Secrecy (PFS) for IKEv2 Connections.
- `EnforceRoutes` (integer): If `1`, all the VPN’s non-default routes take precedence over any locally-defined routes. If `IncludeAllNetworks` is `1`, the system ignores `EnforceRoutes`.
- `EnforceStrictAlgorithmSelection` (integer): If set to `1`, the device doesn’t allow DES, 3DES, and Diffie-Hellman groups less than 14. Also the device requires the encryption algorithm specified for the IKE SA to be at least as cryptographically strong as the algorithm specified for the child SA. The device rejects this profile payload if these requirements are not met.
- `ExcludeAPNs` (integer): If `1` and `IncludeAllNetworks` is `1`, the system excludes network traffic for the Apple Push Notification service (APNs) from the tunnel.
- `ExcludeCellularServices` (integer): If `1` and `IncludeAllNetworks` is `1`, the system excludes internet-routable network traffic for cellular services (VoLTE, Wi-Fi Calling, IMS, MMS, Visual Voicemail, etc.) from the tunnel. Note that some cellular carriers route cellular services traffic directly to the carrier network, bypassing the internet. Such cellular services traffic is always excluded from the tunnel.
- `ExcludeDeviceCommunication` (integer): If set to `1` and `IncludeAllNetworks` is set to `1`, the device excludes network traffic used for communicating with devices connected via USB or Wi-Fi from the tunnel.
- `ExcludeLocalNetworks` (integer): If `1` and either `IncludeAllNetworks` or `EnforceRoutes` are `1`, then the system routes local network traffic outside of the VPN. The default for this value is `0` on macOS and `1` on iOS.
- `ExtendedAuthEnabled` (integer): If `1`, enables EAP-only authentication.
- `IKESecurityAssociationParameters` (VPN.IKEv2.IKESecurityAssociationParameters): These parameters apply to Child Security Association unless `ChildSecurityAssociationParameters` is specified.
- `IncludeAllNetworks` (integer): If `1`, then the system routes all network traffic through the VPN, with some controllable exclusions, such as `ExcludeLocalNetworks`, `ExcludeCellularServices`, and `ExcludeAPNs` properties. The system always excludes the following traffic from the tunnel: - Traffic necessary for connecting and maintaining the device’s network connection, such as DHCP.
- Traffic necessary for connecting to captive networks.
- Certain cellular services traffic that’s not routable over the internet and is instead directly routed to the cellular network. See the `ExcludeCellularServices` field for more information.
- Network communication with a companion device such as a watchOS device.
- `LocalIdentifier` (string) *(required)*: Identifier of the IKEv2 client.
- `MTU` (integer): The Maximum Transmission Unit (MTU) specifies the maximum size in bytes of each packet that the system sends over the IKEv2 VPN interface. Available in iOS 14 and later, and macOS 11 and later.
- `NATKeepAliveInterval` (integer): The NAT Keepalive interval for Always On VPN IKEv2 connections. This value controls the interval that the device sends keepalive offload packets. The minimum value is 20 seconds. If no key is specified, the default is 20 seconds over Wi-Fi and 110 seconds over a cellular interface.
- `NATKeepAliveOffloadEnable` (integer): If `1`, enables NAT keepalive offload for Always On VPN IKEv2 connections. The device sends keepalive packets to maintain NAT mappings for IKEv2 connections that have a NAT on the path. It sends keepalive packets at regular intervals when the device is awake. If `NATKeepAliveOffloadEnable` is `1`, the system offloads keepalive packets to hardware while the device is asleep. NAT keepalive offload has an impact on the battery life due to the extra workload during sleep. The default interval for the keepalive offload packets is 20 seconds over Wi-Fi and 110 seconds over Cellular interface. The default NAT keepalive works well on networks with small NAT mapping timeouts but imposes a potential battery impact. If a network has larger NAT mapping timeouts, larger keepalive intervals may be safely used to minimize battery impact. Modify the keepalive interval through the `NATKeepAliveInterval` key.
- `OnDemandEnabled` (integer): If `1`, enables VPN up on demand.
- `OnDemandRules` ([VPN.VPN.OnDemandRulesElement]): A list of rules that determine when and how to use an OnDemand VPN.
- `OnDemandUserOverrideDisabled` (integer): If `1`, the system disables the Connect On Demand toggle in Settings for this configuration.
- `Password` (string): The password to use for the account credentials. Only used if `AuthenticationMethod` is `Password`.
- `PayloadCertificateUUID` (string): The UUID of the certificate payload within the same profile to use as the account credential. If the value of `AuthenticationMethod` is `Certificate`, the system sends this certificate out for IKEv2 machine authentication. If extended authentication (EAP) is used, the system sends this certificate out for EAP-TLS authentication.
- `PPK` (data): The Post-quantum Pre-shared key (PPK) the device uses for this VPN. This key is is used with VPN servers that support RFC 8784. If this key is present `PPKIdentifier` must also be present.
- `PPKIdentifier` (string): The identifier for the Post-quantum Pre-shared key (PPK) the device uses for this VPN. This key is is used with VPN servers that support RFC 8784. If this key is present `PPK` must also be present.
- `PPKMandatory` (integer): If set to `1`, the VPN doesn’t establish a connection if the server doesn’t support RFC 8784 or doesn’t accept the PPK identifier specified in `PPKIdentifier`. The device ignores this key if `PPK` and `PPKIdentifier` are not present.
- `ProviderBundleIdentifier` (string): If the VPNSubType field contains the bundle identifier of an app that contains multiple VPN providers of the same type (app-proxy or packet-tunnel), then the system uses this field to choose which provider to use for this configuration. If the VPN provider is implemented as a System Extension, then this field is required.
- `ProviderDesignatedRequirement` (string): If the VPN provider is implemented as a System Extension, then this field is required. Available in macOS 10.15 and later, tvOS 17 and later, and watchOS 10 and later.
- `ProviderType` (string): If the value of this key is `app-proxy`, the VPN service tunnels traffic at the application layer. If the value of this key is `packet-tunnel`, the VPN service tunnels traffic at the IP layer.
- `RemoteAddress` (string) *(required)*: The IP address or host name of the VPN server.
- `RemoteIdentifier` (string) *(required)*: The remote identifier.
- `ServerCertificateCommonName` (string): The common name of the server certificate. The system uses this name to validate the certificate sent by the IKE server. If not set, the system uses the remote identifier to validate the certificate.
- `ServerCertificateIssuerCommonName` (string): Common Name of the server certificate issuer. If set, this field causes IKE to send a certificate request based on this certificate issuer to the server. This key is required if the `CertificateType` key is included and the `ExtendedAuthEnabled` key is `1`.
- `SharedSecret` (string): If `AuthenticationMethod` is `SharedSecret`, this value is used for IKE authentication.
- `TLSMaximumVersion` (string): The maximum TLS version to use with EAP-TLS authentication.
- `TLSMinimumVersion` (string): The minimum TLS version to use with EAP-TLS authentication.
- `UseConfigurationAttributeInternalIPSubnet` (integer): If `1`, negotiations should use IKEv2 Configuration Attribute `INTERNAL_IP4_SUBNET` and `INTERNAL_IP6_SUBNET`.

## See Also

- [object VPN.AlwaysOn](vpn/alwayson-data.dictionary.md)
  The dictionary that contains IPSec settings.
- [object VPN.DNS](vpn/dns-data.dictionary.md)
  The dictionary to configure DNS settings for the VPN.
- [object VPN.IPSec](vpn/ipsec-data.dictionary.md)
  The dictionary to use for an IPSec VPN type.
- [object VPN.IPv4](vpn/ipv4-data.dictionary.md)
  The dictionary that contains IPV4 settings.
- [object VPN.PPP](vpn/ppp-data.dictionary.md)
  The dictionary that contains PPP settings.
- [object VPN.Proxies](vpn/proxies-data.dictionary.md)
  The dictionary that contains the Proxies settings.
- [object VPN.TransparentProxy](vpn/transparentproxy-data.dictionary.md)
  The dictionary to use for a transparent proxy VPN type.
- [object VPN.VPN](vpn/vpn-data.dictionary.md)
  The dictionary that contains VPN, IPSec, and IKEv2 settings.
- [object VPN.VendorConfig](vpn/vendorconfig-data.dictionary.md)
  The vendor-specific configuration dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/vpn/ikev2-data.dictionary)*