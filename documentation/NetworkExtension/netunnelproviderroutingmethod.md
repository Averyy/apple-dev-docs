# NETunnelProviderRoutingMethod

**Framework**: Network Extension  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
enum NETunnelProviderRoutingMethod
```

```c
enum NETunnelProviderRoutingMethod : NSInteger;
```

## Topics

### Routing Methods
- [NETunnelProviderRoutingMethod.destinationIP](./netunnelproviderroutingmethod/destinationip.md)
  Route network traffic to the tunnel based on destination IP.
- [NETunnelProviderRoutingMethod.sourceApplication](./netunnelproviderroutingmethod/sourceapplication.md)
  Route network traffic to the tunnel based on source application.
- [NETunnelProviderRoutingMethod.networkRule](./netunnelproviderroutingmethod/networkrule.md)
  A routing method that routes traffic based on network rule objects specified by the provider.
### Initializers
- [init?(rawValue: Int)](./netunnelproviderroutingmethod/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting tunnel configuration properties
- [var routingMethod: NETunnelProviderRoutingMethod](./netunnelprovidermanager/routingmethod.md)
  The method that the system uses to route network traffic to the tunnel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netunnelproviderroutingmethod)*