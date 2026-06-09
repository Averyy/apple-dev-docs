# GlobalHTTPProxy

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures a global HTTP proxy.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 6.0+
- macOS 10.9+
- tvOS 9.0+
- visionOS 2.0+

## Declaration

```swift
object GlobalHTTPProxy
```

#### Discussion

Specify `com.apple.proxy.http.global` as the payload type.

There can only be one payload of this type on the device at any time.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS |
| User channel | N/A |
| Allow manual install | iOS, macOS, tvOS, visionOS |
| Requires supervision | iOS, tvOS, visionOS |
| Requires user-approved MDM | N/A |
| Allowed in user enrollment | N/A |
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
            <key>ProxyCaptiveLoginAllowed</key>
            <false/>
            <key>ProxyPassword</key>
            <string>password</string>
            <key>ProxyServer</key>
            <string>10.0.1.42</string>
            <key>ProxyServerPort</key>
            <integer>8080</integer>
            <key>ProxyType</key>
            <string>Manual</string>
            <key>ProxyUsername</key>
            <string>username</string>
            <key>PayloadIdentifier</key>
            <string>com.example.myglobalhttpproxypayload</string>
            <key>PayloadType</key>
            <string>com.apple.proxy.http.global</string>
            <key>PayloadUUID</key>
            <string>dee0892a-7d4c-41be-ac88-d87247dd076c</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>GlobalHTTPProxy</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>ee2f890c-6c9f-49be-9e19-b81c66d5cc0d</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Properties

- `ProxyCaptiveLoginAllowed` (boolean): If `true`, allows the device to bypass the proxy server to display the login page for captive networks. Available: iOS 7+ | iPadOS 7+ | macOS 10.9+ | tvOS 9+ | visionOS 2+
- `ProxyPACFallbackAllowed` (boolean): If `true`, allows connecting directly to the destination if the proxy autoconfiguration (PAC) file is unreachable. Available: iOS 7+ | iPadOS 7+ | macOS 10.9+ | tvOS 9+ | visionOS 2+
- `ProxyPACURL` (string): The URL of the PAC file that defines the proxy configuration. Starting in iOS 13 and macOS 10.15, only URLs that begin with `http://` or `https://` are allowed. This is only used if `ProxyType` is set to `Automatic`, and is ignored if `ProxyType` is set to `Manual`.
- `ProxyPassword` (string): The password used to authenticate to the proxy server. The device only uses this if `ProxyType` is set to `Manual`, and ignores it if `ProxyType` is set to `Automatic`.
- `ProxyServer` (string): The proxy server’s network address. The device requires this if `ProxyType` is set to `Manual`, and ignores it if `ProxyType` is set to `Automatic`.
- `ProxyServerPort` (integer): The proxy server’s port number. The device requires this if `ProxyType` is set to `Manual`, and ignores this if `ProxyType` is set to `Automatic`.
- `ProxyType` (string): The proxy type. For a manual proxy type, the profile contains the proxy server address, including its port, and optionally a user name and password. For an auto proxy type, you can enter a PAC URL.
- `ProxyUsername` (string): The user name used to authenticate to the proxy server. The device only uses this if `ProxyType` is set to `Manual`, and ignores it if `ProxyType` is set to `Automatic`.

## See Also

- [object DNSProxy](dnsproxy.md)
  The payload that configures DNS proxies.
- [object NetworkProxyConfiguration](networkproxyconfiguration.md)
  The payload that configures network proxies for a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/globalhttpproxy)*