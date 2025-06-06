# NEProxySettings

**Framework**: Network Extension  
**Kind**: class

`NEProxySettings` contains HTTP proxy settings.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NEProxySettings
```

#### Overview

`NEProxySettings` is used in the context of a VPN configuration to specify the proxy that should be used for network traffic when the VPN is active.

Instances of this class are thread safe.

## Topics

### Accessing Automatic Proxy Properties
- [var autoProxyConfigurationEnabled: Bool](neproxysettings/autoproxyconfigurationenabled.md)
  A Boolean indicating if proxy auto-configuration is enabled.
- [var proxyAutoConfigurationURL: URL?](neproxysettings/proxyautoconfigurationurl.md)
  A URL specifying the location from where the Proxy Auto Configuration (PAC) script should be downloaded.
- [var proxyAutoConfigurationJavaScript: String?](neproxysettings/proxyautoconfigurationjavascript.md)
  A string containing the Proxy Auto Configuration (PAC) JavaScript source code.
### Accessing Manual Proxy Properties
- [var httpEnabled: Bool](neproxysettings/httpenabled.md)
  A Boolean indicating if a static HTTP proxy will be used.
- [var httpServer: NEProxyServer?](neproxysettings/httpserver.md)
  An [`NEProxyServer`](neproxyserver.md) object containing the static HTTP proxy server settings.
- [var httpsEnabled: Bool](neproxysettings/httpsenabled.md)
  A Boolean indicating if a static HTTPS proxy will be used.
- [var httpsServer: NEProxyServer?](neproxysettings/httpsserver.md)
  An [`NEProxyServer`](neproxyserver.md) object containing the static HTTPS proxy server settings.
- [class NEProxyServer](neproxyserver.md)
  `NEProxyServer` contains settings for a proxy server.
### Accessing General Proxy Properties
- [var excludeSimpleHostnames: Bool](neproxysettings/excludesimplehostnames.md)
  A Boolean indicating if HTTP requests using single-label host names should be excluded from using the proxy settings.
- [var exceptionList: [String]?](neproxysettings/exceptionlist.md)
  An array of domain name patterns. If the destination host name of an HTTP connection matches one of these patterns then the proxy settings will not be used for the connection.
- [var matchDomains: [String]?](neproxysettings/matchdomains.md)
  An array of domain strings.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [var tunnelRemoteAddress: String](netunnelnetworksettings/tunnelremoteaddress.md)
  The IP address of the tunnel server.
- [var dnsSettings: NEDNSSettings?](netunnelnetworksettings/dnssettings.md)
  The tunnel DNS settings.
- [class NEDNSSettings](nednssettings.md)
  The DNS resolver settings of a network tunnel or a system-wide configuration.
- [var proxySettings: NEProxySettings?](netunnelnetworksettings/proxysettings.md)
  The tunnel HTTP proxy settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neproxysettings)*