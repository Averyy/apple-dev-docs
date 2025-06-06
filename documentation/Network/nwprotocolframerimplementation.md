# NWProtocolFramerImplementation

**Framework**: Network  
**Kind**: protocol

A protocol to which your classes can conform in order to implement a custom framing protocol.

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
protocol NWProtocolFramerImplementation : AnyObject
```

## Topics

### Handling Instance Lifetime
- [init(framer: NWProtocolFramer.Instance)](nwprotocolframerimplementation/init(framer:).md)
  Initializes your custom framing protocol for use in one connection attempt.
- [func start(framer: NWProtocolFramer.Instance) -> NWProtocolFramer.StartResult](nwprotocolframerimplementation/start(framer:).md)
  Requests that your protocol set up its state and begin a handshake, if necessary.
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
### Handling Data
- [func handleOutput(framer: NWProtocolFramer.Instance, message: NWProtocolFramer.Message, messageLength: Int, isComplete: Bool)](nwprotocolframerimplementation/handleoutput(framer:message:messagelength:iscomplete:).md)
  Notifies your protocol about a new outbound message.
- [func handleInput(framer: NWProtocolFramer.Instance) -> Int](nwprotocolframerimplementation/handleinput(framer:).md)
  Notifies your protocol that new inbound data is available to parse.

## See Also

- [NWProtocolFramer.Instance](nwprotocolframer/instance.md)
  An object that represents a single instance of your custom protocol running in a connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolframerimplementation)*