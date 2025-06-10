# NEHotspotHelperCommandType

**Framework**: Network Extension  
**Kind**: enum

An enumeration of hotspot command types.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum NEHotspotHelperCommandType
```

## Topics

### Command Types
- [NEHotspotHelperCommandType.none](nehotspothelpercommandtype/none.md)
  Placeholder for the null command.
- [NEHotspotHelperCommandType.filterScanList](nehotspothelpercommandtype/filterscanlist.md)
  Filter the Wi-Fi scan list.
- [NEHotspotHelperCommandType.evaluate](nehotspothelpercommandtype/evaluate.md)
  Evaluate the network.
- [NEHotspotHelperCommandType.authenticate](nehotspothelpercommandtype/authenticate.md)
  Authenticate to the network.
- [NEHotspotHelperCommandType.presentUI](nehotspothelpercommandtype/presentui.md)
  Present user interface.
- [NEHotspotHelperCommandType.maintain](nehotspothelpercommandtype/maintain.md)
  Maintain the connection to the network.
- [NEHotspotHelperCommandType.logoff](nehotspothelpercommandtype/logoff.md)
  Logoff the network.
### Initializers
- [init?(rawValue: Int)](nehotspothelpercommandtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var commandType: NEHotspotHelperCommandType](nehotspothelpercommand/commandtype.md)
  The type of the command
- [var network: NEHotspotNetwork?](nehotspothelpercommand/network.md)
  The network associated with the command.
- [var networkList: [NEHotspotNetwork]?](nehotspothelpercommand/networklist.md)
  The list of networks associated with the command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspothelpercommandtype)*