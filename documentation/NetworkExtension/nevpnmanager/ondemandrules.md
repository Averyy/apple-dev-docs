# onDemandRules

**Framework**: Network Extension  
**Kind**: property

An ordered list of Connect On Demand rules.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var onDemandRules: [NEOnDemandRule]? { get set }
```

#### Discussion

The VPN configuration can optionally be configured to connect automatically based on a variety of criteria specified in [`NEOnDemandRule`](neondemandrule.md) objects. The [`onDemandRules`](nevpnmanager/ondemandrules.md) property contains the current set of Connect On Demand rules for the VPN configuration. Each rule is evaluated in order, and the first rule that matches all criteria on the current network is applied.

## See Also

- [var isEnabled: Bool](nevpnmanager/isenabled.md)
  A Boolean used to toggle the enabled state of the VPN configuration.
- [var protocolConfiguration: NEVPNProtocol?](nevpnmanager/protocolconfiguration.md)
  An [`NEVPNProtocol`](nevpnprotocol.md) object containing the configuration settings of the VPN tunneling protocol.
- [var `protocol`: NEVPNProtocol?](nevpnmanager/protocol.md)
  An `NEVPNProtocol` object containing the configuration settings of the VPN tunneling protocol.
- [var localizedDescription: String?](nevpnmanager/localizeddescription.md)
  A string containing the display name of the VPN configuration.
- [var isOnDemandEnabled: Bool](nevpnmanager/isondemandenabled.md)
  A Boolean used to toggle the Connect On Demand capability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnmanager/ondemandrules)*