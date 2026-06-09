# staticFriction

**Framework**: RealityKit  
**Kind**: property

The friction the collider applies to contacting cloth body particles with no relative motion.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var staticFriction: Float { get set }
```

#### Discussion

Must be non-negative; negative values are clamped to zero. The default value is `0.8`.

## See Also

- [var kineticFriction: Float](clothcollidermaterial/kineticfriction.md)
  The friction the collider applies to contacting cloth body particles with relative motion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothcollidermaterial/staticfriction)*