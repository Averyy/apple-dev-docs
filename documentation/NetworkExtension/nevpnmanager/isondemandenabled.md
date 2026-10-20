# isOnDemandEnabled

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A Boolean used to toggle the Connect On Demand capability.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var isOnDemandEnabled: Bool { get set }
```

```objc
@property (getter=isOnDemandEnabled) BOOL onDemandEnabled;
```

## Mentions

- [Routing your VPN network traffic](../routing-your-vpn-network-traffic.md)

#### Discussion

The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Accessing VPN configuration properties
- [var isEnabled: Bool](./isenabled.md)
  A Boolean used to toggle the enabled state of the VPN configuration.
- [var protocolConfiguration: NEVPNProtocol?](./protocolconfiguration.md)
  An [`NEVPNProtocol`](../nevpnprotocol.md) object containing the configuration settings of the VPN tunneling protocol.
- [var `protocol`: NEVPNProtocol?](./protocol.md)
  An `NEVPNProtocol` object containing the configuration settings of the VPN tunneling protocol.
- [var localizedDescription: String?](./localizeddescription.md)
  A string containing the display name of the VPN configuration.
- [var onDemandRules: [NEOnDemandRule]?](./ondemandrules.md)
  An ordered list of Connect On Demand rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnmanager/isondemandenabled)*