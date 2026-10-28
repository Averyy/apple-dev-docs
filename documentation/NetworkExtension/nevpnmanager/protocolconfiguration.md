# protocolConfiguration

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

An [`NEVPNProtocol`](../nevpnprotocol.md) object containing the configuration settings of the VPN tunneling protocol.

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

```objc
@property (strong, nullable) NEVPNProtocol * protocolConfiguration;
```

## Discussion

For `NEVPNManager` objects, this property can be set to either an [`NEVPNProtocolIPSec`](../nevpnprotocolipsec.md) object or an [`NEVPNProtocolIKEv2`](../nevpnprotocolikev2.md) object.

## See Also

### Accessing VPN configuration properties
- [var isEnabled: Bool](./isenabled.md)
  A Boolean used to toggle the enabled state of the VPN configuration.
- [var `protocol`: NEVPNProtocol?](./protocol.md)
  An `NEVPNProtocol` object containing the configuration settings of the VPN tunneling protocol.
- [var localizedDescription: String?](./localizeddescription.md)
  A string containing the display name of the VPN configuration.
- [var isOnDemandEnabled: Bool](./isondemandenabled.md)
  A Boolean used to toggle the Connect On Demand capability.
- [var onDemandRules: [NEOnDemandRule]?](./ondemandrules.md)
  An ordered list of Connect On Demand rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnmanager/protocolconfiguration)*