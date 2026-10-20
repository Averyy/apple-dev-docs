# kineticFriction

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The kinetic friction to use between the material pair.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var kineticFriction: Float { get set }
```

#### Discussion

Must be non-negative; negative values are clamped to zero.

## See Also

### Accessing friction values
- [var staticFriction: Float](./staticfriction.md)
  The static friction to use between the material pair.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/frictionoverridescollection/value/kineticfriction)*