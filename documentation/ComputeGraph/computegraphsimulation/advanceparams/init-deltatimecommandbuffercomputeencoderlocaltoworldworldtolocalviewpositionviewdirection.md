# init(deltaTime:commandBuffer:computeEncoder:localToWorld:worldToLocal:viewPosition:viewDirection:)

**Framework**: Compute Graph  
**Kind**: init

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- Reality Composer Pro ?+

## Declaration

```swift
init(deltaTime: Float, commandBuffer: any MTLCommandBuffer, computeEncoder: any MTLComputeCommandEncoder, localToWorld: simd_float4x4, worldToLocal: simd_float4x4, viewPosition: SIMD3<Float>? = nil, viewDirection: SIMD3<Float>? = nil)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computegraphsimulation/advanceparams/init(deltatime:commandbuffer:computeencoder:localtoworld:worldtolocal:viewposition:viewdirection:))*