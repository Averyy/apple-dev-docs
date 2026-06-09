# kineticFriction

**Framework**: RealityKit  
**Kind**: property

The friction the collider applies to contacting cloth body particles with relative motion.

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

Must be non-negative; negative values are clamped to zero. The default value is `0.7`.

## See Also

- [var staticFriction: Float](clothcollidermaterial/staticfriction.md)
  The friction the collider applies to contacting cloth body particles with no relative motion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothcollidermaterial/kineticfriction)*