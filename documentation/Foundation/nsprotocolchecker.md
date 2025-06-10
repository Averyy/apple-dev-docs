# NSProtocolChecker

**Framework**: Foundation  
**Kind**: class

An object that restricts the messages that can be sent to another object (referred to as the checker’s delegate).

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSProtocolChecker
```

#### Overview

A [`NSProtocolChecker`](nsprotocolchecker.md) object can be particularly useful when an object with many methods, only a few of which ought to be remotely accessible, is made available using the distributed objects system.

A protocol checker acts as a kind of proxy; when it receives a message that is in its designated protocol, it forwards the message to its target and consequently appears to be the target object itself. However, when it receives a message not in its protocol, it raises an [`invalidArgumentException`](nsexceptionname/invalidargumentexception.md) to indicate that the message isn’t allowed, whether or not the target object implements the method.

Typically, an object that is to be distributed (yet must restrict messages) creates an [`NSProtocolChecker`](nsprotocolchecker.md) for itself and returns the checker rather than returning itself in response to any messages. The object might also register the checker as the root object of an NSConnection.

The object should be careful about vending references to `self`—the protocol checker will convert a return value of `self` to indicate the checker rather than the object for any messages forwarded by the checker, but direct references to the object (bypassing the checker) could be passed around by other objects.

## Topics

### Creating a checker
- [init(target: NSObject, protocol: Protocol)](nsprotocolchecker/init(target:protocol:).md)
  Initializes a newly allocated `NSProtocolChecker` instance that will forward any messages in `aProtocol` to `anObject`, the protocol checker’s target.
### Getting information
- [var `protocol`: Protocol](nsprotocolchecker/protocol.md)
  Returns the protocol object the receiver uses.
- [var target: NSObject?](nsprotocolchecker/target.md)
  Returns the target of the receiver.

## Relationships

### Inherits From
- [NSProxy](nsproxy.md)
### Conforms To
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol NSMachPortDelegate](nsmachportdelegate.md)
  An interface for handling incoming Mach messages.
- [class NSMachPort](nsmachport.md)
  A port that can be used as an endpoint for distributed object connections (or raw messaging).
- [class MessagePort](messageport.md)
  A port that can be used as an endpoint for distributed object connections (or raw messaging).
- [protocol PortDelegate](portdelegate.md)
  An interface for handling incoming messages.
- [class PortMessage](portmessage.md)
  A low-level, operating system-independent type for inter-application (and inter-thread) messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsprotocolchecker)*