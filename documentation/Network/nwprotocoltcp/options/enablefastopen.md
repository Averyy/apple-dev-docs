# enableFastOpen

**Framework**: Network  
**Kind**: property

A Boolean that enables TCP Fast Open on a connection.

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
var enableFastOpen: Bool { get set }
```

#### Discussion

If TCP Fast Open is enabled and TLS is running on top of TCP, the TLS handshake will automatically be used as the TCP early data. If there is no protocol running on top of TCP, you should also enable fast open on the connection parameters and send idempotent data.

## See Also

- [var allowFastOpen: Bool](nwparameters/allowfastopen.md)
  A Boolean that enables sending application data with protocol handshakes.
- [NWConnection.SendCompletion.idempotent](nwconnection/sendcompletion/idempotent.md)
  Mark the sent data as idempotent—data that can be sent multiple times.
- [init()](nwprotocoltcp/options/init.md)
  Initializes a default set of TCP connection options.
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
- [var disableAckStretching: Bool](nwprotocoltcp/options/disableackstretching.md)
  A Boolean that disables TCP acknowledgment stretching.
- [var disableECN: Bool](nwprotocoltcp/options/disableecn.md)
  A Boolean that disables negotiation of Explicit Congestion Notification markings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocoltcp/options/enablefastopen)*