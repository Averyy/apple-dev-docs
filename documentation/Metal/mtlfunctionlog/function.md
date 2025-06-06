# function

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

When known, the function object corresponding to the logged message.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var function: (any MTLFunction)? { get }
```

## See Also

- [var debugLocation: (any MTLFunctionLogDebugLocation)?](mtlfunctionlog/debuglocation.md)
  If known, the location of the logging command within a shader source file.
- [var encoderLabel: String?](mtlfunctionlog/encoderlabel.md)
  The label for the encoder that logged the message.
- [protocol MTLFunctionLogDebugLocation](mtlfunctionlogdebuglocation.md)
  The source code that logged a debug message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionlog/function)*