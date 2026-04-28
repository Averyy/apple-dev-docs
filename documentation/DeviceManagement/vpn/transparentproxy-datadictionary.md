# VPN.TransparentProxy

**Framework**: Device Management  
**Kind**: dictionary

The dictionary to use for a transparent proxy VPN type.

**Availability**:
- macOS 14.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object VPN.TransparentProxy
```

## Properties

- `AuthenticationMethod` (string): The type of authentication method to use: `Password`, `Certificate`, or `Password+Certificate`. Available in macOS 14 and later.
- `DisconnectOnIdle` (integer): If `1`, the VPN disconnects automatically disconnect after a period defined by `DisconnectOnIdleTimer`. Available in macOS 14 and later.
- `DisconnectOnIdleTimer` (integer): The number of seconds before the VPN disconnects. This value is only used if `DisconnectOnIdle` is `1`. Available in macOS 14 and later.
- `EnforceRoutes` (integer): If `1`, then all the VPN’s non-default routes take precedence over any locally-defined routes. If `IncludeAllNetworks` is `1`, the system ignores the value of `EnforceRoutes`. Available in macOS 14 and later.
- `OnDemandEnabled` (integer): If `1`, the system brings up the VPN on demand. Available in macOS 14 and later.
- `OnDemandRules` ([VPN.VPN.OnDemandRulesElement]): Determines when and how the system uses an OnDemand VPN. Available in macOS 14 and later.
- `Order` (integer): A positive integer. Available in macOS 14 and later.
- `Password` (string): The password to use for the account credentials. Only used if `AuthenticationMethod` is `Password`. Available in macOS 14 and later.
- `PayloadCertificateUUID` (string): The UUID of the identity certificate as the account credential. If `AuthenticationMethod` is `Certificate`, and extended authentication (EAP) isn’t used, this certificate is sent out for IKE client authentication. If extended authentication is used, this certificate can be used for EAP-TLS. Available in macOS 14 and later.
- `ProviderBundleIdentifier` (string): If the VPNSubType field contains the bundle identifier of an app that contains multiple VPN providers of the same type (app-proxy or packet-tunnel), then the system uses this field to choose which provider to use for this configuration. If the VPN provider is implemented as a System Extension, then this field is required. Available in macOS 14 and later.
- `ProviderDesignatedRequirement` (string): If the VPN provider is implemented as a System Extension, then this field is required. Available in macOS 14 and later.
- `ProviderType` (string): If the value of this key is `app-proxy`, the VPN service tunnels traffic at the application layer. If the value of this key is `packet-tunnel`, the VPN service tunnels traffic at the IP layer. Available in macOS 14 and later.

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
- [object VPN.VPN](vpn/vpn-data.dictionary.md)
  The dictionary that contains VPN, IPSec, and IKEv2 settings.
- [object VPN.VendorConfig](vpn/vendorconfig-data.dictionary.md)
  The vendor-specific configuration dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/vpn/transparentproxy-data.dictionary)*