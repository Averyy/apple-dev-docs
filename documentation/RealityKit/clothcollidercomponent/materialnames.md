# materialNames

**Framework**: RealityKit  
**Kind**: property

The names of the collider materials used by this collider.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var materialNames: [String]
```

#### Discussion

The default material is used if no matching material name is present in [`ClothSimulationComponent`](clothsimulationcomponent.md).

The material of the collider determines various physical properties of the collider, such as friction.

Note, only the first material name is used.

## See Also

- [var shape: ClothColliderShape](clothcollidercomponent/shape.md)
  The (simulation) shape of the collider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothcollidercomponent/materialnames)*