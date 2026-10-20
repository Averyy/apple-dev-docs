# autoProxyConfigurationEnabled

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A Boolean indicating if proxy auto-configuration is enabled.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var autoProxyConfigurationEnabled: Bool { get set }
```

```objc
@property BOOL autoProxyConfigurationEnabled;
```

## See Also

### Accessing Automatic Proxy Properties
- [var proxyAutoConfigurationURL: URL?](./proxyautoconfigurationurl.md)
  A URL specifying the location from where the Proxy Auto Configuration (PAC) script should be downloaded.
- [var proxyAutoConfigurationJavaScript: String?](./proxyautoconfigurationjavascript.md)
  A string containing the Proxy Auto Configuration (PAC) JavaScript source code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neproxysettings/autoproxyconfigurationenabled)*