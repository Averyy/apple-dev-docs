# routingMethod

**Framework**: Network Extension  
**Kind**: property

The method by which network traffic is routed to the tunnel.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var routingMethod: NETunnelProviderRoutingMethod { get }
```

#### Discussion

The default is [`NETunnelProviderRoutingMethod.destinationIP`](netunnelproviderroutingmethod/destinationip.md).

## See Also

- [var protocolConfiguration: NEVPNProtocol](netunnelprovider/protocolconfiguration.md)
  The configuration of the current tunneling session.
- [var appRules: [NEAppRule]?](netunnelprovider/apprules.md)
  The app rules dictating which apps use the current tunneling session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netunnelprovider/routingmethod)*