# kineticFriction

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The friction a cloth body particle experiences when in contact with another particle or collider with relative motion.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var kineticFriction: Float { get set }
```

#### Discussion

Must be non-negative; negative values are clamped to zero. The default value is `0.7`, which gives preference to the colliders’ kinetic friction.

## See Also

### Configuring friction
- [var staticFriction: Float](./staticfriction.md)
  The friction a cloth body particle experiences when in contact with another particle or collider with no relative motion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodymaterial/kineticfriction)*