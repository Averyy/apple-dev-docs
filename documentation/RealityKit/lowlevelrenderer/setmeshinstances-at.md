# setMeshInstances(_:at:)

**Framework**: RealityKit  
**Kind**: method

Assigns a mesh instance array to the given slot index.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func setMeshInstances(_ meshInstances: LowLevelMeshInstanceArray?, at index: Int) throws(LowLevelRendererError)
```

#### Discussion

> **Note**: [`LowLevelRendererError`](lowlevelrenderererror.md) if the renderer’s render target descriptor is not contained in the array’s descriptor set.

## Parameters

- `meshInstances`: The mesh instance array to assign, or `nil` to clear the slot.
- `index`: The zero-based slot index to assign to. Must be within `0..<meshInstancesArrayCount`.

## See Also

- [func meshInstances(at: Int) -> LowLevelMeshInstanceArray?](lowlevelrenderer/meshinstances(at:).md)
  Returns the mesh instance array at the given slot index, or the empty value if the slot is unoccupied.
- [var meshInstancesArrayCount: Int](lowlevelrenderer/meshinstancesarraycount.md)
  The number of mesh instance array slots.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/setmeshinstances(_:at:))*