# NSDistantObjectRequest

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

An object used by the distributed objects system to help handle invocations between different processes.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Use [`NSXPCConnection`](./nsxpcconnection.md) instead.

## Declaration

```objc
@interface NSDistantObjectRequest : NSObject
```

## Overview

Do not create [`NSDistantObjectRequest`](./nsdistantobjectrequest.md) objects directly. Unless you are getting involved with the low-level details of distributed objects, there should never be a need to access an [`NSDistantObjectRequest`](./nsdistantobjectrequest.md). To intercept and possibly process requests yourself, implement the [`NSConnection`](./nsconnection.md) delegate method [`connection:handleRequest:`](./nsconnectiondelegate/connection_handlerequest_.md).

## Topics

### Getting Information About a Request
- [connection](./nsdistantobjectrequest/connection.md)
  Returns the `NSConnection` object involved in the request.
- [conversation](./nsdistantobjectrequest/conversation.md)
  Returns the token object representing the conversation in which the receiver was created.
- [invocation](./nsdistantobjectrequest/invocation.md)
  Returns the `NSInvocation` object for the request.
### Raising a Remote Exception
- [- replyWithException:](./nsdistantobjectrequest/replywithexception_.md)
  Sends a reply back to the remote object making the distant object request.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

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
- [NSMachBootstrapServer](./nsmachbootstrapserver.md)
  A port name server that takes and returns Mach port objects.
- [class NSMachPort](./nsmachport.md)
  A port that can be used as an endpoint for distributed object connections (or raw messaging).
- [class MessagePort](./messageport.md)
  A port that can be used as an endpoint for distributed object connections (or raw messaging).
- [NSMessagePortNameServer](./nsmessageportnameserver.md)
  A server takes and returns message ports.
- [NSPortCoder](./nsportcoder.md)
  A coder used to transmit object proxies (and sometimes objects themselves) between connections.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdistantobjectrequest)*