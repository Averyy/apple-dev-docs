# VPN.IPv4

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Profile

The dictionary that contains IPV4 settings.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```
object VPN.IPv4
```

## Properties

- `OverridePrimary` (integer): If `1`, the system sends all network traffic over VPN. Only applies to Cisco IPsec and L2TP VPN types.

  **Default**: `0`; **Allowed Values**: `0`, `1`

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
- [object VPN.PPP](./ppp-data.dictionary.md)
  The dictionary that contains PPP settings.
- [object VPN.Proxies](./proxies-data.dictionary.md)
  The dictionary that contains the Proxies settings.
- [object VPN.TransparentProxy](./transparentproxy-data.dictionary.md)
  The dictionary to use for a transparent proxy VPN type.
- [object VPN.VPN](./vpn-data.dictionary.md)
  The dictionary that contains VPN, IPSec, and IKEv2 settings.
- [object VPN.VendorConfig](./vendorconfig-data.dictionary.md)
  The vendor-specific configuration dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/vpn/ipv4-data.dictionary)*