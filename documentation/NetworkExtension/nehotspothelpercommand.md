# NEHotspotHelperCommand

**Framework**: Network Extension  
**Kind**: class

A command for the hotspot helper to handle.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class NEHotspotHelperCommand
```

#### Overview

NEHotspostHelperCommand objects are passed to the the Hotspot Helper app’s command handler block. The Hotspot Helper app processes the command, instantiates an [`NEHotspotHelperResponse`](nehotspothelperresponse.md) object, sets the annotated `network` or `networkList` (`Evaluate` or `FilterScanList` commands only), and then delivers the response to the system.

## Topics

### Command information
- [var commandType: NEHotspotHelperCommandType](nehotspothelpercommand/commandtype.md)
  The type of the command
- [enum NEHotspotHelperCommandType](nehotspothelpercommandtype.md)
- [var network: NEHotspotNetwork?](nehotspothelpercommand/network.md)
  The network associated with the command.
- [var networkList: [NEHotspotNetwork]?](nehotspothelpercommand/networklist.md)
  The list of networks associated with the command.
### Networking on the hotspot network
- [func bind(to: NEHotspotHelperCommand)](../foundation/nsmutableurlrequest/1619006-bind.md)
  Binds a URL request to the network interface associated with the hotspot helper command instance.
- [func createTCPConnection(NWEndpoint) -> NWTCPConnection](nehotspothelpercommand/createtcpconnection(_:).md)
  Create a new TCP connection over the network associated with the command.
- [func createUDPSession(NWEndpoint) -> NWUDPSession](nehotspothelpercommand/createudpsession(_:).md)
  Creates a new UDP session over the network associated with the command.
### Response creation
- [func createResponse(NEHotspotHelperResult) -> NEHotspotHelperResponse](nehotspothelpercommand/createresponse(_:).md)
  Create a response to the command.
- [enum NEHotspotHelperResult](nehotspothelperresult.md)
### Instance Properties
- [var interface: NWInterface](nehotspothelpercommand/interface-46dq.md)

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

- [class NEHotspotHelperResponse](nehotspothelperresponse.md)
  The hotspot helper’s response to a command.
- [class NEHotspotNetwork](nehotspotnetwork.md)
  Information about a Wi-Fi network associated with a command or a response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspothelpercommand)*