# NWProtocolFramer.StartResult

**Framework**: Network  
**Kind**: enum  
**Role**: Enumeration

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
- [NWProtocolFramer.StartResult.ready](./startresult/ready.md)
  The protocol is immediately ready to send and receive data.
- [NWProtocolFramer.StartResult.willMarkReady](./startresult/willmarkready.md)
  The protocol will perform a handshake, preventing the overall connection from becoming ready until [`markReady()`](./instance/markready%28%29.md) is called.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Handling Instance Lifetime
- [init(framer: NWProtocolFramer.Instance)](../nwprotocolframerimplementation/init%28framer%29.md)
  Initializes your custom framing protocol for use in one connection attempt.
- [func start(framer: NWProtocolFramer.Instance) -> NWProtocolFramer.StartResult](../nwprotocolframerimplementation/start%28framer%29.md)
  Requests that your protocol set up its state and begin a handshake, if necessary.
- [func wakeup(framer: NWProtocolFramer.Instance)](../nwprotocolframerimplementation/wakeup%28framer%29.md)
  Delivers a scheduled wakeup event.
- [func stop(framer: NWProtocolFramer.Instance) -> Bool](../nwprotocolframerimplementation/stop%28framer%29.md)
  Requests that your protocol send any final messages to close the connection.
- [func cleanup(framer: NWProtocolFramer.Instance)](../nwprotocolframerimplementation/cleanup%28framer%29.md)
  Indicates that your protocol should clean up all allocations before being deallocated.
- [static var label: String](../nwprotocolframerimplementation/label.md)
  A label defined by your custom protocol for use in debugging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolframer/startresult)*