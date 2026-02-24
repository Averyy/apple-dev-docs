# VPN

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures a VPN.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
object VPN
```

#### Discussion

Specify `com.apple.vpn.managed` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS |
| User channel | macOS |
| Allow manual install | iOS, macOS, tvOS, visionOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | NA |
| Allow multiple payloads | iOS, macOS, Shared iPad, tvOS, visionOS |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>IPSec</key>
            <dict>
                <key>AuthenticationMethod</key>
                <string>SharedSecret</string>
                <key>LocalIdentifierType</key>
                <string>KeyID</string>
                <key>SharedSecret</key>
                <data>
                UVhCd2JHVXhNak1o
                </data>
            </dict>
            <key>IPv4</key>
            <dict>
                <key>OverridePrimary</key>
                <integer>0</integer>
            </dict>
            <key>PPP</key>
            <dict>
                <key>AuthName</key>
                <string>username</string>
                <key>AuthPassword</key>
                <string>password</string>
                <key>CommRemoteAddress</key>
                <string>vpn.example.com</string>
            </dict>
            <key>Proxies</key>
            <dict>
                <key>HTTPEnable</key>
                <integer>0</integer>
                <key>HTTPSEnable</key>
                <integer>0</integer>
            </dict>
            <key>UserDefinedName</key>
            <string>VPN Server</string>
            <key>VPNType</key>
            <string>L2TP</string>
            <key>PayloadIdentifier</key>
            <string>com.example.myvpnmanagedprofile</string>
            <key>PayloadType</key>
            <string>com.apple.vpn.managed</string>
            <key>PayloadUUID</key>
            <string>74615F25-3B51-4386-A31B-ACB1F1094EF9</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>VPN</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>01E7F1C0-2DD0-4E36-82FF-EC6F29BB6C45</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
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
- [object VPN.VPN](vpn/vpn-data.dictionary.md)
  The dictionary that contains VPN, IPSec, and IKEv2 settings.
- [object VPN.VendorConfig](vpn/vendorconfig-data.dictionary.md)
  The vendor-specific configuration dictionary.

## Properties

- `AlwaysOn` (VPN.AlwaysOn): The dictionary to use when `VPNType` is `AlwaysOn`. Not available in tvOS or watchOS.
- `DNS` (VPN.DNS): A dictionary to use for all VPN types.
- `IKEv2` (VPN.IKEv2): The dictionary to use when `VPNType` is `IKEv2`.
- `IPSec` (VPN.IPSec): The dictionary that contains IPSec settings. Not available in watchOS.
- `IPv4` (VPN.IPv4): The dictionary that contains IPv4 settings. Not available in watchOS.
- `PPP` (VPN.PPP): The dictionary to use when `VPNType` is `L2TP` or `PTPP`. Not available in watchOS.
- `Proxies` (VPN.Proxies): The dictionary to use to configure `Proxies` for use with `VPN`.
- `TransparentProxy` (VPN.TransparentProxy): The dictionary to use when `VPNType` is `TransparentProxy`. Available in macOS 14 and later.
- `UserDefinedName` (string) *(required)*: The description of the VPN connection that the system displays on the device. Not available in watchOS.
- `VendorConfig` (VPN.VendorConfig): The vendor-specific configuration dictionary, which the system reads only when `VPNSubType` has a value. Not available in watchOS.
- `VPN` (VPN.VPN): The dictionary to use when `VPNType` is `VPN`.
- `VPNSubType` (string): An identifier for a vendor-specified configuration dictionary when the value for `VPNType` is `VPN`. If `VPNType` is `VPN`, the system requires this field. If the configuration targets a VPN solution that uses a VPN plugin, then this field contains the bundle identifier of the plugin. Here are some examples: - Cisco AnyConnect: `com.cisco.anyconnect.applevpn.plugin`
- Juniper SSL: `net.juniper.sslvpn`
- F5 SSL: `com.f5.F5-Edge-Client.vpnplugin`
- SonicWALL Mobile Connect: `com.sonicwall.SonicWALL-SSLVPN.vpnplugin`
- ``Aruba VIA: `com.arubanetworks.aruba-via.vpnplugin` If the configuration targets a VPN solution that uses a network extension provider, then this field contains the bundle identifier of the app that contains the provider. Contact the VPN solution vendor for the value of the identifier. If `VPNType` is `IKEv2`, then the `VPNSubType` field is optional and reserved for future use. If it’s specified, it needs to contain an empty string. Not available in watchOS.
- `VPNType` (string) *(required)*: The type of the VPN, which defines which settings are appropriate for this VPN payload. If the type is `VPN` or `TransparentProxy`, then the system requires a value for `VPNSubType`. `TransparentProxy` is only available in macOS. `L2TP` and `IPSec` aren’t available in tvOS. `AlwaysOn` is only available on iOS and Apple Watch pairing isn’t supported with `AlwaysOn`. For a previously paired Apple Watch, all phone-watch communications cease when `AlwaysOn` is enabled. Not available in watchOS.

## See Also

- [object AppLayerVPN](applayervpn.md)
  The payload that configures a per-app VPN.
- [object AppToAppLayerVPNMapping](apptoapplayervpnmapping.md)
  The payload that configures per-app VPN settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/vpn)*