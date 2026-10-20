# debugLocation

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

If known, the location of the logging command within a shader source file.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var debugLocation: (any MTLFunctionLogDebugLocation)? { get }
```

```objc
@property (nonatomic, readonly, nullable) id<MTLFunctionLogDebugLocation> debugLocation;
```

## See Also

### Getting execution details
- [var encoderLabel: String?](./encoderlabel.md)
  The label for the encoder that logged the message.
- [var function: (any MTLFunction)?](./function.md)
  When known, the function object corresponding to the logged message.
- [protocol MTLFunctionLogDebugLocation](../mtlfunctionlogdebuglocation.md)
  The source code that logged a debug message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionlog/debuglocation)*