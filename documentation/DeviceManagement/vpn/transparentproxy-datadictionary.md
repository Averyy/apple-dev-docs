# VPN.TransparentProxy

**Framework**: Device Management  
**Kind**: dictionary

The dictionary to use for a transparent proxy VPN type.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object VPN.TransparentProxy
```

#### Discussion

This dictionary can also contain all keys in the [`VPN.VPN`](vpn/vpn-data.dictionary.md) dictionary. Available in macOS 14 and later.

##### Profile Example

```None
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadDescription</key>
    <string>Configures transparent proxy settings</string>
    <key>PayloadDisplayName</key>
    <string>Transparent Proxy</string>
    <key>PayloadIdentifier</key>
    <string>com.apple.networking.vpn-transparent-proxy</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>01E7F1C0-2DD0-4E36-82FF-EC6F29BB6C45</string>
    <key>PayloadVersion</key>
    <real>1</real>
    <key>TransparentProxy</key>
    <dict>
        <key>AuthName</key>
        <string>username</string>
        <key>AuthPassword</key>
        <string>password</string>
        <key>AuthenticationMethod</key>
        <string>Password</string>
        <key>ProviderBundleIdentifier</key>
        <string>com.example.apple.provider</string>
        <key>RemoteAddress</key>
        <string>vpn.example.com</string>
        <key>ProviderDesignatedRequirement</key>
        <string>identifier "com.example.app.provider" and anchor apple</string>
        <key>Order</key>
        <string>1</string>
    </dict>
    <key>UserDefinedName</key>
    <string>Transparent Proxy</string>
    <key>VPNSubType</key>
    <string>com.example.app</string>
    <key>VPNType</key>
    <string>TransparentProxy</string>
</dict>
```

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