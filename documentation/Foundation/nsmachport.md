# NSMachPort

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
class NSMachPort
```

```objc
@interface NSMachPort : NSPort
```

## Overview

[`NSMachPort`](./nsmachport.md) is a subclass of [`Port`](./port.md) that wraps a Mach port, the fundamental communication port in macOS. [`NSMachPort`](./nsmachport.md) allows for local (on the same machine) communication only. A companion class, [`SocketPort`](./socketport.md), allows for both local and remote distributed object communication, but may be more expensive than [`NSMachPort`](./nsmachport.md) for the local case.

To use [`NSMachPort`](./nsmachport.md) effectively, you should be familiar with Mach ports, port access rights, and Mach messages. See the Mach OS documentation for more information.

> **Note**:  [`NSMachPort`](./nsmachport.md) conforms to the [`NSCoding`](./nscoding.md) protocol, but only supports coding by an [`NSPortCoder`](./nsportcoder.md). [`Port`](./port.md) and its subclasses do not support archiving.

## Topics

### Creating and Initializing
- [class func port(withMachPort: UInt32) -> Port](./nsmachport/port%28withmachport%29.md)
  Creates and returns a port object configured with the given Mach port.
- [class func port(withMachPort: UInt32, options: NSMachPort.Options) -> Port](./nsmachport/port%28withmachport,options%29.md)
  Creates and returns a port object configured with the specified options and the given Mach port.
- [init(machPort: UInt32)](./nsmachport/init%28machport%29.md)
  Initializes a newly allocated `NSMachPort` object with a given Mach port.
- [init(machPort: UInt32, options: NSMachPort.Options)](./nsmachport/init%28machport,options%29.md)
  Initializes a newly allocated `NSMachPort` object with a given Mach port and the specified options.
### Getting the Mach Port
- [var machPort: UInt32](./nsmachport/machport.md)
  The Mach port used by the receiver, represented as an integer.
### Scheduling the Port on a Run Loop
- [func remove(from: RunLoop, forMode: RunLoop.Mode)](./nsmachport/remove%28from,formode%29.md)
  Removes the receiver from the run loop mode `mode` of `runLoop`.
- [func schedule(in: RunLoop, forMode: RunLoop.Mode)](./nsmachport/schedule%28in,formode%29.md)
  Schedules the receiver into the run loop mode `mode` of `runLoop`.
### Getting and Setting the Delegate
- [func delegate() -> (any NSMachPortDelegate)?](./nsmachport/delegate%28%29.md)
  Returns the receiver’s delegate.
- [func setDelegate((any NSMachPortDelegate)?)](./nsmachport/setdelegate%28_%29.md)
  Sets the receiver’s delegate to a given object.
### Constants
- [NSMachPort.Options](./nsmachport/options.md)
  Used to remove access rights to a mach port when the `NSMachPort` object is invalidated or destroyed.

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

### Legacy
- [protocol NSMachPortDelegate](./nsmachportdelegate.md)
  An interface for handling incoming Mach messages.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmachport)*