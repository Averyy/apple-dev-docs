# NEHotspotHelperResponse

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

The hotspot helper’s response to a command.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class NEHotspotHelperResponse
```

```objc
@interface NEHotspotHelperResponse : NSObject
```

## Topics

### Response properties
- [func setNetwork(NEHotspotNetwork)](./nehotspothelperresponse/setnetwork%28_%29.md)
  Set the network that conveys the confidence level.
- [func setNetworkList([NEHotspotNetwork])](./nehotspothelperresponse/setnetworklist%28_%29.md)
  Set the list of handled networks.
### Response delivery
- [func deliver()](./nehotspothelperresponse/deliver%28%29.md)
  Deliver the response to the system.

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

## See Also

### Commands
- [class NEHotspotHelperCommand](./nehotspothelpercommand.md)
  A command for the hotspot helper to handle.
- [class NEHotspotNetwork](./nehotspotnetwork.md)
  Information about a Wi-Fi network associated with a command or a response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspothelperresponse)*