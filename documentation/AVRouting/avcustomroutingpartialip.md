# AVCustomRoutingPartialIP

**Framework**: AVRouting  
**Kind**: class  
**Role**: Class

An object that represents a full or partial IP address.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- visionOS 1.0+

## Declaration

```swift
class AVCustomRoutingPartialIP
```

```objc
@interface AVCustomRoutingPartialIP : NSObject
```

#### Overview

Use this type to define the IP address and subnet mask of known routes on a local network. Create an instance of this class and add it to a custom routing controller’s [`knownRouteIPs`](./avcustomroutingcontroller/knownrouteips.md) array like shown below:

```swift
// Define the IP address.
let anIPAddressInBytes:[UInt8] = [192, 168, 10, 5]
let address = Data(bytes: anIPAddressInBytes, count: anIPAddressInBytes.count)

// Define the subnet mask.
let aMaskInBytes:[UInt8] = [255, 255, 255, 255]
let mask = Data(bytes: aMaskInBytes, count: aMaskInBytes.count)

// Create a new object to represent the address and mask.
let partialIP = AVCustomRoutingPartialIP(address: address, mask: mask)

// Add the instance to the custom routing controller's known routes.
routingController.knownRouteIPs.append(partialIP)
```

## Topics

### Creating an IP fragment
- [init(address: Data, mask: Data)](./avcustomroutingpartialip/init%28address,mask%29.md)
  Creates an IP fragment.
### Inspecting the IP fragment
- [var address: Data](./avcustomroutingpartialip/address.md)
  A full or partial IP address for a device known to be on the network.
- [var mask: Data](./avcustomroutingpartialip/mask.md)
  A mask that represents how many octets of the IP address to respect.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring route addresses
- [var knownRouteIPs: [AVCustomRoutingPartialIP]](./avcustomroutingcontroller/knownrouteips.md)
  An array of route addresses known to be on the local network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avrouting/avcustomroutingpartialip)*