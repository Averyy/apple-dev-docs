# makeMeshInstanceArray(renderTargets:count:)

**Framework**: RealityKit  
**Kind**: method

Creates a fixed-capacity ordered collection of mesh instances for the given render targets.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func makeMeshInstanceArray(renderTargets: LowLevelRenderTarget.DescriptorSet, count: Int) throws -> LowLevelMeshInstanceArray
```

#### Return Value

A newly created [`LowLevelMeshInstanceArray`](lowlevelmeshinstancearray.md).

#### Discussion

Pass the resulting array to [`setMeshInstances(_:at:)`](lowlevelrenderer/setmeshinstances(_:at:).md) to submit it for rendering.

> **Note**: An error if allocation fails.

## Parameters

- `renderTargets`: The set of render target descriptors this array must be compatible with.
- `count`: The maximum number of mesh instance slots to allocate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone/makemeshinstancearray(rendertargets:count:))*