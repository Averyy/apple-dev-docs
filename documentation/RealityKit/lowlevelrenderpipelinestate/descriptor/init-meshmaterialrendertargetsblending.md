# init(mesh:material:renderTargets:blending:)

**Framework**: RealityKit  
**Kind**: init

Creates a descriptor for the given mesh format, material, render targets, and optional blending configuration.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(mesh: LowLevelMeshResource.Descriptor, material: LowLevelMaterialResource, renderTargets: LowLevelRenderTarget.DescriptorSet, blending: LowLevelRenderPipelineState.Descriptor.Blending? = nil)
```

## Parameters

- `mesh`: The vertex format descriptor of the mesh to be rendered.
- `material`: The compiled material (geometry modifier, surface shader, and lighting function).
- `renderTargets`: The render target descriptors this pipeline state must be compatible with.
- `blending`: The blending configuration for transparent draws, or `nil` for opaque draws. Defaults to `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderpipelinestate/descriptor/init(mesh:material:rendertargets:blending:))*