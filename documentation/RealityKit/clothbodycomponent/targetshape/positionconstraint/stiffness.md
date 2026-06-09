# stiffness

**Framework**: RealityKit  
**Kind**: property

The stiffness by which the particle is pulled towards the position.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var stiffness: Float { get set }
```

#### Discussion

In the context of a target shape, this gets multiplied by the weight of the target shape. A stiffness of 0 will effectively inactivate the position constraint.

The valid range is [0.0, 1.0], both included. Values outside the valid range are clamped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/targetshape/positionconstraint/stiffness)*