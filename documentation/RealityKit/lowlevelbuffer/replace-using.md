# replace(using:)

**Framework**: RealityKit  
**Kind**: method

Retrieve an MTLBuffer that can be used to replace the contents of the buffer on GPU using Metal.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func replace(using commandBuffer: any MTLCommandBuffer) -> any MTLBuffer
```

#### Discussion

The buffer’s contents are in an uninitialized state.

The caller supplies the MTLCommandBuffer that they intend to use for buffer modifications. RealityKit will wait for the MTLCommandBuffer to complete before utilizing the buffer for rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelbuffer/replace(using:))*