# protocolConfiguration

**Framework**: Network Extension  
**Kind**: property

The configuration of the current tunneling session.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var protocolConfiguration: NEVPNProtocol { get }
```

#### Discussion

The configuration is created by the containing app of the Tunnel Provider using the [`NETunnelProviderManager`](netunnelprovidermanager.md) class, or by the ingestion of a `com.apple.vpn.managed` or a `com.apple.vpn.managed.applayer` configuration profile payload. See the [`NETunnelProviderManager`](netunnelprovidermanager.md) class for more details.

For [`NEPacketTunnelProvider`](nepackettunnelprovider.md) subclasses and [`NEAppProxyProvider`](neappproxyprovider.md) subclasses, this property will be set to a [`NETunnelProviderProtocol`](netunnelproviderprotocol.md) object.

`NETunnelProvider` subclasses can observe this property using KVO to be notified when the configuration changes. For details see [`Key-Value Observing Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

## See Also

- [var routingMethod: NETunnelProviderRoutingMethod](netunnelprovider/routingmethod.md)
  The method by which network traffic is routed to the tunnel.
- [var appRules: [NEAppRule]?](netunnelprovider/apprules.md)
  The app rules dictating which apps use the current tunneling session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netunnelprovider/protocolconfiguration)*