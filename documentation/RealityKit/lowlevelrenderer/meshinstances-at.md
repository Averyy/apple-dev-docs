# meshInstances(at:)

**Framework**: RealityKit  
**Kind**: method

Returns the mesh instance array at the given slot index, or the empty value if the slot is unoccupied.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func meshInstances(at index: Int) -> LowLevelMeshInstanceArray?
```

#### Return Value

The [`LowLevelMeshInstanceArray`](lowlevelmeshinstancearray.md) at `index`, or `nil` if the slot is unoccupied.

## Parameters

- `index`: The zero-based slot index to retrieve.

## See Also

- [func setMeshInstances(LowLevelMeshInstanceArray?, at: Int) throws(LowLevelRendererError)](lowlevelrenderer/setmeshinstances(_:at:).md)
  Assigns a mesh instance array to the given slot index.
- [var meshInstancesArrayCount: Int](lowlevelrenderer/meshinstancesarraycount.md)
  The number of mesh instance array slots.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/meshinstances(at:))*