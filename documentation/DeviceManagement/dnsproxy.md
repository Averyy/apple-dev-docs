# DNSProxy

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures DNS proxies.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.15+
- visionOS 1.1+

## Declaration

```swift
object DNSProxy
```

#### Discussion

Specify `com.apple.dnsProxy.managed` as the payload type.

Beginning with iOS 15, this profile is unsupervised and needs to be installed through MDM.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, visionOS |
| User channel | N/A |
| Allow manual install | macOS |
| Requires supervision | N/A |
| Requires user-approved MDM | N/A |
| Allowed in user enrollment | iOS, visionOS |
| Allow multiple payloads | N/A |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>AppBundleIdentifier</key>
            <string>com.example.mydnsproxyapp</string>
            <key>ProviderBundleIdentifier</key>
            <string>com.example.mydnsproxyapp.mydnsproxyprovider</string>
            <key>ProviderConfiguration</key>
            <dict>
                <key>resolver</key>
                <dict>
                    <key>ipaddress</key>
                    <string>9.9.9.9</string>
                </dict>
            </dict>
            <key>PayloadIdentifier</key>
            <string>com.example.mydnsproxypayload</string>
            <key>PayloadType</key>
            <string>com.apple.dnsProxy.managed</string>
            <key>PayloadUUID</key>
            <string>D6B3F3E4-A72E-49F1-AE2E-742A3A11BE1D</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>DNS Proxy</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>6a60bbe0-242c-493d-b338-c5885107f2af</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object DNSProxy.ProviderConfiguration](dnsproxy/providerconfiguration-data.dictionary.md)
  The dictionary of vendor-specific configuration items.

## Properties

- `AppBundleIdentifier` (string) *(required)*: The bundle identifier of the app containing the DNS proxy network extension.
- `DNSProxyUUID` (string): A globally unique identifier for this DNS proxy configuration. The proxy processes DNS lookups traffic for managed apps with the same `DNSProxyUUID` in their app attributes. This key is required for user enrollment. Available: iOS 16+ | iPadOS 16+ | visionOS 1.1+
- `ProviderBundleIdentifier` (string): The bundle identifier of the DNS proxy network extension to use. Declaring the bundle identifier is useful for apps that contain more than one DNS proxy extension.
- `ProviderConfiguration` (DNSProxy.ProviderConfiguration): The dictionary of vendor-specific configuration items.
- `ProviderDesignatedRequirement` (string): The designated requirement string that the system embeds in the code signature of the DNS proxy network extension. Use this to correctly identify the DNS proxy extension when `ProviderBundleIdentifier` is present. Available: macOS 10.15+

## See Also

- [object GlobalHTTPProxy](globalhttpproxy.md)
  The payload that configures a global HTTP proxy.
- [object NetworkProxyConfiguration](networkproxyconfiguration.md)
  The payload that configures network proxies for a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/dnsproxy)*