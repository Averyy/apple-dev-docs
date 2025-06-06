# disableAckStretching

**Framework**: Network  
**Kind**: property

A Boolean that disables TCP acknowledgment stretching.

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
var disableAckStretching: Bool { get set }
```

## See Also

- [init()](nwprotocoltcp/options/init.md)
  Initializes a default set of TCP connection options.
- [var enableFastOpen: Bool](nwprotocoltcp/options/enablefastopen.md)
  A Boolean that enables TCP Fast Open on a connection.
- [var maximumSegmentSize: Int](nwprotocoltcp/options/maximumsegmentsize.md)
  TCP’s maximum segment size in bytes.
- [var noDelay: Bool](nwprotocoltcp/options/nodelay.md)
  A Boolean that disables Nagle’s algorithm for TCP.
- [var noOptions: Bool](nwprotocoltcp/options/nooptions.md)
  A Boolean that sets TCP into no-options mode.
- [var noPush: Bool](nwprotocoltcp/options/nopush.md)
  A Boolean that sets TCP into no-push mode.
- [var retransmitFinDrop: Bool](nwprotocoltcp/options/retransmitfindrop.md)
  A Boolean that causes TCP to drop its connection after not receiving an ACK packet after a FIN packet.
- [var disableECN: Bool](nwprotocoltcp/options/disableecn.md)
  A Boolean that disables negotiation of Explicit Congestion Notification markings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocoltcp/options/disableackstretching)*