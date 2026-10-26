# NSSocketPortNameServer

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A port name server that takes and returns socket ports.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Use [`NSXPCConnection`](./nsxpcconnection.md) instead.

## Declaration

```objc
@interface NSSocketPortNameServer : NSPortNameServer
```

#### Overview

Port removal functionality is supported by the [`removePortForName:`](./nssocketportnameserver/removeportforname_.md) method and should be used to remove invalid socket ports.

Unlike the other port name servers, [`NSSocketPortNameServer`](./nssocketportnameserver.md) can operate over a network. By registering your socket ports, you make them available to other computers on the local network without hard-coding the TCP port numbers. Clients just need to know the name of the port.

[`NSPortNameServer`](./nsportnameserver.md) is implemented using [`NetService`](./netservice.md) and registers ports in the local network domain. The registered name of a port must be unique within the local domain, not just the local host. The name server only supports TCP/IP (either IPv4 or IPv6) sockets.

> **Note**:  Prior to OS X 10.2, [`NSSocketPortNameServer`](./nssocketportnameserver.md) was inoperable.

## Topics

### Getting the Server Object
- [+ sharedInstance](./nssocketportnameserver/sharedinstance.md)
  Returns the shared socket port name server.
### Looking up Ports
- [- portForName:](./nssocketportnameserver/portforname_.md)
  Looks up and returns the port registered under the specified name on the local host.
- [- portForName:host:](./nssocketportnameserver/portforname_host_.md)
  Looks up and returns the port registered under the specified name on a specified host.
- [- portForName:host:nameServerPortNumber:](./nssocketportnameserver/portforname_host_nameserverportnumber_.md)
  Looks up and returns the port registered under the specified name on a specified host.
### Registering and Removing Ports
- [- registerPort:name:](./nssocketportnameserver/registerport_name_.md)
  Registers a given port as a network service with the specified name in the local domain.
- [- registerPort:name:nameServerPortNumber:](./nssocketportnameserver/registerport_name_nameserverportnumber_.md)
  Registers a given port as a network service with the specified name in the local domain.
- [- removePortForName:](./nssocketportnameserver/removeportforname_.md)
  Unregisters the port for a given name on the local host.
### Configuring the Default Port Number
- [defaultNameServerPortNumber](./nssocketportnameserver/defaultnameserverportnumber.md)
  Returns the port number used to contact the name server.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssocketportnameserver)*