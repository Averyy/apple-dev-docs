# dnsSettings

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The tunnel DNS settings.

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
var dnsSettings: NEDNSSettings? { get set }
```

```objc
@property (copy, nullable) NEDNSSettings * DNSSettings;
```

## Discussion

Network connections to hosts in the tunnel’s internal network will use these DNS settings when resolving host names.

## See Also

### Accessing tunnel network settings
- [var tunnelRemoteAddress: String](./tunnelremoteaddress.md)
  The IP address of the tunnel server.
- [class NEDNSSettings](../nednssettings.md)
  The DNS resolver settings of a network tunnel or a system-wide configuration.
- [var proxySettings: NEProxySettings?](./proxysettings.md)
  The tunnel HTTP proxy settings.
- [class NEProxySettings](../neproxysettings.md)
  `NEProxySettings` contains HTTP proxy settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netunnelnetworksettings/dnssettings)*