# NEAppProxyProviderManager

**Framework**: Network Extension  
**Kind**: class

An object to create and manage the app proxy provider’s VPN configuration.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
class NEAppProxyProviderManager
```

## Mentions

- [Routing your VPN network traffic](routing-your-vpn-network-traffic.md)

#### Overview

Objects cannot be directly instantiated. Instead, App Proxy configurations are created exclusively from `com.apple.vpn.managed.applayer` payloads in configuration profiles.

App Proxy configurations can only be used with Per-App VPN routing rules. For more details about how to create App Proxy configurations and configure Per-App VPN, see [`NETunnelProviderManager`](netunnelprovidermanager.md).

> ❗ **Important**:  The `com.apple.developer.networking.networkextension` entitlement is required in order to use the [`NEAppProxyProviderManager`](neappproxyprovidermanager.md) class. Enable this entitlement when creating an App ID in your developer account.

 The `com.apple.developer.networking.networkextension` entitlement is required in order to use the [`NEAppProxyProviderManager`](neappproxyprovidermanager.md) class. Enable this entitlement when creating an App ID in your developer account.

## Topics

### Loading the app proxy configuration
- [class func loadAllFromPreferences(completionHandler: ([NEAppProxyProviderManager]?, (any Error)?) -> Void)](neappproxyprovidermanager/loadallfrompreferences(completionhandler:).md)
  Load all of the App Proxy configurations associated with the calling app that have previously been saved to the Network Extension preferences.

## Relationships

### Inherits From
- [NETunnelProviderManager](netunnelprovidermanager.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NETunnelProviderManager](netunnelprovidermanager.md)
  An object to create and manage the tunnel provider’s VPN configuration.
- [class NEVPNManager](nevpnmanager.md)
  An object to create and manage a Personal VPN configuration.
- [class NETunnelProviderProtocol](netunnelproviderprotocol.md)
  Configuration parameters for a VPN tunnel.
- [class NEAppRule](neapprule.md)
  The identity of an app whose traffic is to be routed through the tunnel.
- [VPN On Demand Rules](vpn-on-demand-rules.md)
  Set up VPN On Demand.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxyprovidermanager)*