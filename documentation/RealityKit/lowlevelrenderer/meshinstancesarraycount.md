# meshInstancesArrayCount

**Framework**: RealityKit  
**Kind**: property

The number of mesh instance array slots.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final var meshInstancesArrayCount: Int { get set }
```

#### Discussion

Increase this value before calling `setMeshInstances(_:at:)` to assign arrays to slots. Setting this to a smaller value removes trailing slots.

## See Also

- [func meshInstances(at: Int) -> LowLevelMeshInstanceArray?](lowlevelrenderer/meshinstances(at:).md)
  Returns the mesh instance array at the given slot index, or the empty value if the slot is unoccupied.
- [func setMeshInstances(LowLevelMeshInstanceArray?, at: Int) throws(LowLevelRendererError)](lowlevelrenderer/setmeshinstances(_:at:).md)
  Assigns a mesh instance array to the given slot index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/meshinstancesarraycount)*