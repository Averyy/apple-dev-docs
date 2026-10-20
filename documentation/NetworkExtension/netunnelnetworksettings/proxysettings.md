# proxySettings

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The tunnel HTTP proxy settings.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var proxySettings: NEProxySettings? { get set }
```

```objc
@property (copy, nullable) NEProxySettings * proxySettings;
```

#### Discussion

HTTP connections to hosts in the tunnel’s internal network will use these proxy settings.

## See Also

### Accessing tunnel network settings
- [var tunnelRemoteAddress: String](./tunnelremoteaddress.md)
  The IP address of the tunnel server.
- [var dnsSettings: NEDNSSettings?](./dnssettings.md)
  The tunnel DNS settings.
- [class NEDNSSettings](../nednssettings.md)
  The DNS resolver settings of a network tunnel or a system-wide configuration.
- [class NEProxySettings](../neproxysettings.md)
  `NEProxySettings` contains HTTP proxy settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netunnelnetworksettings/proxysettings)*