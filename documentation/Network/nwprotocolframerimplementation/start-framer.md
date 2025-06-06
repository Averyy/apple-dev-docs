# start(framer:)

**Framework**: Network  
**Kind**: method  
**Required**: Yes

Requests that your protocol set up its state and begin a handshake, if necessary.

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
func start(framer: NWProtocolFramer.Instance) -> NWProtocolFramer.StartResult
```

## See Also

- [init(framer: NWProtocolFramer.Instance)](nwprotocolframerimplementation/init(framer:).md)
  Initializes your custom framing protocol for use in one connection attempt.
- [NWProtocolFramer.StartResult](nwprotocolframer/startresult.md)
  Results that you send to indicate the disposition of your protocol after receiving the call to start.
- [func wakeup(framer: NWProtocolFramer.Instance)](nwprotocolframerimplementation/wakeup(framer:).md)
  Delivers a scheduled wakeup event.
- [func stop(framer: NWProtocolFramer.Instance) -> Bool](nwprotocolframerimplementation/stop(framer:).md)
  Requests that your protocol send any final messages to close the connection.
- [func cleanup(framer: NWProtocolFramer.Instance)](nwprotocolframerimplementation/cleanup(framer:).md)
  Indicates that your protocol should clean up all allocations before being deallocated.
- [static var label: String](nwprotocolframerimplementation/label.md)
  A label defined by your custom protocol for use in debugging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolframerimplementation/start(framer:))*