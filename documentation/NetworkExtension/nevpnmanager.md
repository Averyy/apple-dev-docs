# NEVPNManager

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

An object to create and manage a Personal VPN configuration.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NEVPNManager
```

```objc
@interface NEVPNManager : NSObject
```

#### Overview

The [`NEVPNManager`](./nevpnmanager.md) API gives apps the ability to create and manage a Personal VPN configuration on iOS and macOS. Personal VPN configurations are typically used to provide a service to users that protects their Internet browsing activity on insecure networks such as public Wi-Fi networks.

## Topics

### Managing VPN configurations
- [class func shared() -> NEVPNManager](./nevpnmanager/shared%28%29.md)
  Access the single instance of `NEVPNManager`.
- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](./nevpnmanager/loadfrompreferences%28completionhandler%29.md)
  Load the VPN configuration from the Network Extension preferences.
- [func saveToPreferences(completionHandler: (((any Error)?) -> Void)?)](./nevpnmanager/savetopreferences%28completionhandler%29.md)
  Save the VPN configuration in the Network Extension preferences.
- [func setAuthorization(AuthorizationRef)](./nevpnmanager/setauthorization%28_%29.md)
- [func removeFromPreferences(completionHandler: (((any Error)?) -> Void)?)](./nevpnmanager/removefrompreferences%28completionhandler%29.md)
  Remove the VPN configuration from the Network Extension preferences.
### Accessing VPN configuration properties
- [var isEnabled: Bool](./nevpnmanager/isenabled.md)
  A Boolean used to toggle the enabled state of the VPN configuration.
- [var protocolConfiguration: NEVPNProtocol?](./nevpnmanager/protocolconfiguration.md)
  An [`NEVPNProtocol`](./nevpnprotocol.md) object containing the configuration settings of the VPN tunneling protocol.
- [var `protocol`: NEVPNProtocol?](./nevpnmanager/protocol.md)
  An `NEVPNProtocol` object containing the configuration settings of the VPN tunneling protocol.
- [var localizedDescription: String?](./nevpnmanager/localizeddescription.md)
  A string containing the display name of the VPN configuration.
- [var isOnDemandEnabled: Bool](./nevpnmanager/isondemandenabled.md)
  A Boolean used to toggle the Connect On Demand capability.
- [var onDemandRules: [NEOnDemandRule]?](./nevpnmanager/ondemandrules.md)
  An ordered list of Connect On Demand rules.
### Connecting and disconnecting VPN
- [var connection: NEVPNConnection](./nevpnmanager/connection.md)
  An [`NEVPNConnection`](./nevpnconnection.md) object that is used to control the VPN tunnel specified by the VPN configuration.
### Errors
- [NEVPNError.Code](./nevpnerror-swift.struct/code.md)
  Codes that indicate the source of an error.
- [let NEVPNErrorDomain: String](./nevpnerrordomain.md)
- [NEVPNError.Code](./nevpnerror-swift.struct/code.md)
  Codes that indicate the source of an error.
### Notifications
- [static let NEVPNConfigurationChange: NSNotification.Name](../Foundation/nsnotification/name-swift.struct/nevpnconfigurationchange.md)
  Posted after the VPN configuration stored in the Network Extension preferences changes.
### Entitlements
- [Personal VPN Entitlement](../BundleResources/entitlements/com.apple.developer.networking.vpn.api.md)
  The API an app can use to create and control a custom system VPN configuration.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [NETransparentProxyManager](./netransparentproxymanager.md)
- [NETunnelProviderManager](./netunnelprovidermanager.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### VPN configuration
- [class NEAppProxyProviderManager](./neappproxyprovidermanager.md)
  An object to create and manage the app proxy provider’s VPN configuration.
- [class NETunnelProviderManager](./netunnelprovidermanager.md)
  An object to create and manage the tunnel provider’s VPN configuration.
- [class NETunnelProviderProtocol](./netunnelproviderprotocol.md)
  Configuration parameters for a VPN tunnel.
- [class NEAppRule](./neapprule.md)
  The identity of an app whose traffic is to be routed through the tunnel.
- [VPN On Demand Rules](./vpn-on-demand-rules.md)
  Set up VPN On Demand.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnmanager)*