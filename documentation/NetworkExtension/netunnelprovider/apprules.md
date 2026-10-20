# appRules

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The app rules dictating which apps use the current tunneling session.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var appRules: [NEAppRule]? { get }
```

```objc
@property (readonly, nullable) NSArray<NEAppRule *> * appRules;
```

#### Discussion

This property is only non-`nil` if the current configuration is a Per-App VPN configuration.

## See Also

### Getting the tunnel configuration
- [var protocolConfiguration: NEVPNProtocol](./protocolconfiguration.md)
  The configuration of the current tunneling session.
- [var routingMethod: NETunnelProviderRoutingMethod](./routingmethod.md)
  The method by which network traffic is routed to the tunnel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netunnelprovider/apprules)*