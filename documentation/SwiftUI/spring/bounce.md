# bounce

**Framework**: SwiftUI  
**Kind**: property

How bouncy the spring is.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var bounce: Double { get }
```

#### Discussion

A value of 0 indicates no bounces (a critically damped spring), positive values indicate increasing amounts of bounciness up to a maximum of 1.0 (corresponding to undamped oscillation), and negative values indicate overdamped springs with a minimum value of -1.0.

## See Also

- [var damping: Double](spring/damping.md)
  Defines how the spring’s motion should be damped due to the forces of friction.
- [var dampingRatio: Double](spring/dampingratio.md)
  The amount of drag applied, as a fraction of the amount needed to produce critical damping.
- [var duration: TimeInterval](spring/duration.md)
  The perceptual duration, which defines the pace of the spring.
- [var mass: Double](spring/mass.md)
  The mass of the object attached to the end of the spring.
- [var response: Double](spring/response.md)
  The stiffness of the spring, defined as an approximate duration in seconds.
- [var settlingDuration: TimeInterval](spring/settlingduration.md)
  The estimated duration required for the spring system to be considered at rest.
- [var stiffness: Double](spring/stiffness.md)
  The spring stiffness coefficient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spring/bounce)*