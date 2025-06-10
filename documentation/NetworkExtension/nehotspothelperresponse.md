# NEHotspotHelperResponse

**Framework**: Network Extension  
**Kind**: class

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

## Topics

### Response properties
- [func setNetwork(NEHotspotNetwork)](nehotspothelperresponse/setnetwork(_:).md)
  Set the network that conveys the confidence level.
- [func setNetworkList([NEHotspotNetwork])](nehotspothelperresponse/setnetworklist(_:).md)
  Set the list of handled networks.
### Response delivery
- [func deliver()](nehotspothelperresponse/deliver.md)
  Deliver the response to the system.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NEHotspotHelperCommand](nehotspothelpercommand.md)
  A command for the hotspot helper to handle.
- [class NEHotspotNetwork](nehotspotnetwork.md)
  Information about a Wi-Fi network associated with a command or a response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspothelperresponse)*