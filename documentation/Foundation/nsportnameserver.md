# NSPortNameServer

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

An object-oriented interface to the port registration service used by the distributed objects system.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Use [`NSXPCConnection`](./nsxpcconnection.md) instead.

## Declaration

```objc
@interface NSPortNameServer : NSObject
```

#### Overview

[`NSConnection`](./nsconnection.md) objects use this interface to contact each other and to distribute objects over the network; you should rarely need to interact directly with an [`NSPortNameServer`](./nsportnameserver.md).

You get an [`NSPortNameServer`](./nsportnameserver.md) object by using the [`systemDefaultPortNameServer`](./nsportnameserver/systemdefaultportnameserver.md) class method—never allocate and initialize an instance directly. With the default server object you can register an [`Port`](./port.md) object under a given name, making it available on the network, and also unregister it so that it can’t be looked up (although other applications that have already looked up the [`Port`](./port.md) object  can still use it until it becomes invalid). See the [`Port`](./port.md) class specification for more information.

## Topics

### Getting the Server Object
- [+ systemDefaultPortNameServer](./nsportnameserver/systemdefaultportnameserver.md)
  Returns the single instance of `NSPortNameServer` for the application.
### Looking up Ports
- [- portForName:](./nsportnameserver/portforname_.md)
  Looks up and returns the port registered under the specified name on the local host.
- [- portForName:host:](./nsportnameserver/portforname_host_.md)
  Looks up and returns the port registered under the specified name on a specified host.
### Registering Ports
- [- registerPort:name:](./nsportnameserver/registerport_name_.md)
  Makes a given port available on the network under a specified name.
- [- removePortForName:](./nsportnameserver/removeportforname_.md)
  Unregisters the port for a given name on the local host.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [NSMachBootstrapServer](./nsmachbootstrapserver.md)
- [NSMessagePortNameServer](./nsmessageportnameserver.md)
- [NSSocketPortNameServer](./nssocketportnameserver.md)

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
- [NSPortCoder](./nsportcoder.md)
  A coder used to transmit object proxies (and sometimes objects themselves) between connections.
- [protocol PortDelegate](./portdelegate.md)
  An interface for handling incoming messages.
- [class PortMessage](./portmessage.md)
  A low-level, operating system-independent type for inter-application (and inter-thread) messages.
- [class NSProtocolChecker](./nsprotocolchecker.md)
  An object that restricts the messages that can be sent to another object (referred to as the checker’s delegate).
- [NSSocketPortNameServer](./nssocketportnameserver.md)
  A port name server that takes and returns socket ports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsportnameserver)*