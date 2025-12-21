# MTLFunctionLog

**Framework**: Metal  
**Kind**: protocol

A log entry a Metal device generates when the it runs a command buffer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
protocol MTLFunctionLog : NSObjectProtocol
```

## Topics

### Getting the log messsage
- [var type: MTLFunctionLogType](mtlfunctionlog/type.md)
  The type of message that was logged.
- [enum MTLFunctionLogType](mtlfunctionlogtype.md)
  Options for different kinds of function logs.
### Getting execution details
- [var debugLocation: (any MTLFunctionLogDebugLocation)?](mtlfunctionlog/debuglocation.md)
  If known, the location of the logging command within a shader source file.
- [var encoderLabel: String?](mtlfunctionlog/encoderlabel.md)
  The label for the encoder that logged the message.
- [var function: (any MTLFunction)?](mtlfunctionlog/function.md)
  When known, the function object corresponding to the logged message.
- [protocol MTLFunctionLogDebugLocation](mtlfunctionlogdebuglocation.md)
  The source code that logged a debug message.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [struct MTLLogContainer](mtllogcontainer-swift.struct.md)
  A collection of logged messages, created when a Metal device runs a command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionlog)*