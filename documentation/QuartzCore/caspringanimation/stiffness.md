# stiffness

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property CGFloat stiffness;
```

## Discussion

The default stiffness coefficient is `100`. Increasing the [`stiffness`](./stiffness.md) reduces the number of oscillations and will reduce the settling duration. Decreasing the [`stiffness`](./stiffness.md) increases the the number of oscillations and will increase the settling duration.

## See Also

### Configuring Physical Attributes
- [var damping: CGFloat](./damping.md)
  Defines how the spring’s motion should be damped due to the forces of friction.
- [var initialVelocity: CGFloat](./initialvelocity.md)
  The initial velocity of the object attached to the spring.
- [var mass: CGFloat](./mass.md)
  The mass of the object attached to the end of the spring.
- [var settlingDuration: CFTimeInterval](./settlingduration.md)
  The estimated duration required for the spring system to be considered at rest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caspringanimation/stiffness)*