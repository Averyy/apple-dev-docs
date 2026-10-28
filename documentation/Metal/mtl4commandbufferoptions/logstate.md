# logState

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

Contains information related to shader logging.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var logState: (any MTLLogState)? { get set }
```

```objc
@property (nonatomic, retain, readwrite, nullable) id<MTLLogState> logState;
```

## Discussion

To enable shader logging, call [`beginCommandBuffer(allocator:options:)`](../mtl4commandbuffer/begincommandbuffer%28allocator,options%29.md) with an instance of [`MTL4CommandBufferOptions`](../mtl4commandbufferoptions.md) that contains a non-`nil` [`MTLLogState`](../mtllogstate.md) instance in this property.

Shader functions log messages until the command buffer ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandbufferoptions/logstate)*