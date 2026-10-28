# proxyAutoConfigurationJavaScript

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A string containing the Proxy Auto Configuration (PAC) JavaScript source code.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var proxyAutoConfigurationJavaScript: String? { get set }
```

```objc
@property (copy, nullable) NSString * proxyAutoConfigurationJavaScript;
```

## Discussion

If [`autoProxyConfigurationEnabled`](./autoproxyconfigurationenabled.md) is set to [`true`](../../Swift/true.md) then the system will execute the PAC script to determine what proxies to use (if any) for HTTP and HTTPS connections.

## See Also

### Accessing Automatic Proxy Properties
- [var autoProxyConfigurationEnabled: Bool](./autoproxyconfigurationenabled.md)
  A Boolean indicating if proxy auto-configuration is enabled.
- [var proxyAutoConfigurationURL: URL?](./proxyautoconfigurationurl.md)
  A URL specifying the location from where the Proxy Auto Configuration (PAC) script should be downloaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neproxysettings/proxyautoconfigurationjavascript)*