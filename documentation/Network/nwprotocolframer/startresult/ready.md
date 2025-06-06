# NWProtocolFramer.StartResult.ready

**Framework**: Network  
**Kind**: case

The protocol is immediately ready to send and receive data.

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
case ready
```

## See Also

- [NWProtocolFramer.StartResult.willMarkReady](nwprotocolframer/startresult/willmarkready.md)
  The protocol will perform a handshake, preventing the overall connection from becoming ready until [`markReady()`](nwprotocolframer/instance/markready().md) is called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolframer/startresult/ready)*