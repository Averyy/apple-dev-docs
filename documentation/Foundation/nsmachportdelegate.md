# NSMachPortDelegate

**Framework**: Foundation  
**Kind**: protocol  
**Role**: Protocol

An interface for handling incoming Mach messages.

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
protocol NSMachPortDelegate : PortDelegate
```

```objc
@protocol NSMachPortDelegate <NSPortDelegate>
```

#### Overview

Delegates of [`NSMachPort`](./nsmachport.md) objects optionally adopt this protocol.

## Topics

### Handling Mach messages
- [func handleMachMessage(UnsafeMutableRawPointer)](./nsmachportdelegate/handlemachmessage%28_%29.md)
  Process an incoming Mach message.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [PortDelegate](./portdelegate.md)

## See Also

### Legacy
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmachportdelegate)*