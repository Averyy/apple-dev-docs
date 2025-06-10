# Xsan

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure an Xsan client system.

**Availability**:
- macOS 10.10+

## Declaration

```swift
object Xsan
```

#### Discussion

Specify `com.apple.xsan` as the payload type.

For more information, see [`https://support.apple.com/en-us/HT205333`](https://developer.apple.comhttps://support.apple.com/en-us/HT205333).

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | NA |
| Allow manual install | macOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | NA |
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
            <key>fsnameservers</key>
            <array>
                <string>san.example.com</string>
            </array>
            <key>sanAuthMethod</key>
            <string>auth_secret</string>
            <key>sanName</key>
            <string>user_xsan</string>
            <key>sharedSecret</key>
            <string>shared_secret</string>
            <key>PayloadIdentifier</key>
            <string>com.example.myxsanpayload</string>
            <key>PayloadType</key>
            <string>com.apple.xsan</string>
            <key>PayloadUUID</key>
            <string>015b6f29-6a6a-4e23-9305-a4182838516d</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Xsan</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>e93b1eca-d07c-4383-8b4f-ca9db76f4aa8</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## See Also

- [object XsanPreferences](xsanpreferences.md)
  The payload you use to configure the Xsan preferences that define the volumes that automatically mount at startup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/xsan)*