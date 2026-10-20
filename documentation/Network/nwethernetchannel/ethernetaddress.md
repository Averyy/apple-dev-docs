# NWEthernetChannel.EthernetAddress

**Framework**: Network  
**Kind**: struct  
**Role**: Structure

A 48-bit Ethernet address.

**Availability**:
- macOS 10.15+

## Declaration

```swift
struct EthernetAddress
```

## Topics

### Creating Addresses
- [init?(Data)](./ethernetaddress/init%28_%29-62x9i.md)
  Initializes an Ethernet address with data.
- [init?(String)](./ethernetaddress/init%28_%29-1brh7.md)
  Initializes an Ethernet address with a string.
### Inspecting Addresses
- [var rawValue: Data](./ethernetaddress/rawvalue.md)
  The raw data of the Ethernet address.

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Sending and Receiving Ethernet Frames
- [func send(content: Data, to: NWEthernetChannel.EthernetAddress, vlanTag: UInt16, completion: (NWError?) -> Void)](./send%28content,to,vlantag,completion%29.md)
  Sends a single Ethernet frame over a channel to a specific Ethernet address.
- [var receiveHandler: ((Data, UInt16, NWEthernetChannel.EthernetAddress, NWEthernetChannel.EthernetAddress) -> Void)?](./receivehandler.md)
  A handler that delivers inbound Ethernet frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwethernetchannel/ethernetaddress)*