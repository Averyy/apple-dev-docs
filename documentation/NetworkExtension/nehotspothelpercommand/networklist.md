# networkList

**Framework**: Network Extension  
**Kind**: property

The list of networks associated with the command.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var networkList: [NEHotspotNetwork]? { get }
```

#### Discussion

This property will be nil unless `commandType` is `kNEHotspotHelperCommandTypeFilterScanList`.

## See Also

- [var commandType: NEHotspotHelperCommandType](nehotspothelpercommand/commandtype.md)
  The type of the command
- [enum NEHotspotHelperCommandType](nehotspothelpercommandtype.md)
  An enumeration of hotspot command types.
- [var network: NEHotspotNetwork?](nehotspothelpercommand/network.md)
  The network associated with the command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspothelpercommand/networklist)*