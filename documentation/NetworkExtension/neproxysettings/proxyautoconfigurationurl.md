# proxyAutoConfigurationURL

**Framework**: Network Extension  
**Kind**: property

A URL specifying the location from where the Proxy Auto Configuration (PAC) script should be downloaded.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var proxyAutoConfigurationURL: URL? { get set }
```

#### Discussion

If [`autoProxyConfigurationEnabled`](neproxysettings/autoproxyconfigurationenabled.md) is set to [`true`](https://developer.apple.com/documentation/Swift/true) and [`proxyAutoConfigurationJavaScript`](neproxysettings/proxyautoconfigurationjavascript.md) is set to nil then the system will download the PAC script from this location and execute the script to determine what proxies to use (if any) for HTTP and HTTPS connections.

## See Also

- [var autoProxyConfigurationEnabled: Bool](neproxysettings/autoproxyconfigurationenabled.md)
  A Boolean indicating if proxy auto-configuration is enabled.
- [var proxyAutoConfigurationJavaScript: String?](neproxysettings/proxyautoconfigurationjavascript.md)
  A string containing the Proxy Auto Configuration (PAC) JavaScript source code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neproxysettings/proxyautoconfigurationurl)*