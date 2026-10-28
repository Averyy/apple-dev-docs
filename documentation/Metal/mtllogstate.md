# MTLLogState

**Framework**: Metal  
**Kind**: protocol  
**Role**: Protocol

A container for shader log messages.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
protocol MTLLogState : NSObjectProtocol, Sendable
```

```objc
@protocol MTLLogState <NSObject>
```

## Mentions

- [Logging shader debug messages](./logging-shader-debug-messages.md)

## Overview

Create an [`MTLCommandQueue`](./mtlcommandqueue.md) or [`MTLCommandBuffer`](./mtlcommandbuffer.md) with a log state to hold messages logged from shaders. Attach a log state to a command buffer by assigning it to the command buffer descriptor’s [`logState`](./mtlcommandbufferdescriptor/logstate.md). Similarly, to attach a log state to a command queue, use the command queue descriptor’s [`logState`](./mtlcommandqueuedescriptor/logstate.md).

When you attach a log state to a command queue, the command queue shares the log state with all the command buffers it creates. If you attach different log states to a command buffer and command queue, then the system uses the state attached to the command buffer.

Because logging incurs an overhead, regardless of whether the system prints messages, you need to explicitly enable logging with [`enableLogging`](./mtlcompileoptions/enablelogging.md).

## Topics

### Instance Methods
- [func addLogHandler((String?, String?, MTLLogLevel, String) -> Void)](./mtllogstate/addloghandler%28_%29.md)
  Adds a log handler to customize the presentation of shader logging.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Shader logging
- [class MTLLogStateDescriptor](./mtllogstatedescriptor.md)
  An interface that represents a log state configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllogstate)*