# isEnabled

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A Boolean used to toggle the enabled state of the VPN configuration.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var isEnabled: Bool { get set }
```

```objc
@property (getter=isEnabled) BOOL enabled;
```

## Discussion

A VPN configuration must be enabled before it can be used to bring up a VPN tunnel. Only one Personal VPN configuration can be enabled simultaneously on the system. If another Personal VPN configuration is enabled, then this property will be automatically set to [`false`](../../Swift/false.md) in the Network Extension preferences. Note that you will need to re-load the VPN configuration from the preferences in order to see the change in value. You can register with [`NotificationCenter`](../../Foundation/notificationcenter.md) to observe the [`NEVPNConfigurationChangeNotification`](../nevpnconfigurationchangenotification.md) notification for the [`NEVPNManager`](../nevpnmanager.md) object so that your code can detect when the VPN configuration has been disabled.

## See Also

### Accessing VPN configuration properties
- [var protocolConfiguration: NEVPNProtocol?](./protocolconfiguration.md)
  An [`NEVPNProtocol`](../nevpnprotocol.md) object containing the configuration settings of the VPN tunneling protocol.
- [var `protocol`: NEVPNProtocol?](./protocol.md)
  An `NEVPNProtocol` object containing the configuration settings of the VPN tunneling protocol.
- [var localizedDescription: String?](./localizeddescription.md)
  A string containing the display name of the VPN configuration.
- [var isOnDemandEnabled: Bool](./isondemandenabled.md)
  A Boolean used to toggle the Connect On Demand capability.
- [var onDemandRules: [NEOnDemandRule]?](./ondemandrules.md)
  An ordered list of Connect On Demand rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnmanager/isenabled)*