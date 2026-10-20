# NIDiscoveryToken

**Framework**: Nearby Interaction  
**Kind**: class  
**Role**: Class

An object that uniquely identifies a peer that participates in an interaction session.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- watchOS 7.3+

## Declaration

```swift
class NIDiscoveryToken
```

```objc
@interface NIDiscoveryToken : NSObject
```

## Mentions

- [Extending advanced direction finding and ranging](./extending-advanced-direction-finding-and-ranging.md)

#### Overview

Use `NIDiscoveryToken` to determine the peer device’s nearby interaction capabilities by examining the [`deviceCapabilities`](./nidiscoverytoken/devicecapabilities.md) that describes the available capabilities on a person’s device.

## Topics

### Understanding device capabilities
- [var deviceCapabilities: any NIDeviceCapability](./nidiscoverytoken/devicecapabilities.md)
  A protocol object that describes the nearby interaction capabilities of a person’s device.
### Initializers
- [init?(coder: NSCoder)](./nidiscoverytoken/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Connecting to a peer device
- [var discoveryToken: NIDiscoveryToken?](./nisession/discoverytoken.md)
  A temporary, random identifier for a device.
- [func run(NIConfiguration)](./nisession/run%28_%29.md)
  Starts a session with a nearby peer.
- [var configuration: NIConfiguration?](./nisession/configuration.md)
  The configuration run by the session.
- [var delegateQueue: dispatch_queue_t?](./nisession/delegatequeue.md)
  The dispatch queue on which the session invokes delegate callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidiscoverytoken)*