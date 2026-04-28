# VPN.PPP

**Framework**: Device Management  
**Kind**: dictionary

The dictionary that contains PPP settings.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- visionOS 1.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object VPN.PPP
```

## Properties

- `AuthEAPPlugins` ([string]): An array of authentication plugins. For use of RSA SecurID, this array should only have one value: `EAP-RSA`. This key is for use with L2TP and PPTP networks.
- `AuthName` (string): The VPN account user name. This key is for use with L2TP and PPTP networks.
- `AuthPassword` (string): If `TokenCard` is `1`, use this password for authentication. This key is for use with L2TP and PPTP networks.
- `AuthProtocol` ([string]): An array of authentication protocols. For use of RSA SecurID, this array should have one value, `EAP`. This key is for use with L2TP and PPTP networks.
- `CCPEnabled` (integer): If `1`, enables encryption on the connection. This key is for use with PPTP networks.
- `CCPMPPE128Enabled` (integer): If `1` and `CCPEnabled` is also `1`, enables CCPMPPE40 encryption.
- `CCPMPPE40Enabled` (integer): If `1` and `CCPEnabled` is also `1`, enables CCPMPPE128 encryption.
- `CommRemoteAddress` (string): The IP address or host name of VPN server. This key is for use with L2TP and PPTP networks.
- `DisconnectOnIdle` (integer): If `1`, disconnects after an on demand connection idles.
- `DisconnectOnIdleTimer` (integer): The length of time to wait before disconnecting an on demand connection
- `TokenCard` (integer): If `1`, uses a token card such as an RSA SecurID card for connecting. This key is for use with L2TP networks.

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
- [object VPN.Proxies](vpn/proxies-data.dictionary.md)
  The dictionary that contains the Proxies settings.
- [object VPN.TransparentProxy](vpn/transparentproxy-data.dictionary.md)
  The dictionary to use for a transparent proxy VPN type.
- [object VPN.VPN](vpn/vpn-data.dictionary.md)
  The dictionary that contains VPN, IPSec, and IKEv2 settings.
- [object VPN.VendorConfig](vpn/vendorconfig-data.dictionary.md)
  The vendor-specific configuration dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/vpn/ppp-data.dictionary)*