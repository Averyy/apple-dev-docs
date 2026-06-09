# kineticFriction

**Framework**: RealityKit  
**Kind**: property

The friction a cloth body particle experiences when in contact with another particle or collider with relative motion.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var kineticFriction: Float { get set }
```

#### Discussion

Must be non-negative; negative values are clamped to zero. The default value is `0.7`, which gives preference to the colliders’ kinetic friction.

## See Also

- [var staticFriction: Float](clothbodymaterial/staticfriction.md)
  The friction a cloth body particle experiences when in contact with another particle or collider with no relative motion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodymaterial/kineticfriction)*