# NSMachPort

**Framework**: Foundation  
**Kind**: class

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

#### Overview

[`NSMachPort`](nsmachport.md) is a subclass of [`Port`](port.md) that wraps a Mach port, the fundamental communication port in macOS. [`NSMachPort`](nsmachport.md) allows for local (on the same machine) communication only. A companion class, [`SocketPort`](socketport.md), allows for both local and remote distributed object communication, but may be more expensive than [`NSMachPort`](nsmachport.md) for the local case.

To use [`NSMachPort`](nsmachport.md) effectively, you should be familiar with Mach ports, port access rights, and Mach messages. See the Mach OS documentation for more information.

> **Note**:  [`NSMachPort`](nsmachport.md) conforms to the [`NSCoding`](nscoding.md) protocol, but only supports coding by an [`NSPortCoder`](nsportcoder.md). [`Port`](port.md) and its subclasses do not support archiving.

## Topics

### Creating and Initializing
- [class func port(withMachPort: UInt32) -> Port](nsmachport/port(withmachport:).md)
  Creates and returns a port object configured with the given Mach port.
- [class func port(withMachPort: UInt32, options: NSMachPort.Options) -> Port](nsmachport/port(withmachport:options:).md)
  Creates and returns a port object configured with the specified options and the given Mach port.
- [init(machPort: UInt32)](nsmachport/init(machport:).md)
  Initializes a newly allocated `NSMachPort` object with a given Mach port.
- [init(machPort: UInt32, options: NSMachPort.Options)](nsmachport/init(machport:options:).md)
  Initializes a newly allocated `NSMachPort` object with a given Mach port and the specified options.
### Getting the Mach Port
- [var machPort: UInt32](nsmachport/machport.md)
  The Mach port used by the receiver, represented as an integer.
### Scheduling the Port on a Run Loop
- [func remove(from: RunLoop, forMode: RunLoop.Mode)](nsmachport/remove(from:formode:).md)
  Removes the receiver from the run loop mode `mode` of `runLoop`.
- [func schedule(in: RunLoop, forMode: RunLoop.Mode)](nsmachport/schedule(in:formode:).md)
  Schedules the receiver into the run loop mode `mode` of `runLoop`.
### Getting and Setting the Delegate
- [func delegate() -> (any NSMachPortDelegate)?](nsmachport/delegate.md)
  Returns the receiver’s delegate.
- [func setDelegate((any NSMachPortDelegate)?)](nsmachport/setdelegate(_:).md)
  Sets the receiver’s delegate to a given object.
### Constants
- [NSMachPort.Options](nsmachport/options.md)
  Used to remove access rights to a mach port when the `NSMachPort` object is invalidated or destroyed.

## Relationships

### Inherits From
- [Port](port.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol NSMachPortDelegate](nsmachportdelegate.md)
  An interface for handling incoming Mach messages.
- [class MessagePort](messageport.md)
  A port that can be used as an endpoint for distributed object connections (or raw messaging).
- [protocol PortDelegate](portdelegate.md)
  An interface for handling incoming messages.
- [class PortMessage](portmessage.md)
  A low-level, operating system-independent type for inter-application (and inter-thread) messages.
- [class NSProtocolChecker](nsprotocolchecker.md)
  An object that restricts the messages that can be sent to another object (referred to as the checker’s delegate).


---

*[View on Apple Developer](https://developer.apple.com/documentation/Foundation/nsmachport)*