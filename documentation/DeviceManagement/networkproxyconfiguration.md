# NetworkProxyConfiguration

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures network proxies for a device.

**Availability**:
- macOS 10.7+

## Declaration

```swift
object NetworkProxyConfiguration
```

#### Discussion

Specify `com.apple.SystemConfiguration` as the payload type.

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
            <key>Proxies</key>
            <dict>
                <key>Exceptions</key>
                <array>
                    <string>*.local, 169.254/16</string>
                </array>
                <key>HTTPEnable</key>
                <integer>1</integer>
                <key>HTTPProxy</key>
                <string>proxy.example.com</string>
                <key>HTTPPort</key>
                <integer>8080</integer>
                <key>FTPPassive</key>
                <integer>1</integer>
            </dict>
            <key>PayloadIdentifier</key>
            <string>com.example.myproxypayload</string>
            <key>PayloadType</key>
            <string>com.apple.SystemConfiguration</string>
            <key>PayloadUUID</key>
            <string>db29e77a-58ee-404b-8579-935a202cf16c</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Network Proxy Configuration</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>b2b00925-6565-4e56-85ab-e012ee0ce4e9</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object NetworkProxyConfiguration.Proxies](networkproxyconfiguration/proxies-data.dictionary.md)
  The payload for configuring network proxies.

## See Also

- [object DNSProxy](dnsproxy.md)
  The payload that configures DNS proxies.
- [object GlobalHTTPProxy](globalhttpproxy.md)
  The payload that configures a global HTTP proxy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkproxyconfiguration)*