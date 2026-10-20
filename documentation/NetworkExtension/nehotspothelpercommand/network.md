# network

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The network associated with the command.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var network: NEHotspotNetwork? { get }
```

```objc
@property (readonly, nullable) NEHotspotNetwork * network;
```

## See Also

### Command information
- [var commandType: NEHotspotHelperCommandType](./commandtype.md)
  The type of the command
- [enum NEHotspotHelperCommandType](../nehotspothelpercommandtype.md)
  An enumeration of hotspot command types.
- [var networkList: [NEHotspotNetwork]?](./networklist.md)
  The list of networks associated with the command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspothelpercommand/network)*