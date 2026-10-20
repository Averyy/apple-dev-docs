# PortDelegate

**Framework**: Foundation  
**Kind**: protocol  
**Role**: Protocol

An interface for handling incoming messages.

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
protocol PortDelegate : NSObjectProtocol
```

```objc
@protocol NSPortDelegate <NSObject>
```

#### Overview

The [`PortDelegate`](./portdelegate.md) protocol defines the optional methods implemented by delegates of [`Port`](./port.md) objects.

## Topics

### Handling Port Messages
- [func handle(NSPortMessage)](./portdelegate/handle%28_%29.md)
  Processes a given incoming message on the port.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [NSMachPortDelegate](./nsmachportdelegate.md)

## See Also

### Legacy
- [protocol NSMachPortDelegate](./nsmachportdelegate.md)
  An interface for handling incoming Mach messages.
- [class NSMachPort](./nsmachport.md)
  A port that can be used as an endpoint for distributed object connections (or raw messaging).
- [class MessagePort](./messageport.md)
  A port that can be used as an endpoint for distributed object connections (or raw messaging).
- [class PortMessage](./portmessage.md)
  A low-level, operating system-independent type for inter-application (and inter-thread) messages.
- [class NSProtocolChecker](./nsprotocolchecker.md)
  An object that restricts the messages that can be sent to another object (referred to as the checker’s delegate).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/portdelegate)*