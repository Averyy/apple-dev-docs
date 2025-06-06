# NETunnelProvider

**Framework**: Network Extension  
**Kind**: class

An abstract base class shared by NEPacketTunnelProvider and NEAppProxyProvider.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NETunnelProvider
```

## Mentions

- [Routing your VPN network traffic](routing-your-vpn-network-traffic.md)

#### Overview

Each [`NETunnelProvider`](netunnelprovider.md) instance corresponds to a single tunneling session, with a single associated configuration.

> ❗ **Important**:  The `com.apple.developer.networking.networkextension` entitlement is required in order to use the [`NETunnelProvider`](netunnelprovider.md) class. Enable this entitlement when creating an App ID in your developer account.

 The `com.apple.developer.networking.networkextension` entitlement is required in order to use the [`NETunnelProvider`](netunnelprovider.md) class. Enable this entitlement when creating an App ID in your developer account.

##### Subclassing Notes

The `NETunnelProvider` class should not be subclassed directly. Instead, you should create subclasses of `NETunnelProvider` subclasses.

###### Methods to Override

- [`handleAppMessage(_:completionHandler:)`](netunnelprovider/handleappmessage(_:completionhandler:).md)

## Topics

### Getting the tunnel configuration
- [var protocolConfiguration: NEVPNProtocol](netunnelprovider/protocolconfiguration.md)
  The configuration of the current tunneling session.
- [var routingMethod: NETunnelProviderRoutingMethod](netunnelprovider/routingmethod.md)
  The method by which network traffic is routed to the tunnel.
- [var appRules: [NEAppRule]?](netunnelprovider/apprules.md)
  The app rules dictating which apps use the current tunneling session.
### Configuring the tunnel interface
- [func setTunnelNetworkSettings(NETunnelNetworkSettings?, completionHandler: (((any Error)?) -> Void)?)](netunnelprovider/settunnelnetworksettings(_:completionhandler:).md)
  Specify the network settings for the current tunneling session.
### Communicating with the containing app
- [func handleAppMessage(Data, completionHandler: ((Data?) -> Void)?)](netunnelprovider/handleappmessage(_:completionhandler:).md)
  Handle messages sent by the tunnel provider extension’s containing app.
### Setting tunnel status
- [var reasserting: Bool](netunnelprovider/reasserting.md)
  Indicate to the system that the tunnel is being re-established.
### Errors
- [NETunnelProviderError.Code](netunnelprovidererror-swift.struct/code.md)
  Error codes that the tunnel provider declares.
- [let NETunnelProviderErrorDomain: String](netunnelprovidererrordomain.md)
  The domain used for Tunnel Provider errors.
- [NETunnelProviderError.Code](netunnelprovidererror-swift.struct/code.md)
  Error codes that the tunnel provider declares.

## Relationships

### Inherits From
- [NEProvider](neprovider.md)
### Inherited By
- [NEAppProxyProvider](neappproxyprovider.md)
- [NEPacketTunnelProvider](nepackettunnelprovider.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NEAppProxyProvider](neappproxyprovider.md)
  The principal class for an app proxy provider app extension.
- [class NEProvider](neprovider.md)
  An abstract base class for all NetworkExtension providers.
- [class NETunnelNetworkSettings](netunnelnetworksettings.md)
  The configuration for a tunnel provider’s virtual interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netunnelprovider)*