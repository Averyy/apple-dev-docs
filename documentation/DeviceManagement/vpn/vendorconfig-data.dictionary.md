# VPN.VendorConfig

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Profile

The vendor-specific configuration dictionary.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```
object VPN.VendorConfig
```

## Properties

- `Group` (string): The group to connect to on the head end. Valid for Cisco AnyConnect and Cisco Legacy AnyConnect. Not available in watchOS.
- `LoginGroupOrDomain` (string): The login group or domain. Valid only for SonicWALL Mobile Connect. Not available in watchOS.
- `Realm` (string): The Kerberos realm name, which needs to be properly capitalized. Valid only for Juniper SSL and Pulse Secure. Not available in watchOS.
- `Role` (string): The role to select when connecting to the server. Valid only for Juniper SSL and Pulse Secure. Not available in watchOS.

## See Also

### Objects
- [object VPN.AlwaysOn](./alwayson-data.dictionary.md)
  The dictionary that contains IPSec settings.
- [object VPN.DNS](./dns-data.dictionary.md)
  The dictionary to configure DNS settings for the VPN.
- [object VPN.IKEv2](./ikev2-data.dictionary.md)
  The dictionary to use for an IKEv2 VPN type.
- [object VPN.IPSec](./ipsec-data.dictionary.md)
  The dictionary to use for an IPSec VPN type.
- [object VPN.IPv4](./ipv4-data.dictionary.md)
  The dictionary that contains IPV4 settings.
- [object VPN.PPP](./ppp-data.dictionary.md)
  The dictionary that contains PPP settings.
- [object VPN.Proxies](./proxies-data.dictionary.md)
  The dictionary that contains the Proxies settings.
- [object VPN.TransparentProxy](./transparentproxy-data.dictionary.md)
  The dictionary to use for a transparent proxy VPN type.
- [object VPN.VPN](./vpn-data.dictionary.md)
  The dictionary that contains VPN, IPSec, and IKEv2 settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/vpn/vendorconfig-data.dictionary)*