# NWEthernetChannel.EthernetAddress

**Framework**: Network  
**Kind**: struct

A 48-bit Ethernet address.

**Availability**:
- macOS 10.15+

## Declaration

```swift
struct EthernetAddress
```

## Topics

### Creating Addresses
- [init?(Data)](nwethernetchannel/ethernetaddress/init(_:)-62x9i.md)
  Initializes an Ethernet address with data.
- [init?(String)](nwethernetchannel/ethernetaddress/init(_:)-1brh7.md)
  Initializes an Ethernet address with a string.
### Inspecting Addresses
- [var rawValue: Data](nwethernetchannel/ethernetaddress/rawvalue.md)
  The raw data of the Ethernet address.

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func send(content: Data, to: NWEthernetChannel.EthernetAddress, vlanTag: UInt16, completion: (NWError?) -> Void)](nwethernetchannel/send(content:to:vlantag:completion:).md)
  Sends a single Ethernet frame over a channel to a specific Ethernet address.
- [var receiveHandler: ((Data, UInt16, NWEthernetChannel.EthernetAddress, NWEthernetChannel.EthernetAddress) -> Void)?](nwethernetchannel/receivehandler.md)
  A handler that delivers inbound Ethernet frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwethernetchannel/ethernetaddress)*