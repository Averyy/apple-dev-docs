# VPN.Proxies

**Framework**: Device Management  
**Kind**: dictionary

The dictionary that contains the Proxies settings.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
object VPN.Proxies
```

## Properties

- `HTTPEnable` (integer): If `1`, enables proxy for HTTP traffic.
- `HTTPPort` (integer): The port number of the HTTP proxy. This field is required if `HTTPProxy` is specified.
- `HTTPProxy` (string): The host name of the HTTP proxy.
- `HTTPProxyPassword` (string): The password used for authentication.
- `HTTPProxyUsername` (string): The user name used for authentication.
- `HTTPSEnable` (integer): If `true`, enables proxy for HTTPS traffic.
- `HTTPSPort` (integer): The port number of the HTTPS proxy. This field is required if `HTTPSProxy` is specified.
- `HTTPSProxy` (string): The host name of the HTTPS proxy.
- `ProxyAutoConfigEnable` (integer): If `true`, enables automatic proxy configuration.
- `ProxyAutoConfigURLString` (string): The URL to the location of the proxy auto-configuration file. Used only when `ProxyAutoConfigEnable` is `true`.
- `ProxyAutoDiscoveryEnable` (integer): If `true`, enables proxy auto discovery.
- `SupplementalMatchDomains` ([string]): An array of domains that defines which hosts use proxy settings for hosts.

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
- [object VPN.TransparentProxy](vpn/transparentproxy-data.dictionary.md)
  The dictionary to use for a transparent proxy VPN type.
- [object VPN.VPN](vpn/vpn-data.dictionary.md)
  The dictionary that contains VPN, IPSec, and IKEv2 settings.
- [object VPN.VendorConfig](vpn/vendorconfig-data.dictionary.md)
  The vendor-specific configuration dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/vpn/proxies-data.dictionary)*