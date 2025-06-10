# 8021XGlobalEthernet

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure the default fallback global Ethernet interface.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 10.13+
- tvOS 17.0+

## Declaration

```swift
object 8021XGlobalEthernet
```

#### Discussion

Specify `com.apple.globalethernet.managed` as the payload type.

This payload’s contents contain these profile-specific keys:

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS |
| User channel | macOS, Shared iPad |
| Allow manual install | iOS, macOS, tvOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | iOS, macOS |
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
            <string>GlobalEthernet</string>
            <key>Password</key>
            <string>password</string>
            <key>ProxyType</key>
            <string>None</string>
            <key>SetupModes</key>
            <array>
                <string>System</string>
            </array>
            <key>PayloadIdentifier</key>
            <string>com.example.myglobalethpayload</string>
            <key>PayloadType</key>
            <string>com.apple.globalethernet.managed</string>
            <key>PayloadUUID</key>
            <string>f3d469f1-d7cc-45c5-ac2d-024195a6454b</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>802.1x Global Ethernet</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>9a0d652e-1ace-450c-9449-7bcc5d1d62c4</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## See Also

- [type 8021XFirstActiveEthernet](8021xfirstactiveethernet.md)
  The payload you use to configure the first wired, active Ethernet interface.
- [type 8021XFirstEthernet](8021xfirstethernet.md)
  The payload you use to configure the first wired Ethernet interface.
- [type 8021XSecondActiveEthernet](8021xsecondactiveethernet.md)
  The payload you use to configure the second wired, active Ethernet interface.
- [type 8021XSecondEthernet](8021xsecondethernet.md)
  The payload you use to configure the second wired Ethernet interface.
- [type 8021XThirdActiveEthernet](8021xthirdactiveethernet.md)
  The payload you use to configure the third wired, active Ethernet interface.
- [type 8021XThirdEthernet](8021xthirdethernet.md)
  The payload you use to configure the third wired Ethernet interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/8021xglobalethernet)*