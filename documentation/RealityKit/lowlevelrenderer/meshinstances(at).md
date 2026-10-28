# meshInstances(at:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Returns the mesh instance array at the given slot index, or `nil` if the slot is unoccupied.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final func meshInstances(at index: Int) -> LowLevelMeshInstanceArray?
```

## Return Value

The [`LowLevelMeshInstanceArray`](../lowlevelmeshinstancearray.md) at `index`, or `nil` if the slot is unoccupied.

## Parameters

- `index`: The zero-based slot index to retrieve.

## See Also

### Managing mesh instances
- [func setMeshInstances(LowLevelMeshInstanceArray?, at: Int) throws(LowLevelRendererError)](./setmeshinstances%28_,at%29.md)
  Assigns a mesh instance array to the given slot index.
- [var meshInstancesArrayCount: Int](./meshinstancesarraycount.md)
  The number of mesh instance array slots.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/meshinstances(at:))*