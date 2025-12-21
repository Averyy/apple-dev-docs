# PortMessage

**Framework**: Foundation  
**Kind**: class

A low-level, operating system-independent type for inter-application (and inter-thread) messages.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class PortMessage
```

#### Overview

Port messages are used primarily by the distributed objects system. You should implement inter-application communication using distributed objects whenever possible and use [`PortMessage`](portmessage.md) only when necessary.

An [`PortMessage`](portmessage.md) object has three major parts: the send and receive ports, which are [`Port`](port.md) objects that link the sender of the message to the receiver, and the components, which form the body of the message. The components are held as an [`NSArray`](nsarray.md) object containing [`NSData`](nsdata.md) and [`Port`](port.md) objects. The [`send(before:)`](portmessage/send(before:).md) message sends the components out through the send port; any replies to the message arrive on the receive port. See the [`Port`](port.md) class specification for information on handling incoming messages.

An [`PortMessage`](portmessage.md) instance can be initialized with a pair of [`Port`](port.md) objects and an array of components. A port message’s body can contain only [`Port`](port.md) objects or [`NSData`](nsdata.md) objects. In the distributed objects system the byte/character arrays are usually encoded [`NSInvocation`](nsinvocation.md) objects that are being forwarded from a proxy to the corresponding real object.

An [`PortMessage`](portmessage.md) object also maintains a message identifier, which can be used to indicate the class of a message, such as an Objective-C method invocation, a connection request, an error, and so on. Use the [`msgid`](portmessage/msgid.md) and [`msgid`](portmessage/msgid.md) methods to access the identifier.

## Topics

### Creating Instances
- [init(send: Port?, receive: Port?, components: [Any]?)](portmessage/init(send:receive:components:).md)
  Initializes a newly allocated `NSPortMessage` object to send given data on a given port and to receiver replies on another given port.
### Sending the Message
- [func send(before: Date) -> Bool](portmessage/send(before:).md)
  Attempts to send the message before the specified date.
### Getting the Components
- [var components: [Any]?](portmessage/components.md)
  Returns the data components of the receiver.
### Getting the Ports
- [var receivePort: Port?](portmessage/receiveport.md)
  For an outgoing message, returns the port on which replies to the receiver will arrive. For an incoming message, returns the port the receiver did arrive on.
- [var sendPort: Port?](portmessage/sendport.md)
  For an outgoing message, returns the port the receiver will send itself through. For an incoming message, returns the port replies to the receiver should be sent through.
### Accessing the Message ID
- [var msgid: UInt32](portmessage/msgid.md)
  Returns the identifier for the receiver.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol NSMachPortDelegate](nsmachportdelegate.md)
  An interface for handling incoming Mach messages.
- [class NSMachPort](nsmachport.md)
  A port that can be used as an endpoint for distributed object connections (or raw messaging).
- [class MessagePort](messageport.md)
  A port that can be used as an endpoint for distributed object connections (or raw messaging).
- [protocol PortDelegate](portdelegate.md)
  An interface for handling incoming messages.
- [class NSProtocolChecker](nsprotocolchecker.md)
  An object that restricts the messages that can be sent to another object (referred to as the checker’s delegate).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/portmessage)*