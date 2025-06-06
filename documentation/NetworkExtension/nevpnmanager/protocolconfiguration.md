# protocolConfiguration

**Framework**: Network Extension  
**Kind**: property

An [`NEVPNProtocol`](nevpnprotocol.md) object containing the configuration settings of the VPN tunneling protocol.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var protocolConfiguration: NEVPNProtocol? { get set }
```

#### Discussion

For `NEVPNManager` objects, this property can be set to either an [`NEVPNProtocolIPSec`](nevpnprotocolipsec.md) object or an [`NEVPNProtocolIKEv2`](nevpnprotocolikev2.md) object.

## See Also

- [var isEnabled: Bool](nevpnmanager/isenabled.md)
  A Boolean used to toggle the enabled state of the VPN configuration.
- [var `protocol`: NEVPNProtocol?](nevpnmanager/protocol.md)
  An `NEVPNProtocol` object containing the configuration settings of the VPN tunneling protocol.
- [var localizedDescription: String?](nevpnmanager/localizeddescription.md)
  A string containing the display name of the VPN configuration.
- [var isOnDemandEnabled: Bool](nevpnmanager/isondemandenabled.md)
  A Boolean used to toggle the Connect On Demand capability.
- [var onDemandRules: [NEOnDemandRule]?](nevpnmanager/ondemandrules.md)
  An ordered list of Connect On Demand rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnmanager/protocolconfiguration)*