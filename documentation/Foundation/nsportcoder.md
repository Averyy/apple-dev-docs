# NSPortCoder

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A coder used to transmit object proxies (and sometimes objects themselves) between connections.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Use [`NSXPCConnection`](./nsxpcconnection.md) instead.

## Declaration

```objc
@interface NSPortCoder : NSCoder
```

## Overview

[`NSPortCoder`](./nsportcoder.md) is a concrete subclass of [`NSCoder`](./nscoder.md) used in the distributed objects system to transmit object proxies (and sometimes objects themselves) between [`NSConnection`](./nsconnection.md) objects. An [`NSPortCoder`](./nsportcoder.md) instance is always created and used by an [`NSConnection`](./nsconnection.md) object; you should never need to explicitly create or use one directly yourself.

## Topics

### Creating an NSPortCoder Object
- [+ portCoderWithReceivePort:sendPort:components:](./nsportcoder/portcoderwithreceiveport_sendport_components_.md)
  Creates and returns a new `NSPortCoder` object.
- [- initWithReceivePort:sendPort:components:](./nsportcoder/initwithreceiveport_sendport_components_.md)
  Initializes and returns an `NSPortCoder` object.
### Getting the Connection
- [- connection](./nsportcoder/connection.md)
  Returns the `NSConnection` object that uses the receiver.
### Encoding NSPort Objects
- [- encodePortObject:](./nsportcoder/encodeportobject_.md)
  Encodes a given port so it can be properly reconstituted in the receiving process or thread.
- [- decodePortObject](./nsportcoder/decodeportobject.md)
  Decodes and returns an `NSPort` object that was previously encoded with any of the general `encode...Object:` messages.
### Checking for Encoding
- [- isBycopy](./nsportcoder/isbycopy.md)
  Returns a Boolean value that indicates whether the receiver is encoding an object by copying it.
- [- isByref](./nsportcoder/isbyref.md)
  Returns a Boolean value that indicates whether the receiver is encoding an object by reference.
### Dispatching
- [- dispatch](./nsportcoder/dispatch.md)
  Processes and acts upon the distributed object message with which the receiver was initialized.

## Relationships

### Inherits From
- [NSCoder](./nscoder.md)

## See Also

### Legacy
- [protocol NSMachPortDelegate](./nsmachportdelegate.md)
  An interface for handling incoming Mach messages.
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
- [class NSMachPort](./nsmachport.md)
  A port that can be used as an endpoint for distributed object connections (or raw messaging).
- [class MessagePort](./messageport.md)
  A port that can be used as an endpoint for distributed object connections (or raw messaging).
- [NSMessagePortNameServer](./nsmessageportnameserver.md)
  A server takes and returns message ports.
- [protocol PortDelegate](./portdelegate.md)
  An interface for handling incoming messages.
- [class PortMessage](./portmessage.md)
  A low-level, operating system-independent type for inter-application (and inter-thread) messages.
- [NSPortNameServer](./nsportnameserver.md)
  An object-oriented interface to the port registration service used by the distributed objects system.
- [class NSProtocolChecker](./nsprotocolchecker.md)
  An object that restricts the messages that can be sent to another object (referred to as the checker’s delegate).
- [NSSocketPortNameServer](./nssocketportnameserver.md)
  A port name server that takes and returns socket ports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsportcoder)*