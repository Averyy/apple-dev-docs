# NSConnectionDelegate

**Framework**: Foundation  
**Kind**: protocol  
**Role**: Protocol

An interface for interacting with low-level, interprocess connections.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Use [`NSXPCConnection`](./nsxpcconnection.md) instead.

## Declaration

```objc
@protocol NSConnectionDelegate <NSObject>
```

## Overview

The [`NSConnectionDelegate`](./nsconnectiondelegate.md) protocol defines the optional methods implemented by delegates of [`NSConnection`](./nsconnection.md) objects.

## Topics

### Authenticating
- [- authenticateComponents:withData:](./nsconnectiondelegate/authenticatecomponents_withdata_.md)
  Returns a Boolean value that indicates whether given authentication data is valid for a given set of components.
- [- authenticationDataForComponents:](./nsconnectiondelegate/authenticationdataforcomponents_.md)
  Returns an `NSData` object to be used as an authentication stamp for an outgoing message.
### Responding to a Connection
- [- connection:shouldMakeNewConnection:](./nsconnectiondelegate/connection_shouldmakenewconnection_.md)
  Returns a Boolean value that indicates whether the parent connection should allow a given new connection to be created.
- [- connection:handleRequest:](./nsconnectiondelegate/connection_handlerequest_.md)
  This method should be implemented by `NSConnection` object delegates that want to intercept distant object requests.
- [- createConversationForConnection:](./nsconnectiondelegate/createconversationforconnection_.md)
  Returns an arbitrary object identifying a new conversation being created for the connection in the current thread.
- [- makeNewConnection:sender:](./nsconnectiondelegate/makenewconnection_sender_.md)
  Returns a Boolean value that indicates whether the parent should allow a given new connection to be created and configured.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Legacy
- [protocol NSMachPortDelegate](./nsmachportdelegate.md)
  An interface for handling incoming Mach messages.
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
- [NSSocketPortNameServer](./nssocketportnameserver.md)
  A port name server that takes and returns socket ports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconnectiondelegate)*