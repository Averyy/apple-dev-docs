# NSProtocolChecker

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

An object that restricts the messages that can be sent to another object (referred to as the checker’s delegate).

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSProtocolChecker
```

```objc
@interface NSProtocolChecker : NSProxy
```

#### Overview

A [`NSProtocolChecker`](./nsprotocolchecker.md) object can be particularly useful when an object with many methods, only a few of which ought to be remotely accessible, is made available using the distributed objects system.

A protocol checker acts as a kind of proxy; when it receives a message that is in its designated protocol, it forwards the message to its target and consequently appears to be the target object itself. However, when it receives a message not in its protocol, it raises an [`invalidArgumentException`](./nsexceptionname/invalidargumentexception.md) to indicate that the message isn’t allowed, whether or not the target object implements the method.

Typically, an object that is to be distributed (yet must restrict messages) creates an [`NSProtocolChecker`](./nsprotocolchecker.md) for itself and returns the checker rather than returning itself in response to any messages. The object might also register the checker as the root object of an NSConnection.

The object should be careful about vending references to `self`—the protocol checker will convert a return value of `self` to indicate the checker rather than the object for any messages forwarded by the checker, but direct references to the object (bypassing the checker) could be passed around by other objects.

## Topics

### Creating a checker
- [init(target: NSObject, protocol: Protocol)](./nsprotocolchecker/init%28target,protocol%29.md)
  Initializes a newly allocated `NSProtocolChecker` instance that will forward any messages in `aProtocol` to `anObject`, the protocol checker’s target.
- [+ protocolCheckerWithTarget:protocol:](./nsprotocolchecker/protocolcheckerwithtarget_protocol_.md)
  Allocates and initializes an `NSProtocolChecker` instance that will forward any messages in `aProtocol` to `anObject`, the protocol checker’s target.
### Getting information
- [var `protocol`: Protocol](./nsprotocolchecker/protocol.md)
  Returns the protocol object the receiver uses.
- [var target: NSObject?](./nsprotocolchecker/target.md)
  Returns the target of the receiver.

## Relationships

### Inherits From
- [NSProxy](./nsproxy.md)
### Conforms To
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Legacy
- [protocol NSMachPortDelegate](./nsmachportdelegate.md)
  An interface for handling incoming Mach messages.
- [class NSMachPort](./nsmachport.md)
  A port that can be used as an endpoint for distributed object connections (or raw messaging).
- [class MessagePort](./messageport.md)
  A port that can be used as an endpoint for distributed object connections (or raw messaging).
- [protocol PortDelegate](./portdelegate.md)
  An interface for handling incoming messages.
- [class PortMessage](./portmessage.md)
  A low-level, operating system-independent type for inter-application (and inter-thread) messages.
- [NSConnectionDelegate](./nsconnectiondelegate.md)
  An interface for interacting with low-level, interprocess connections.
- [NSConnection](./nsconnection.md)
  An object that manages the communication between objects in different threads or between a thread and a process running on a local or remote system.
- [NSDistantObject](./nsdistantobject.md)
  A proxy for objects in other applications or threads.
- [NSDistantObjectRequest](./nsdistantobjectrequest.md)
  An object used by the distributed objects system to help handle invocations between different processes.
- [NSMachBootstrapServer](./nsmachbootstrapserver.md)
  A port name server that takes and returns Mach port objects.
- [NSMessagePortNameServer](./nsmessageportnameserver.md)
  A server takes and returns message ports.
- [NSPortCoder](./nsportcoder.md)
  A coder used to transmit object proxies (and sometimes objects themselves) between connections.
- [NSPortNameServer](./nsportnameserver.md)
  An object-oriented interface to the port registration service used by the distributed objects system.
- [NSSocketPortNameServer](./nssocketportnameserver.md)
  A port name server that takes and returns socket ports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsprotocolchecker)*