# memoryBarrier(scope:after:before:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a memory barrier that enforces the order of write and read operations for specific resource types.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func memoryBarrier(scope: MTLBarrierScope, after: MTLRenderStages, before: MTLRenderStages)
```

#### Discussion

Memory barriers ensure the relevant stages of prior draw commands finish updating resources before starting the stages of subsequent commands that depend on those resources.

To determine whether a GPU supports memory barriers, see the [`Metal feature set tables (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf).

## Parameters

- `scope`: An   instance that represents the resource types the barrier synchronizes operations on.
- `after`: The render stages of previous draw commands that modify resources of the types that   defines.
- `before`: The render stages of subsequent draw commands that read or modify resources of the types that   defines.

## See Also

- [func waitForFence(any MTLFence, before: MTLRenderStages)](mtlrendercommandencoder/waitforfence(_:before:).md)
  Encodes a command that instructs the GPU to pause before starting one or more stages of the render pass until a pass updates a fence.
- [func updateFence(any MTLFence, after: MTLRenderStages)](mtlrendercommandencoder/updatefence(_:after:).md)
  Encodes a command that instructs the GPU to update a fence after one or more stages, which signals passes waiting on the fence.
- [func memoryBarrier(resources: [any MTLResource], after: MTLRenderStages, before: MTLRenderStages)](mtlrendercommandencoder/memorybarrier(resources:after:before:).md)
  Creates a memory barrier that enforces the order of write and read operations for specific resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/memorybarrier(scope:after:before:))*