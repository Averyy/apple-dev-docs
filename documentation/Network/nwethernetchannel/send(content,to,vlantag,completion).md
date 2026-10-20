# send(content:to:vlanTag:completion:)

**Framework**: Network  
**Kind**: method  
**Role**: Instance Method

Sends a single Ethernet frame over a channel to a specific Ethernet address.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@preconcurrency
final func send(content: Data, to remoteAddress: NWEthernetChannel.EthernetAddress, vlanTag: UInt16, completion: @escaping @Sendable (NWError?) -> Void)
```

## See Also

### Sending and Receiving Ethernet Frames
- [var receiveHandler: ((Data, UInt16, NWEthernetChannel.EthernetAddress, NWEthernetChannel.EthernetAddress) -> Void)?](./receivehandler.md)
  A handler that delivers inbound Ethernet frames.
- [NWEthernetChannel.EthernetAddress](./ethernetaddress.md)
  A 48-bit Ethernet address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwethernetchannel/send(content:to:vlantag:completion:))*