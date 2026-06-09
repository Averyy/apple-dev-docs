# VPN.VPN

**Framework**: Device Management  
**Kind**: dictionary

The dictionary that contains VPN, IPSec, and IKEv2 settings.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
object VPN.VPN
```

## Topics

### Objects
- [object VPN.VPN.OnDemandRulesElement](vpn/vpn-data.dictionary/ondemandruleselement.md)
  An On Demand rule

## Properties

- `AuthenticationMethod` (string): The authentication method to use.
- `AuthName` (string): The VPN account username.
- `AuthPassword` (string): The VPN account password. Only use this if `AuthenticationMethod` is set to `Password`.
- `DisconnectOnIdle` (integer): If `1`, disconnects after an on-demand connection idles.
- `DisconnectOnIdleTimer` (integer): The length of time to wait, in seconds, before disconnecting an on-demand connection. In watchOS, the maximum allowed value is `15`.
- `EnforceRoutes` (integer): If `1`, all the VPN’s non-default routes take precedence over any locally defined routes. If `IncludeAllNetworks` is `1`, the system ignores the value of `EnforceRoutes`. Not available in watchOS. Available: iOS 14.2+ | iPadOS 14.2+ | macOS 11+ | tvOS 17+ | visionOS 1+
- `ExcludeAPNs` (integer): If `1` and `IncludeAllNetworks` is `1`, then the system excludes the network traffic for the Apple Push Notification service (APNs) from the tunnel. Not available in watchOS. Available: iOS 16.4+ | iPadOS 16.4+ | macOS 13.3+ | visionOS 1+
- `ExcludeCellularServices` (integer): If `1` and `IncludeAllNetworks` is `1`, then the system excludes internet-routable network traffic for cellular services (VoLTE, Wi-Fi Calling, IMS, MMS, Visual Voicemail, etc.) from the tunnel. Note that some cellular carriers route cellular services traffic directly to the carrier network, bypassing the internet. Such cellular services traffic is always excluded from the tunnel. Not available in watchOS. Available: iOS 16.4+ | iPadOS 16.4+ | macOS 13.3+ | visionOS 1+
- `ExcludeDeviceCommunication` (integer): If set to `1` and `IncludeAllNetworks` is set to `1`, the device excludes network traffic used for communicating with devices connected via USB or Wi-Fi from the tunnel. Available: iOS 17.4+ | iPadOS 17.4+ | macOS 14.4+ | visionOS 1.1+
- `ExcludeLocalNetworks` (integer): If `1` and `IncludeAllNetworks` is `1`, routes all local network traffic outside the VPN. Not available in watchOS. Available: iOS 14.2+ | iPadOS 14.2+ | macOS 10.15+ | visionOS 1+
- `IncludeAllNetworks` (integer): If `1``, routes all traffic through the VPN, with some exclusions. Several of the exclusions can be controlled with the `ExcludeLocalNetworks`, `ExcludeCellularServices`, `ExcludeAPNs`and`ExcludeDeviceCommunication` properties. The following traffic is always excluded from the tunnel: - Traffic necessary for connecting and maintaining the device’s network connection, such as DHCP.
- Traffic necessary for connecting to captive networks.
- Certain cellular services traffic that is not routable over the internet and is instead directly routed to the cellular network. See the ExcludeCellularServices property for more details.
- Network communication with a companion device such as a watchOS device. Not available in watchOS. Available: iOS 14+ | iPadOS 14+ | macOS 10.15+ | visionOS 1+
- `OnDemandEnabled` (integer): If `1`, enables VPN On Demand.
- `OnDemandMatchDomainsAlways` ([string]): A list of domain names. The system treats associated domain names as though they’re associated with the `OnDemandMatchDomainsOnRetry` key. This behavior can be overridden by `OnDemandRules`. In iOS 7 and later, this key is deprecated (but still supported) in favor of `EvaluateConnection` actions in the `OnDemandRules` dictionaries. Not available in watchOS. Deprecated: iOS 7+ | iPadOS 7+
- `OnDemandMatchDomainsNever` ([string]): A list of domain names. If the host name ends with one of these domain names, the system doesn’t start the VPN automatically. The system uses this value to exclude a subdomain within an included domain. In iOS 7 and later, this key is deprecated (but still supported) in favor of `EvaluateConnection` actions in the `OnDemandRules` dictionaries. Not available in watchOS. Deprecated: iOS 7+ | iPadOS 7+
- `OnDemandMatchDomainsOnRetry` ([string]): A list of domain names. If the host name ends with one of these domain names and a DNS query for that domain name fails, the system starts the VPN automatically. In iOS 7 and later, this key is deprecated (but still supported) in favor of `EvaluateConnection` actions in the `OnDemandRules` dictionaries. Not available in watchOS. Deprecated: iOS 7+ | iPadOS 7+
- `OnDemandRules` ([VPN.VPN.OnDemandRulesElement]): An array of dictionaries defining On Demand Rules.
- `OnDemandUserOverrideDisabled` (integer): If `1`, the Connect On Demand toggle in Settings is disabled for this configuration. Not available in watchOS. Available: iOS 14+ | iPadOS 14+ | tvOS 17+ | visionOS 1+
- `PayloadCertificateUUID` (string): The UUID of the certificate payload within the same profile to use for account credentials.
- `ProviderBundleIdentifier` (string): The bundle identifier for the VPN provider. Not available in watchOS.
- `ProviderDesignatedRequirement` (string): If the VPN provider is implemented as a system extension, this field is required. Not available in watchOS. Available: macOS 10.15+ | tvOS 17+
- `ProviderType` (string): The type of VPN service. If the value is `app-proxy`, the service tunnels traffic at the app level. If the value is `packet-tunnel`, the service tunnels traffic at the IP layer. Not available in watchOS.
- `RemoteAddress` (string) *(required)*: The IP address or hostname of the VPN server.

## See Also

- [object VPN.AlwaysOn](vpn/alwayson-data.dictionary.md)
  The dictionary that contains IPSec settings.
- [object VPN.DNS](vpn/dns-data.dictionary.md)
  The dictionary to configure DNS settings for the VPN.
- [object VPN.IKEv2](vpn/ikev2-data.dictionary.md)
  The dictionary to use for an IKEv2 VPN type.
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
- [object VPN.VendorConfig](vpn/vendorconfig-data.dictionary.md)
  The vendor-specific configuration dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/vpn/vpn-data.dictionary)*