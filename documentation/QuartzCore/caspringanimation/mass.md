# mass

**Framework**: Core Animation  
**Kind**: property

The mass of the object attached to the end of the spring.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var mass: CGFloat { get set }
```

#### Discussion

The default mass is `1`. Increasing this value will increase the spring effect: the attached object will be subject to more oscillations and greater overshoot, resulting in an increased [`settlingDuration`](caspringanimation/settlingduration.md). Decreasing the mass will reduce the spring effect: there will be fewer oscillations and a reduced overshoot, resulting in a decreased [`settlingDuration`](caspringanimation/settlingduration.md).

## See Also

- [var damping: CGFloat](caspringanimation/damping.md)
  Defines how the spring’s motion should be damped due to the forces of friction.
- [var initialVelocity: CGFloat](caspringanimation/initialvelocity.md)
  The initial velocity of the object attached to the spring.
- [var settlingDuration: CFTimeInterval](caspringanimation/settlingduration.md)
  The estimated duration required for the spring system to be considered at rest.
- [var stiffness: CGFloat](caspringanimation/stiffness.md)
  The spring stiffness coefficient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caspringanimation/mass)*