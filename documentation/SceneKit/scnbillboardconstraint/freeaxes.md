# freeAxes

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

An option that specifies which degrees of freedom the constraint affects.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var freeAxes: SCNBillboardAxis { get set }
```

```objc
@property (nonatomic) SCNBillboardAxis freeAxes;
```

#### Discussion

With the default constraint type of [`all`](../scnbillboardaxis/all.md), a node affected by the constraint never rotates with respect to the scene’s point of view. Change this property to partially constrain a node’s orientation. For example, the [`Y`](../scnbillboardaxis/y.md) constraint type keeps only the node’s y-axis parallel to the screen—this option can be useful for applications like drawing trees in the distance with 2D sprites instead of with 3D geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnbillboardconstraint/freeaxes)*