# receiveHandler

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property

A handler that delivers inbound Ethernet frames.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@preconcurrency
final var receiveHandler: (@Sendable (Data, UInt16, NWEthernetChannel.EthernetAddress, NWEthernetChannel.EthernetAddress) -> Void)? { get set }
```

## Discussion

The receive handler only needs to be set once, and will be invoked for each received Ethernet frame.

## See Also

### Sending and Receiving Ethernet Frames
- [func send(content: Data, to: NWEthernetChannel.EthernetAddress, vlanTag: UInt16, completion: (NWError?) -> Void)](./send%28content,to,vlantag,completion%29.md)
  Sends a single Ethernet frame over a channel to a specific Ethernet address.
- [NWEthernetChannel.EthernetAddress](./ethernetaddress.md)
  A 48-bit Ethernet address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwethernetchannel/receivehandler)*