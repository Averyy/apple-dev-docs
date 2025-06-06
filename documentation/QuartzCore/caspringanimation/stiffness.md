# stiffness

**Framework**: Core Animation  
**Kind**: property

The spring stiffness coefficient.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var stiffness: CGFloat { get set }
```

#### Discussion

The default stiffness coefficient is `100`. Increasing the [`stiffness`](caspringanimation/stiffness.md) reduces the number of oscillations and will reduce the settling duration. Decreasing the [`stiffness`](caspringanimation/stiffness.md) increases the the number of oscillations and will increase the settling duration.

## See Also

- [var damping: CGFloat](caspringanimation/damping.md)
  Defines how the spring’s motion should be damped due to the forces of friction.
- [var initialVelocity: CGFloat](caspringanimation/initialvelocity.md)
  The initial velocity of the object attached to the spring.
- [var mass: CGFloat](caspringanimation/mass.md)
  The mass of the object attached to the end of the spring.
- [var settlingDuration: CFTimeInterval](caspringanimation/settlingduration.md)
  The estimated duration required for the spring system to be considered at rest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caspringanimation/stiffness)*