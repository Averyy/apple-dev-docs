# damping

**Framework**: Core Animation  
**Kind**: property

Defines how the spring’s motion should be damped due to the forces of friction.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var damping: CGFloat { get set }
```

#### Discussion

The default value of the [`damping`](caspringanimation/damping.md) property is `10`. Reducing this value reduces the energy loss with each oscillation: the animated value will overshoot the [`toValue`](cabasicanimation/tovalue.md) and the [`settlingDuration`](caspringanimation/settlingduration.md) may be greater than the [`duration`](camediatiming/duration.md). Increasing the value increases the energy loss with each duration: there will be fewer and smaller oscillations and the [`settlingDuration`](caspringanimation/settlingduration.md) may be smaller than the duration.

## See Also

- [var initialVelocity: CGFloat](caspringanimation/initialvelocity.md)
  The initial velocity of the object attached to the spring.
- [var mass: CGFloat](caspringanimation/mass.md)
  The mass of the object attached to the end of the spring.
- [var settlingDuration: CFTimeInterval](caspringanimation/settlingduration.md)
  The estimated duration required for the spring system to be considered at rest.
- [var stiffness: CGFloat](caspringanimation/stiffness.md)
  The spring stiffness coefficient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caspringanimation/damping)*