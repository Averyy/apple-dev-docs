# function

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
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

```objc
@property (nonatomic, readonly, nullable) id<MTLFunction> function;
```

## See Also

### Getting execution details
- [var debugLocation: (any MTLFunctionLogDebugLocation)?](./debuglocation.md)
  If known, the location of the logging command within a shader source file.
- [var encoderLabel: String?](./encoderlabel.md)
  The label for the encoder that logged the message.
- [protocol MTLFunctionLogDebugLocation](../mtlfunctionlogdebuglocation.md)
  The source code that logged a debug message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionlog/function)*