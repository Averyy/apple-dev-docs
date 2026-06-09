# count

**Framework**: RealityKit  
**Kind**: property

The number of instance slots in this array.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final var count: Int { get }
```

#### Discussion

Represents the total capacity allocated at creation time; some slots may be unoccupied. Use `setMeshInstance(_:index:)` to populate slots and the `subscript` to check occupancy.

## See Also

- [func setMeshInstance(LowLevelMeshInstanceArray.Element, index: Int) throws(LowLevelRenderContextError)](lowlevelmeshinstancearray/setmeshinstance(_:index:).md)
  Assigns a mesh instance to the slot at the given index, or clears the slot if the instance is nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshinstancearray/count)*