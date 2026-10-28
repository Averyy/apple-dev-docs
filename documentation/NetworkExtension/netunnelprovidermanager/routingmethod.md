# routingMethod

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The method that the system uses to route network traffic to the tunnel.

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

```objc
@property (readonly) NETunnelProviderRoutingMethod routingMethod;
```

## Discussion

The default is [`NETunnelProviderRoutingMethod.destinationIP`](../netunnelproviderroutingmethod/destinationip.md).

## See Also

### Getting tunnel configuration properties
- [enum NETunnelProviderRoutingMethod](../netunnelproviderroutingmethod.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netunnelprovidermanager/routingmethod)*