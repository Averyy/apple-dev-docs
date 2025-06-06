# MTLTessellationFactorStepFunction.constant

**Framework**: Metal  
**Kind**: case

A constant step function. For all instances, the tessellation factor for all patches in a patch draw call is at the `offset` location in the tessellation factor buffer.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case constant
```

## See Also

- [MTLTessellationFactorStepFunction.perPatch](mtltessellationfactorstepfunction/perpatch.md)
  A per-patch step function. For all instances, the tessellation factor for all patches in a patch draw call is at the `offset + (drawPatchIndex * tessellationFactorStride)` location in the tessellation factor buffer.
- [MTLTessellationFactorStepFunction.perInstance](mtltessellationfactorstepfunction/perinstance.md)
  A per-instance step function. For a given instance ID, the tessellation factor for a patch in a patch draw call is at the `offset + (instanceID * instanceStride)` location in the tessellation factor buffer.
- [MTLTessellationFactorStepFunction.perPatchAndPerInstance](mtltessellationfactorstepfunction/perpatchandperinstance.md)
  A per-patch and per-instance step function. For a given instance ID, the tessellation factor for a patch in a patch draw call is at the `offset + (drawPatchIndex * tessellationFactorStride + instanceID * instanceStride)` location in the tessellation factor buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltessellationfactorstepfunction/constant)*