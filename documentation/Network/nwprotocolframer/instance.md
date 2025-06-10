# NWProtocolFramer.Instance

**Framework**: Network  
**Kind**: class

An object that represents a single instance of your custom protocol running in a connection.

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
final class Instance
```

#### Overview

All interaction between your protocol and the connection occurs through this object.

## Topics

### Writing Output
- [func parseOutput(minimumIncompleteLength: Int, maximumLength: Int, parse: (UnsafeMutableRawBufferPointer?, Bool) -> Int) -> Bool](nwprotocolframer/instance/parseoutput(minimumincompletelength:maximumlength:parse:).md)
  Examines the content of output data while inside your output handler.
- [func writeOutput(data: Data)](nwprotocolframer/instance/writeoutput(data:)-ydvk.md)
  Sends arbitrary output data from your protocol to the next protocol.
- [func writeOutputNoCopy(length: Int) throws](nwprotocolframer/instance/writeoutputnocopy(length:).md)
  Sends a specific number of bytes from a message while inside your output handler.
- [func passThroughOutput()](nwprotocolframer/instance/passthroughoutput.md)
  Indicates that your protocol no longer needs to handle output data.
### Delivering Input
- [func parseInput(minimumIncompleteLength: Int, maximumLength: Int, parse: (UnsafeMutableRawBufferPointer?, Bool) -> Int) -> Bool](nwprotocolframer/instance/parseinput(minimumincompletelength:maximumlength:parse:).md)
  Examines the content of input data while in your input handler.
- [func deliverInput(data: Data, message: NWProtocolFramer.Message, isComplete: Bool)](nwprotocolframer/instance/deliverinput(data:message:iscomplete:).md)
  Delivers an inbound message containing arbitrary data from your protocol to the application.
- [func deliverInputNoCopy(length: Int, message: NWProtocolFramer.Message, isComplete: Bool) -> Bool](nwprotocolframer/instance/deliverinputnocopy(length:message:iscomplete:).md)
  Delivers an inbound message containing a specific number of next received bytes.
- [func passThroughInput()](nwprotocolframer/instance/passthroughinput.md)
  Indicates that your protocol no longer needs to handle input data.
### Managing Instance Lifetime
- [func markReady()](nwprotocolframer/instance/markready.md)
  Indicates to a connection that your protocol’s handshake is complete.
- [func markFailed(error: NWError?)](nwprotocolframer/instance/markfailed(error:).md)
  Indicates to a connection that your protocol has encountered an error, or has gracefully closed.
- [func prependApplicationProtocol(options: NWProtocolOptions) throws](nwprotocolframer/instance/prependapplicationprotocol(options:).md)
  Dynamically adds another protocol that will run above your protocol after your protocol calls [`markReady()`](nwprotocolframer/instance/markready().md).
### Inspecting Instance Properties
- [var remote: NWEndpoint?](nwprotocolframer/instance/remote.md)
  The remote endpoint of the connection in which your protocol is running.
- [var local: NWEndpoint?](nwprotocolframer/instance/local.md)
  The local endpoint of the connection in which your protocol is running.
- [var parameters: NWParameters?](nwprotocolframer/instance/parameters.md)
  The parameters of the connection in which your protocol is running.
### Handling Asynchronous Events
- [func async(execute: () -> Void)](nwprotocolframer/instance/async(execute:).md)
  Requests that a block be executed on the connection’s internal scheduling context.
- [func scheduleWakeup(wakeupTime: NWProtocolFramer.Instance.WakeupTime)](nwprotocolframer/instance/schedulewakeup(wakeuptime:).md)
  Requests that [`wakeup(framer:)`](nwprotocolframerimplementation/wakeup(framer:).md) be called on your protocol at a specific time in the future.
- [NWProtocolFramer.Instance.WakeupTime](nwprotocolframer/instance/wakeuptime.md)
  Times at which to schedule a protocol wakeup.
### Instance Properties
- [var options: NWProtocolFramer.Options](nwprotocolframer/instance/options.md)
### Instance Methods
- [func writeOutput<Output>(data: Output)](nwprotocolframer/instance/writeoutput(data:)-9axn3.md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol NWProtocolFramerImplementation](nwprotocolframerimplementation.md)
  A protocol to which your classes can conform in order to implement a custom framing protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolframer/instance)*