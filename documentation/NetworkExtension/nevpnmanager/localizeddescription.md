# localizedDescription

**Framework**: Network Extension  
**Kind**: property

A string containing the display name of the VPN configuration.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var localizedDescription: String? { get set }
```

#### Discussion

This string is used as the display name of the VPN configuration in the system’s VPN settings UI. If this property is set to nil at the time that the configuration is created, it will be automatically set to the display name of the calling app.

## See Also

- [var isEnabled: Bool](nevpnmanager/isenabled.md)
  A Boolean used to toggle the enabled state of the VPN configuration.
- [var protocolConfiguration: NEVPNProtocol?](nevpnmanager/protocolconfiguration.md)
  An [`NEVPNProtocol`](nevpnprotocol.md) object containing the configuration settings of the VPN tunneling protocol.
- [var `protocol`: NEVPNProtocol?](nevpnmanager/protocol.md)
  An `NEVPNProtocol` object containing the configuration settings of the VPN tunneling protocol.
- [var isOnDemandEnabled: Bool](nevpnmanager/isondemandenabled.md)
  A Boolean used to toggle the Connect On Demand capability.
- [var onDemandRules: [NEOnDemandRule]?](nevpnmanager/ondemandrules.md)
  An ordered list of Connect On Demand rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnmanager/localizeddescription)*