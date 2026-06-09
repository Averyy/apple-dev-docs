# targetVolume

**Framework**: RealityKit  
**Kind**: property

The target volume (in ㎥) that the body tries to match.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var targetVolume: Float? { get set }
```

#### Discussion

Must be positive when non-`nil`. When `nil`, the volume of the body’s [`mesh`](clothbodycomponent/mesh.md) is used.

## See Also

- [var stiffness: Float](clothbodycomponent/inflationconstraint-swift.struct/stiffness.md)
  The resistance of the body’s volume to diverge from `targetVolume`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/inflationconstraint-swift.struct/targetvolume)*