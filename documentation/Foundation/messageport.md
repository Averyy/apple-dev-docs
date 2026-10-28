# MessagePort

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A port that can be used as an endpoint for distributed object connections (or raw messaging).

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class MessagePort
```

```objc
@interface NSMessagePort : NSPort
```

## Overview

[`MessagePort`](./messageport.md) is a subclass of [`Port`](./port.md) that allows for local (on the same machine) communication only. A companion class, [`SocketPort`](./socketport.md), allows for both local and remote communication, but may be more expensive than [`MessagePort`](./messageport.md) for the local case.

[`MessagePort`](./messageport.md) defines no additional methods over those already defined by [`Port`](./port.md).

> **Note**:  [`MessagePort`](./messageport.md) conforms to the [`NSCoding`](./nscoding.md) protocol, but only supports coding by an [`NSPortCoder`](./nsportcoder.md) object. [`Port`](./port.md) and its subclasses do not support archiving.

> ❗ **Important**:  Avoid [`MessagePort`](./messageport.md). There’s little reason to use [`MessagePort`](./messageport.md) rather than [`NSMachPort`](./nsmachport.md) or [`SocketPort`](./socketport.md). There’s no particular performance or functionality advantage. It is recommended avoiding its use.
>
> [`MessagePort`](./messageport.md) may be deprecated in the macOS 10.6 or later.

## Relationships

### Inherits From
- [Port](./port.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSCopying](./nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Related Documentation
- [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)
### Legacy
- [protocol NSMachPortDelegate](./nsmachportdelegate.md)
  An interface for handling incoming Mach messages.
- [class NSMachPort](./nsmachport.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/messageport)*