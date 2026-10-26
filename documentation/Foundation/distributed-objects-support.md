# Distributed Objects Support

**Framework**: Foundation  
**Role**: API Collection

Enable communication among objects in different processes, both locally and on remote systems.

## Topics

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
- [class NSProtocolChecker](./nsprotocolchecker.md)
  An object that restricts the messages that can be sent to another object (referred to as the checker’s delegate).
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

## See Also

### Legacy
- [Objective-C Garbage Collection](./objective-c-garbage-collection.md)
  Interface with the legacy garbage collection system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/distributed-objects-support)*