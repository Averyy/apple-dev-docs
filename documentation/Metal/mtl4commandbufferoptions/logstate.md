# logState

**Framework**: Metal  
**Kind**: property

Contains information related to shader logging.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var logState: (any MTLLogState)? { get set }
```

#### Discussion

To enable shader logging, call [`beginCommandBuffer(allocator:options:)`](mtl4commandbuffer/begincommandbuffer(allocator:options:).md) with an instance of [`MTL4CommandBufferOptions`](mtl4commandbufferoptions.md) that contains a non-`nil` [`MTLLogState`](mtllogstate.md) instance in this property.

Shader functions log messages until the command buffer ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandbufferoptions/logstate)*