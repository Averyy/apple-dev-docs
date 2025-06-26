# replace(using:)

**Framework**: RealityKit  
**Kind**: method

Retrieve an MTLBuffer that can be used to replace the per instance transform data on GPU using Metal.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final func replace(using commandBuffer: any MTLCommandBuffer) -> any MTLBuffer
```

#### Discussion

The transform buffer’s contents are in an uninitialized state.

The caller supplies the MTLCommandBuffer that they intend to use for transform buffer modifications. RealityKit will wait for the MTLCommandBuffer to complete before utilizing the transform buffer for rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelinstancedata/replace(using:))*