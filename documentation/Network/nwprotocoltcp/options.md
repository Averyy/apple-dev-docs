# NWProtocolTCP.Options

**Framework**: Network  
**Kind**: class

A container of options for configuring how TCP is used on a connection.

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
class Options
```

## Topics

### Customizing TCP Options
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
- [var disableAckStretching: Bool](nwprotocoltcp/options/disableackstretching.md)
  A Boolean that disables TCP acknowledgment stretching.
- [var disableECN: Bool](nwprotocoltcp/options/disableecn.md)
  A Boolean that disables negotiation of Explicit Congestion Notification markings.
### Configuring Keepalives
- [var enableKeepalive: Bool](nwprotocoltcp/options/enablekeepalive.md)
  A Boolean that enables TCP keepalives.
- [var keepaliveIdle: Int](nwprotocoltcp/options/keepaliveidle.md)
  The number of seconds of idleness that TCP waits before sending keepalive probes.
- [var keepaliveCount: Int](nwprotocoltcp/options/keepalivecount.md)
  The number of keepalive probes that TCP sends before terminating the connection.
- [var keepaliveInterval: Int](nwprotocoltcp/options/keepaliveinterval.md)
  The number of seconds that TCP waits between sending keepalive probes.
### Setting Timeouts
- [var connectionTimeout: Int](nwprotocoltcp/options/connectiontimeout.md)
  The number of seconds that TCP waits before timing out its handshake.
- [var connectionDropTime: Int](nwprotocoltcp/options/connectiondroptime.md)
  The timeout, in seconds, for TCP retransmission attempts.
- [var persistTimeout: Int](nwprotocoltcp/options/persisttimeout.md)
  The TCP persist timeout, in seconds, as defined by RFC 6429.

## Relationships

### Inherits From
- [NWProtocolOptions](nwprotocoloptions.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [static let definition: NWProtocolDefinition](nwprotocoltcp/definition.md)
  The system definition of the Transport Control Protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocoltcp/options)*