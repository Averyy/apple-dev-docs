# NWProtocolFramer.StartResult.willMarkReady

**Framework**: Network  
**Kind**: case

The protocol will perform a handshake, preventing the overall connection from becoming ready until [`markReady()`](nwprotocolframer/instance/markready().md) is called.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case willMarkReady
```

## See Also

- [func markReady()](nwprotocolframer/instance/markready.md)
  Indicates to a connection that your protocol’s handshake is complete.
- [NWProtocolFramer.StartResult.ready](nwprotocolframer/startresult/ready.md)
  The protocol is immediately ready to send and receive data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolframer/startresult/willmarkready)*