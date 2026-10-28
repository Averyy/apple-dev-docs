# targetVolume

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The target volume (in ㎥) that the body tries to match.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var targetVolume: Float? { get set }
```

## Discussion

Must be positive when non-`nil`. When `nil`, the volume of the body’s [`mesh`](../mesh.md) is used.

## See Also

### Configuring inflation
- [var stiffness: Float](./stiffness.md)
  The resistance of the body’s volume to diverge from `targetVolume`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/inflationconstraint-swift.struct/targetvolume)*