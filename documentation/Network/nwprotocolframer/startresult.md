# NWProtocolFramer.StartResult

**Framework**: Network  
**Kind**: enum

Results that you send to indicate the disposition of your protocol after receiving the call to start.

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
enum StartResult
```

## Topics

### Start Results
- [NWProtocolFramer.StartResult.ready](nwprotocolframer/startresult/ready.md)
  The protocol is immediately ready to send and receive data.
- [NWProtocolFramer.StartResult.willMarkReady](nwprotocolframer/startresult/willmarkready.md)
  The protocol will perform a handshake, preventing the overall connection from becoming ready until [`markReady()`](nwprotocolframer/instance/markready().md) is called.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [init(framer: NWProtocolFramer.Instance)](nwprotocolframerimplementation/init(framer:).md)
  Initializes your custom framing protocol for use in one connection attempt.
- [func start(framer: NWProtocolFramer.Instance) -> NWProtocolFramer.StartResult](nwprotocolframerimplementation/start(framer:).md)
  Requests that your protocol set up its state and begin a handshake, if necessary.
- [func wakeup(framer: NWProtocolFramer.Instance)](nwprotocolframerimplementation/wakeup(framer:).md)
  Delivers a scheduled wakeup event.
- [func stop(framer: NWProtocolFramer.Instance) -> Bool](nwprotocolframerimplementation/stop(framer:).md)
  Requests that your protocol send any final messages to close the connection.
- [func cleanup(framer: NWProtocolFramer.Instance)](nwprotocolframerimplementation/cleanup(framer:).md)
  Indicates that your protocol should clean up all allocations before being deallocated.
- [static var label: String](nwprotocolframerimplementation/label.md)
  A label defined by your custom protocol for use in debugging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolframer/startresult)*