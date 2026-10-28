# protocol

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

An `NEVPNProtocol` object containing the configuration settings of the VPN tunneling protocol.

**Availability**:
- iOS 8.0+ - Deprecated in 9.0
- iPadOS 8.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.11+ - Deprecated in 10.11
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
var `protocol`: NEVPNProtocol? { get set }
```

```objc
@property (strong, nullable) NEVPNProtocol * protocol;
```

## Discussion

For `NEVPNManager` objects, this property can be set to either an [`NEVPNProtocolIPSec`](../nevpnprotocolipsec.md) object or an [`NEVPNProtocolIKEv2`](../nevpnprotocolikev2.md) object.

## See Also

### Accessing VPN configuration properties
- [var isEnabled: Bool](./isenabled.md)
  A Boolean used to toggle the enabled state of the VPN configuration.
- [var protocolConfiguration: NEVPNProtocol?](./protocolconfiguration.md)
  An [`NEVPNProtocol`](../nevpnprotocol.md) object containing the configuration settings of the VPN tunneling protocol.
- [var localizedDescription: String?](./localizeddescription.md)
  A string containing the display name of the VPN configuration.
- [var isOnDemandEnabled: Bool](./isondemandenabled.md)
  A Boolean used to toggle the Connect On Demand capability.
- [var onDemandRules: [NEOnDemandRule]?](./ondemandrules.md)
  An ordered list of Connect On Demand rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnmanager/protocol)*