# 8021XThirdActiveEthernet

**Framework**: Device Management  
**Kind**: typealias

The payload you use to configure the third wired, active Ethernet interface.

**Availability**:
- macOS 10.7+

## Declaration

```swift
WiFi.EAPClientConfiguration 8021XThirdActiveEthernet
```

#### Discussion

Specify `com.apple.thirdactiveethernet.managed` as the payload type.

This payload’s contents contain these profile-specific keys:

Payloads with `active` in their name apply to Ethernet interfaces that are working at the time of profile installation. If there’s no active Ethernet interface working, this payload configures the interface with the highest service-order priority.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | macOS |
| Allow manual install | macOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | macOS |
| Allow multiple payloads | NA |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>AuthenticationMethod</key>
            <string></string>
            <key>AutoJoin</key>
            <true/>
            <key>CaptiveBypass</key>
            <false/>
            <key>EAPClientConfiguration</key>
            <dict>
                <key>AcceptEAPTypes</key>
                <array>
                    <integer>25</integer>
                </array>
                <key>UserName</key>
                <string>user</string>
                <key>UserPassword</key>
                <string>password</string>
            </dict>
            <key>EncryptionType</key>
            <string>WPA2</string>
            <key>HIDDEN_NETWORK</key>
            <false/>
            <key>Interface</key>
            <string>ThirdActiveEthernet</string>
            <key>Password</key>
            <string>password</string>
            <key>ProxyType</key>
            <string>None</string>
            <key>SetupModes</key>
            <array>
                <string>System</string>
            </array>
            <key>PayloadIdentifier</key>
            <string>com.example.my8021xthirdaepayload</string>
            <key>PayloadType</key>
            <string>com.apple.thirdactiveethernet.managed</string>
            <key>PayloadUUID</key>
            <string>a001a09a-d40d-4535-83ea-b21c409a5949</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>802.1x Third Active Ethernet</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>77d92cd3-d303-4e2e-8c67-b6e67b30ba2c</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>

```

## See Also

- [object 8021XGlobalEthernet](8021xglobalethernet.md)
  The payload you use to configure the default fallback global Ethernet interface.
- [type 8021XFirstActiveEthernet](8021xfirstactiveethernet.md)
  The payload you use to configure the first wired, active Ethernet interface.
- [type 8021XFirstEthernet](8021xfirstethernet.md)
  The payload you use to configure the first wired Ethernet interface.
- [type 8021XSecondActiveEthernet](8021xsecondactiveethernet.md)
  The payload you use to configure the second wired, active Ethernet interface.
- [type 8021XSecondEthernet](8021xsecondethernet.md)
  The payload you use to configure the second wired Ethernet interface.
- [type 8021XThirdEthernet](8021xthirdethernet.md)
  The payload you use to configure the third wired Ethernet interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/8021xthirdactiveethernet)*