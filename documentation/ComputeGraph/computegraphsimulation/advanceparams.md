# ComputeGraphSimulation.AdvanceParams

**Framework**: ComputeGraph  
**Kind**: struct

Parameters for advancing a compute graph simulation by one time step.

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
struct AdvanceParams
```

## Topics

### Initializers
- [init(deltaTime: Float, commandBuffer: any MTLCommandBuffer, computeEncoder: any MTLComputeCommandEncoder)](computegraphsimulation/advanceparams/init(deltatime:commandbuffer:computeencoder:).md)
  Creates advance parameters with the required Metal objects.
- [init(deltaTime: Float, commandBuffer: any MTLCommandBuffer, computeEncoder: any MTLComputeCommandEncoder, localToWorld: simd_float4x4, worldToLocal: simd_float4x4, viewPosition: SIMD3<Float>?, viewDirection: SIMD3<Float>?)](computegraphsimulation/advanceparams/init(deltatime:commandbuffer:computeencoder:localtoworld:worldtolocal:viewposition:viewdirection:).md)
### Instance Properties
- [var commandBuffer: any MTLCommandBuffer](computegraphsimulation/advanceparams/commandbuffer.md)
  The command buffer to encode simulation commands into.
- [var computeEncoder: any MTLComputeCommandEncoder](computegraphsimulation/advanceparams/computeencoder.md)
  The compute command encoder to encode simulation dispatches with.
- [var deltaTime: Float](computegraphsimulation/advanceparams/deltatime.md)
  The time interval, in seconds, to advance the simulation.
- [var localToWorld: simd_float4x4](computegraphsimulation/advanceparams/localtoworld.md)
  The transform from the system’s local space to world space.
- [var maxSteps: Int](computegraphsimulation/advanceparams/maxsteps.md)
  The maximum number of fixed-size steps per advance.
- [var viewDirection: SIMD3<Float>?](computegraphsimulation/advanceparams/viewdirection.md)
  The forward direction of the viewer in world space.
- [var viewPosition: SIMD3<Float>?](computegraphsimulation/advanceparams/viewposition.md)
  The position of the viewer in world space.
- [var worldToLocal: simd_float4x4](computegraphsimulation/advanceparams/worldtolocal.md)
  The transform from world space to the system’s local space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computegraphsimulation/advanceparams)*