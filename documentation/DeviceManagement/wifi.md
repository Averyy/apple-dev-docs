# WiFi

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures Wi-Fi settings.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.2+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object WiFi
```

## Mentions

- [Returning a managed device to service](returning-a-managed-device-to-service.md)

#### Discussion

Specify `com.apple.wifi.managed` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | macOS |
| Allow manual install | iOS, macOS, tvOS, visionOS, watchOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | iOS, macOS, visionOS |
| Allow multiple payloads | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>New item</key>
    <dict>
        <key>PayloadContent</key>
        <array>
            <dict>
                <key>AutoJoin</key>
                <true/>
                <key>CaptiveBypass</key>
                <false/>
                <key>DisableAssociationMACRandomization</key>
                <false/>
                <key>EncryptionType</key>
                <string>WPA</string>
                <key>HIDDEN_NETWORK</key>
                <true/>
                <key>IsHotspot</key>
                <false/>
                <key>Password</key>
                <string>Password123</string>
                <key>PayloadDisplayName</key>
                <string>Wi-Fi</string>
                <key>ProxyType</key>
                <string>None</string>
                <key>SSID_STR</key>
                <string>Example</string>
                <key>PayloadIdentifier</key>
                <string>com.example.mywifipayload</string>
                <key>PayloadType</key>
                <string>com.apple.wifi.managed</string>
                <key>PayloadUUID</key>
                <string>94c487e0-d6f8-41e3-b66d-a89994e6919b</string>
                <key>PayloadVersion</key>
                <integer>1</integer>
            </dict>
        </array>
        <key>PayloadDisplayName</key>
        <string>Wi-Fi</string>
        <key>PayloadIdentifier</key>
        <string>com.example.myprofile</string>
        <key>PayloadType</key>
        <string>Configuration</string>
        <key>PayloadUUID</key>
        <string>71e9b0f7-02f8-4aea-b365-b381d872909a</string>
        <key>PayloadVersion</key>
        <integer>1</integer>
    </dict>
</dict>
</plist>
```

## Topics

### Objects
- [object WiFi.EAPClientConfiguration](wifi/eapclientconfiguration-data.dictionary.md)
  A dictionary that configures an enterprise network.
- [object WiFi.QoSMarkingPolicy](wifi/qosmarkingpolicy-data.dictionary.md)
  A dictionary that defines the quality-of-service settings.

## Properties

