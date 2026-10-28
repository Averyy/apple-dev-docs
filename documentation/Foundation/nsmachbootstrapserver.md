# NSMachBootstrapServer

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A port name server that takes and returns Mach port objects.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Use [`NSXPCConnection`](./nsxpcconnection.md) instead.

## Declaration

```objc
@interface NSMachBootstrapServer : NSPortNameServer
```

## Overview

Port removal functionality is not supported in [`NSMachBootstrapServer`](./nsmachbootstrapserver.md); if you want to cancel a service, you have to destroy the port (invalidate the [`NSMachPort`](./nsmachport.md) given to [`registerPort:name:`](./nsmachbootstrapserver/registerport_name_.md)).

## Topics

### Getting the Server Object
- [+ sharedInstance](./nsmachbootstrapserver/sharedinstance.md)
  Returns the shared instance of the bootstrap server.
### Looking up Ports
- [- portForName:](./nsmachbootstrapserver/portforname_.md)
  Looks up and returns the port registered under the specified name on the local host.
- [- portForName:host:](./nsmachbootstrapserver/portforname_host_.md)
  Looks up and returns the port registered under the specified name.
- [- servicePortWithName:](./nsmachbootstrapserver/serviceportwithname_.md)
  Looks up and returns the port for the vended service that is registered under the specified name.
### Registering Ports
- [- registerPort:name:](./nsmachbootstrapserver/registerport_name_.md)
  Registers a port with a specified name.

## Relationships

### Inherits From
- [NSPortNameServer](./nsportnameserver.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmachbootstrapserver)*