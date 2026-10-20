# knownRouteIPs

**Framework**: AVRouting  
**Kind**: property  
**Role**: Instance Property

An array of route addresses known to be on the local network.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- visionOS 1.0+

## Declaration

```swift
var knownRouteIPs: [AVCustomRoutingPartialIP] { get set }
```

```objc
@property (nonatomic, strong) NSArray<AVCustomRoutingPartialIP *> * knownRouteIPs;
```

## See Also

### Configuring route addresses
- [class AVCustomRoutingPartialIP](../avcustomroutingpartialip.md)
  An object that represents a full or partial IP address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avrouting/avcustomroutingcontroller/knownrouteips)*