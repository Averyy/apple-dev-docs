# makeMeshInstance(meshPart:pipeline:geometryArguments:surfaceArguments:lightingArguments:transform:sortCategory:)

**Framework**: RealityKit  
**Kind**: method

Creates a drawable mesh instance pairing a mesh part with a compiled pipeline state and optional per-draw argument tables.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func makeMeshInstance(meshPart: LowLevelMeshPart, pipeline: LowLevelRenderPipelineState, geometryArguments: LowLevelArgumentTable?, surfaceArguments: LowLevelArgumentTable?, lightingArguments: LowLevelArgumentTable?, transform: simd_float4x4, sortCategory: LowLevelMeshInstance.SortCategory) throws -> LowLevelMeshInstance
```

#### Return Value

A newly created [`LowLevelMeshInstance`](lowlevelmeshinstance.md).

#### Discussion

Pass `nil` for any argument table stage not required by the material.

> **Note**: An error if the pipeline or argument tables are incompatible with the render context.

## Parameters

- `meshPart`: The mesh part this instance draws.
- `pipeline`: The compiled pipeline state used to render this instance.
- `geometryArguments`: The argument table bound to the geometry modifier stage, or `nil` if none.
- `surfaceArguments`: The argument table bound to the surface shader stage, or `nil` if none.
- `lightingArguments`: The argument table bound to the lighting function stage, or `nil` if none.
- `transform`: The initial local-to-world transform of this instance.
- `sortCategory`: The category (opaque or transparent) for sorting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone/makemeshinstance(meshpart:pipeline:geometryarguments:surfacearguments:lightingarguments:transform:sortcategory:))*