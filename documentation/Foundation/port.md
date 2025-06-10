# Port

**Framework**: Foundation  
**Kind**: class

An abstract class that represents a communication channel.

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
class Port
```

#### Overview

Communication occurs between [`Port`](port.md) objects, which typically reside in different threads or tasks. The distributed objects system uses [`Port`](port.md) objects to send [`PortMessage`](portmessage.md) objects back and forth. Implement interapplication communication using distributed objects whenever possible and use [`Port`](port.md) objects only when necessary.

To receive incoming messages, add [`Port`](port.md) objects to an instance of [`RunLoop`](runloop.md) as input sources. [`NSConnection`](nsconnection.md) objects automatically add their receive port when initialized.

When the [`Port`](port.md) object receives a port message, it forwards the message to its delegate in a [`handleMachMessage(_:)`](nsmachportdelegate/handlemachmessage(_:).md) or [`handle(_:)`](portdelegate/handle(_:).md) message. The delegate should implement only one of these methods to process the incoming message in whatever form desired. [`handleMachMessage(_:)`](nsmachportdelegate/handlemachmessage(_:).md) provides a message as a raw Mach message beginning with a `msg_header_t` structure. [`handle(_:)`](portdelegate/handle(_:).md) provides a message as an instance of [`PortMessage`](portmessage.md), which is an object-oriented wrapper for a Mach message. If a delegate has not been set, the `NSPort` object handles the message itself.

When you are finished using a port object, you must explicitly invalidate the port object prior to sending it a `release` message. Similarly, if your application uses garbage collection, you must invalidate the port object before removing any strong references to it. If you do not invalidate the port, the resulting port object may linger and create a memory leak. To invalidate the port object, invoke its [`invalidate()`](port/invalidate().md) method.

Foundation defines three concrete subclasses of `NSPort`. [`NSMachPort`](nsmachport.md) and [`MessagePort`](messageport.md) allow local (on the same machine) communication only. [`SocketPort`](socketport.md) allows for both local and remote communication, but may be more expensive than the others for the local case. When creating an `NSPort` object, using doc:nsport/1807189-allocwithzone or [`port`](nsport/port.md), an [`NSMachPort`](nsmachport.md) object is created instead.

For backward compatibility on Mach, `- [NSPort allocWithZone:]` returns an instance of the [`NSMachPort`](nsmachport.md) class when sent to this class. Otherwise, it returns an instance of a concrete subclass that can be used for messaging between threads or processes on the local machine, or, in the case of [`SocketPort`](socketport.md), between processes on separate machines.

> ❗ **Important**:  [`Port`](port.md) conforms to the [`NSCoding`](nscoding.md) protocol, but only supports coding by an [`NSPortCoder`](nsportcoder.md). [`Port`](port.md) and its subclasses do not support archiving.

## Topics

### Validation
- [func invalidate()](port/invalidate.md)
  Marks the receiver as invalid and posts an [`didBecomeInvalidNotification`](port/didbecomeinvalidnotification.md) to the default notification center.
- [var isValid: Bool](port/isvalid.md)
  A Boolean value that indicates whether the receiver is valid.
### Setting the Delegate
- [func setDelegate((any PortDelegate)?)](port/setdelegate(_:).md)
  Sets the receiver’s delegate to a given object.
- [func delegate() -> (any PortDelegate)?](port/delegate.md)
  Returns the receiver’s delegate.
### Setting Information
- [func send(before: Date, components: NSMutableArray?, from: Port?, reserved: Int) -> Bool](port/send(before:components:from:reserved:).md)
  This method is provided for subclasses that have custom types of `NSPort`.
- [func send(before: Date, msgid: Int, components: NSMutableArray?, from: Port?, reserved: Int) -> Bool](port/send(before:msgid:components:from:reserved:).md)
  This method is provided for subclasses that have custom types of `NSPort`.
- [var reservedSpaceLength: Int](port/reservedspacelength.md)
  The number of bytes of space reserved by the receiver for sending data.
### Port Monitoring
- [func remove(from: RunLoop, forMode: RunLoop.Mode)](port/remove(from:formode:).md)
  This method should be implemented by a subclass to stop monitoring of a port when removed from a give run loop in a given input mode.
- [func schedule(in: RunLoop, forMode: RunLoop.Mode)](port/schedule(in:formode:).md)
  This method should be implemented by a subclass to set up monitoring of a port when added to a given run loop in a given input mode.
### Notifications
- [class let didBecomeInvalidNotification: NSNotification.Name](port/didbecomeinvalidnotification.md)
  Posted from the [`invalidate()`](port/invalidate().md) method, which is invoked when the `NSPort` is deallocated or when it notices that its communication channel has been damaged. The notification object is the `NSPort` object that has become invalid. This notification does not contain a `userInfo` dictionary.
### Data Types
- [typealias SocketNativeHandle](socketnativehandle.md)
  Type for the platform-specific native socket handle.
### Structures
- [struct DidBecomeInvalidMessage](port/didbecomeinvalidmessage.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [MessagePort](messageport.md)
- [NSMachPort](nsmachport.md)
- [SocketPort](socketport.md)
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

- [class Host](host.md)
  A representation of an individual host on the network.
- [class SocketPort](socketport.md)
  A port that represents a BSD socket.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/port)*