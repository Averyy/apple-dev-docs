# NWProtocolFramer.Instance

**Framework**: Network  
**Kind**: class  
**Role**: Class

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
- [func parseOutput(minimumIncompleteLength: Int, maximumLength: Int, parse: (UnsafeMutableRawBufferPointer?, Bool) -> Int) -> Bool](./instance/parseoutput%28minimumincompletelength,maximumlength,parse%29.md)
  Examines the content of output data while inside your output handler.
- [func writeOutput(data: Data)](./instance/writeoutput%28data%29-ydvk.md)
  Sends arbitrary output data from your protocol to the next protocol.
- [func writeOutputNoCopy(length: Int) throws](./instance/writeoutputnocopy%28length%29.md)
  Sends a specific number of bytes from a message while inside your output handler.
- [func passThroughOutput()](./instance/passthroughoutput%28%29.md)
  Indicates that your protocol no longer needs to handle output data.
### Delivering Input
- [func parseInput(minimumIncompleteLength: Int, maximumLength: Int, parse: (UnsafeMutableRawBufferPointer?, Bool) -> Int) -> Bool](./instance/parseinput%28minimumincompletelength,maximumlength,parse%29.md)
  Examines the content of input data while in your input handler.
- [func deliverInput(data: Data, message: NWProtocolFramer.Message, isComplete: Bool)](./instance/deliverinput%28data,message,iscomplete%29.md)
  Delivers an inbound message containing arbitrary data from your protocol to the application.
- [func deliverInputNoCopy(length: Int, message: NWProtocolFramer.Message, isComplete: Bool) -> Bool](./instance/deliverinputnocopy%28length,message,iscomplete%29.md)
  Delivers an inbound message containing a specific number of next received bytes.
- [func passThroughInput()](./instance/passthroughinput%28%29.md)
  Indicates that your protocol no longer needs to handle input data.
### Managing Instance Lifetime
- [func markReady()](./instance/markready%28%29.md)
  Indicates to a connection that your protocol’s handshake is complete.
- [func markFailed(error: NWError?)](./instance/markfailed%28error%29.md)
  Indicates to a connection that your protocol has encountered an error, or has gracefully closed.
- [func prependApplicationProtocol(options: NWProtocolOptions) throws](./instance/prependapplicationprotocol%28options%29.md)
  Dynamically adds another protocol that will run above your protocol after your protocol calls [`markReady()`](./instance/markready%28%29.md).
### Inspecting Instance Properties
- [var remote: NWEndpoint?](./instance/remote.md)
  The remote endpoint of the connection in which your protocol is running.
- [var local: NWEndpoint?](./instance/local.md)
  The local endpoint of the connection in which your protocol is running.
- [var parameters: NWParameters?](./instance/parameters.md)
  The parameters of the connection in which your protocol is running.
### Handling Asynchronous Events
- [func async(execute: () -> Void)](./instance/async%28execute%29.md)
  Requests that a block be executed on the connection’s internal scheduling context.
- [func scheduleWakeup(wakeupTime: NWProtocolFramer.Instance.WakeupTime)](./instance/schedulewakeup%28wakeuptime%29.md)
  Requests that [`wakeup(framer:)`](../nwprotocolframerimplementation/wakeup%28framer%29.md) be called on your protocol at a specific time in the future.
- [NWProtocolFramer.Instance.WakeupTime](./instance/wakeuptime.md)
  Times at which to schedule a protocol wakeup.
### Instance Properties
- [var options: NWProtocolFramer.Options](./instance/options.md)
### Instance Methods
- [func prependApplicationProtocolIgnoringReady(options: NWProtocolOptions) throws](./instance/prependapplicationprotocolignoringready%28options%29.md)
  Dynamically add a protocol to a connection establishment attempt “above” the framer protocol. This means that the protocol above will start running once the framer becomes ready by calling markReady(). This can only be used with framers that return a value of willMarkReady to their start handlers. An example of using this functionality is adding a security protocol, like TLS, above a framer once that framer completes its initial handshake.
- [func writeOutput<Output>(data: Output)](./instance/writeoutput%28data%29-9axn3.md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Implementing Framer Protocols
- [protocol NWProtocolFramerImplementation](../nwprotocolframerimplementation.md)
  A protocol to which your classes can conform in order to implement a custom framing protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolframer/instance)*