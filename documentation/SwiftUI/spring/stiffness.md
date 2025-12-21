# stiffness

**Framework**: SwiftUI  
**Kind**: property

The spring stiffness coefficient.

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
var stiffness: Double { get }
```

#### Discussion

Increasing the stiffness reduces the number of oscillations and will reduce the settling duration. Decreasing the stiffness increases the number of oscillations and will increase the settling duration.

## See Also

- [var bounce: Double](spring/bounce.md)
  How bouncy the spring is.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spring/stiffness)*