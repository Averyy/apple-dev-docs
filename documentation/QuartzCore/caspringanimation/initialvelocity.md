# initialVelocity

**Framework**: Core Animation  
**Kind**: property

The initial velocity of the object attached to the spring.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var initialVelocity: CGFloat { get set }
```

#### Discussion

Defaults to `0`, which represents an unmoving object. Negative values represent the object moving away from the spring attachment point, positive values represent the object moving towards the spring attachment point.

## See Also

- [var damping: CGFloat](caspringanimation/damping.md)
  Defines how the spring’s motion should be damped due to the forces of friction.
- [var mass: CGFloat](caspringanimation/mass.md)
  The mass of the object attached to the end of the spring.
- [var settlingDuration: CFTimeInterval](caspringanimation/settlingduration.md)
  The estimated duration required for the spring system to be considered at rest.
- [var stiffness: CGFloat](caspringanimation/stiffness.md)
  The spring stiffness coefficient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caspringanimation/initialvelocity)*