- `AllowJoinBeforeFirstUnlock` (boolean): If `true`, the device makes this network available for joining before the device is unlocked for the first time following a reboot, on a device configured for return to service. Any network credentials are placed into Class D storage within the keychain, and information about the network is stored on disk in Class D. There are several restrictions on the use of this flag: - This property is only available in the return to service mode.
- Only one network can be designated as available before first unlock.
- `EAPClientConfiguration` must not be present.
- If `IsHotspot` is present, it must be set to `false`.
- `QoSMarkingPolicy` must not be present.
- If `ProxyType` is present, it must be set to `None`. The device fails to install the profile payload if any of these conditions are not met. Available in visionOS 26 and later.
- `AutoJoin` (boolean): If `true`, the device joins the network automatically. If `false`, the user must tap the network name to join it. Available in iOS 5 and later, macOS 10.7 and later, tvOS 9 and later, visionOS 1 and later, and watchOS 3.2 and later.
- `CaptiveBypass` (boolean): If `true`, the system bypasses Captive Network detection when the device connects to the network. Available in iOS 10 and later, tvOS 9 and later, visionOS 1 and later, and watchOS 3.2 and later.
- `DisableAssociationMACRandomization` (boolean): If `true,` disables MAC address randomization for a Wi-Fi network while associated with that network. This feature also shows a privacy warning in Settings indicating that the network has reduced privacy protections. If `false`, then the system enables MAC address randomization on iOS, watchOS, and visionOS. This value is only locked when MDM installs the profile. If the profile is manually installed, the system sets the value but the user can change it. Available in iOS 14 and later, macOS 15 and later, visionOS 1 and later, and watchOS 7 and later.
- `DisplayedOperatorName` (string): The operator name to display when connected to this network. Used only with Wi-Fi Hotspot 2.0 access points. Available in iOS 7 and later, macOS 10.9 and later, tvOS 9 and later, visionOS 1 and later, and watchOS 3.2 and later.
- `DomainName` (string): The primary domain of the tunnel. Available in iOS 7 and later, macOS 10.9 and later, tvOS 9 and later, visionOS 1 and later, and watchOS 3.2 and later.
- `EAPClientConfiguration` (WiFi.EAPClientConfiguration): The enterprise network configuration.
- `EnableIPv6` (boolean): If `true`, enables IPv6 on this interface.
- `EncryptionType` (string): The encryption type for the network. If set to anything except `None`, the payload may contain the following three keys: `Password`, `PayloadCertificateUUID`, or `EAPClientConfiguration`. As of iOS 16, tvOS 16, watchOS 9, and macOS 13: - `WPA` allows joining WPA or WPA2 networks
- `WPA2` allows joining WPA2 or WPA3 networks
- `WPA3` allows joining WPA3 networks only
- `Any` allows joining WPA, WPA2, WPA3, and WEP networks Prior to iOS 16, tvOS 16, and watchOS 9, specifying `WPA`, `WPA2`, and `WPA3` were equivalent and would allow joining any WPA network. Prior to macOS 13, the encryption type, if specified explicitly, needed to match the encryption type of the network exactly.
- `HESSID` (string): The HESSID used for Wi-Fi Hotspot 2.0 negotiation. Available in iOS 7 and later, macOS 10.7 and later, tvOS 9 and later, visionOS 1 and later, and watchOS 3.2 and later.
- `HIDDEN_NETWORK` (boolean): If `true`, defines this network as hidden.
- `IsHotspot` (boolean): If `true`, the device treats the network as a hotspot. Available in iOS 7 and later, macOS 10.9 and later, tvOS 9 and later, visionOS 1 and later, and watchOS 3.2 and later.
- `MCCAndMNCs` ([string]): An array of Mobile Country Code/Mobile Network Code (MCC/MNC) pairs used for Wi-Fi Hotspot 2.0 negotiation. Each string must contain exactly six digits. Available in iOS 7 and later, tvOS 9 and later, visionOS 1 and later, and watchOS 3.2 and later.
- `NAIRealmNames` ([string]): An array of Network Access Identifier Realm names used for Wi-Fi Hotspot 2.0 negotiation. Available in iOS 7 and later, macOS 10.9 and later, tvOS 9 and later, visionOS 1 and later, and watchOS 3.2 and later.
- `Password` (string): The password for the access point.
- `PayloadCertificateUUID` (string): The UUID of the certificate payload within the same profile to use for the client credential.
- `ProxyPACFallbackAllowed` (boolean): If `true`, allows connecting directly to the destination if the PAC file is unreachable.
- `ProxyPACURL` (string): The URL of the PAC file that defines the proxy configuration.
- `ProxyPassword` (string): The password used to authenticate to the proxy server.
- `ProxyServer` (string): The proxy server’s network address.
- `ProxyServerPort` (integer): The proxy server’s port number.
- `ProxyType` (string): The proxy type, if any, to use. If you choose the manual proxy type, you need the proxy server address, including its port and optionally a user name and password into the proxy server. If you choose the auto proxy type, you can enter a proxy autoconfiguration (PAC) URL.
- `ProxyUsername` (string): The user name used to authenticate to the proxy server.
- `QoSMarkingPolicy` (WiFi.QoSMarkingPolicy): A dictionary that contains the list of apps that the system allows to benefit from L2 and L3 marking. When this dictionary isn’t present, the system allows all apps to use L2 and L3 marking when the Wi-Fi network supports Cisco QoS fast lane. Available in iOS 10 and later, macOS 10.13 and later, tvOS 9 and later, visionOS 1 and later, and watchOS 3.2 and later.
- `RoamingConsortiumOIs` ([string]): An array of Roaming Consortium Organization Identifiers used for Wi-Fi Hotspot 2.0 negotiation. Available in iOS 7 and later, macOS 10.9 and later, tvOS 9 and later, visionOS 1 and later, and watchOS 3.2 and later.
- `ServiceProviderRoamingEnabled` (boolean): If `true`, allows connection to roaming service providers. Available in iOS 7 and later, macOS 10.9 and later, tvOS 9 and later, visionOS 1 and later, and watchOS 3.2 and later.
- `SetupModes` ([string]): An array of strings that contain the type of connection mode to attach. Available in macOS 10.7 and later.
- `SSID_STR` (string): The SSID of the Wi-Fi network to use. In iOS 7.0 and later, the SSID is optional if a value exists for `DomainName` value. Available in iOS 7 and later, macOS 10.7 and later, tvOS 9 and later, visionOS 1 and later, and watchOS 3.2 and later.
- `TLSCertificateRequired` (boolean): If `true`, allows for two-factor authentication for EAP-TTLS, PEAP, or EAP-FAST. If `false`, allows for zero-factor authentication for EAP-TLS.

## See Also

- [object Cellular](cellular.md)
  The payload that configures cellular settings.
- [object CellularPrivateNetwork](cellularprivatenetwork.md)
  The payload that provides device info on private network deployments, including geographical location, preference over Wi-Fi, and network deployment type.
- [object ContentCaching](contentcaching.md)
  The payload that configures the Content Caching service.
- [object DNSSettings](dnssettings.md)
  The payload that configures encrypted DNS settings.
- [object Domains](domains.md)
  The payload that configures the domains under an organization’s management.
- [object Firewall](firewall.md)
  The payload that configures the firewall.
- [object NetworkUsageRules](networkusagerules.md)
  The payload that configures network-usage rules.
- [object Relay](relay.md)
  The payload that configures relay settings.
- [object WiFiManagedSettings](wifimanagedsettings.md)
  The payload that configures managed Wi-Fi settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/wifi)*