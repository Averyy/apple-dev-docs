# MTLLogStateDescriptor

**Framework**: Metal  
**Kind**: class

An interface that represents a log state configuration.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
class MTLLogStateDescriptor
```

## Mentions

- [Logging shader debug messages](logging-shader-debug-messages.md)

#### Overview

Configure the descriptor to create an [`MTLLogState`](mtllogstate.md) by calling [`makeLogState(descriptor:)`](mtldevice/makelogstate(descriptor:).md).

If you’ve set the environment variables `MTL_LOG_BUFFER_SIZE` or `MTL_LOG_LEVEL`, then the system automatically enables logging. If any command buffer or command queue has an attached log state, then the system uses the log state’s settings instead of the environment variable values.

## Topics

### Instance Properties
- [var bufferSize: Int](mtllogstatedescriptor/buffersize.md)
  The size of the internal buffer the log state uses, specified in bytes.
- [var level: MTLLogLevel](mtllogstatedescriptor/level.md)
  The minimum level of messages that the shader can log.
### Log Levels
- [enum MTLLogLevel](mtlloglevel.md)
  The supported log levels for shader logging.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MTLLogState](mtllogstate.md)
  A container for shader log messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllogstatedescriptor)*