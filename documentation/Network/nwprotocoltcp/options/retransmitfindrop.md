# retransmitFinDrop

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property

A Boolean that causes TCP to drop its connection after not receiving an ACK packet after a FIN packet.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var retransmitFinDrop: Bool { get set }
```

## See Also

### Customizing TCP Options
- [init()](./init%28%29.md)
  Initializes a default set of TCP connection options.
- [var enableFastOpen: Bool](./enablefastopen.md)
  A Boolean that enables TCP Fast Open on a connection.
- [var maximumSegmentSize: Int](./maximumsegmentsize.md)
  TCP’s maximum segment size in bytes.
- [var noDelay: Bool](./nodelay.md)
  A Boolean that disables Nagle’s algorithm for TCP.
- [var noOptions: Bool](./nooptions.md)
  A Boolean that sets TCP into no-options mode.
- [var noPush: Bool](./nopush.md)
  A Boolean that sets TCP into no-push mode.
- [var disableAckStretching: Bool](./disableackstretching.md)
  A Boolean that disables TCP acknowledgment stretching.
- [var disableECN: Bool](./disableecn.md)
  A Boolean that disables negotiation of Explicit Congestion Notification markings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocoltcp/options/retransmitfindrop)*