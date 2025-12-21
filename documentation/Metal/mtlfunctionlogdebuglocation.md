# MTLFunctionLogDebugLocation

**Framework**: Metal  
**Kind**: protocol

The source code that logged a debug message.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
protocol MTLFunctionLogDebugLocation : NSObjectProtocol
```

## Topics

### Inspecting the location details
- [var functionName: String?](mtlfunctionlogdebuglocation/functionname.md)
  The name of the shader function.
- [var url: URL?](mtlfunctionlogdebuglocation/url.md)
  The URL of the file that contains the shader function.
- [var line: Int](mtlfunctionlogdebuglocation/line.md)
  The line that the log message appears on.
- [var column: Int](mtlfunctionlogdebuglocation/column.md)
  The column where the log message appears.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var debugLocation: (any MTLFunctionLogDebugLocation)?](mtlfunctionlog/debuglocation.md)
  If known, the location of the logging command within a shader source file.
- [var encoderLabel: String?](mtlfunctionlog/encoderlabel.md)
  The label for the encoder that logged the message.
- [var function: (any MTLFunction)?](mtlfunctionlog/function.md)
  When known, the function object corresponding to the logged message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionlogdebuglocation)*