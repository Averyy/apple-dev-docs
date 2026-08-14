# NETunnelProviderRoutingMethod

**Framework**: Network Extension  
**Kind**: enum

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

## Topics

### Routing Methods
- [NETunnelProviderRoutingMethod.destinationIP](netunnelproviderroutingmethod/destinationip.md)
  Route network traffic to the tunnel based on destination IP.
- [NETunnelProviderRoutingMethod.sourceApplication](netunnelproviderroutingmethod/sourceapplication.md)
  Route network traffic to the tunnel based on source application.
- [NETunnelProviderRoutingMethod.networkRule](netunnelproviderroutingmethod/networkrule.md)
  A routing method that routes traffic based on network rule objects specified by the provider.
### Initializers
- [init?(rawValue: Int)](netunnelproviderroutingmethod/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var routingMethod: NETunnelProviderRoutingMethod](netunnelprovidermanager/routingmethod.md)
  The method that the system uses to route network traffic to the tunnel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netunnelproviderroutingmethod)*