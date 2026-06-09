# reset(encoder:)

**Framework**: ComputeGraph  
**Kind**: method

Resets the simulation to its initial state, clearing all live elements and accumulated time.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
final func reset(encoder: any MTLComputeCommandEncoder)
```

#### Discussion

The reset is encoded as a compute dispatch into `encoder`. You must commit the enclosing command buffer for the reset to take effect on the GPU.

## Parameters

- `encoder`: The compute command encoder to encode the reset operation with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computegraphsimulation/reset(encoder:))*