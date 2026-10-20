# tunnelRemoteAddress

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The IP address of the tunnel server.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var tunnelRemoteAddress: String { get }
```

```objc
@property (readonly) NSString * tunnelRemoteAddress;
```

## See Also

### Accessing tunnel network settings
- [var dnsSettings: NEDNSSettings?](./dnssettings.md)
  The tunnel DNS settings.
- [class NEDNSSettings](../nednssettings.md)
  The DNS resolver settings of a network tunnel or a system-wide configuration.
- [var proxySettings: NEProxySettings?](./proxysettings.md)
  The tunnel HTTP proxy settings.
- [class NEProxySettings](../neproxysettings.md)
  `NEProxySettings` contains HTTP proxy settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netunnelnetworksettings/tunnelremoteaddress)*