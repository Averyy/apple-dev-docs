# dampingRatio

**Framework**: SwiftUI  
**Kind**: property

The amount of drag applied, as a fraction of the amount needed to produce critical damping.

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
var dampingRatio: Double { get }
```

#### Discussion

When `dampingRatio` is 1, the spring will smoothly decelerate to its final position without oscillating. Damping ratios less than 1 will oscillate more and more before coming to a complete stop.

## See Also

- [var bounce: Double](spring/bounce.md)
  How bouncy the spring is.
- [var damping: Double](spring/damping.md)
  Defines how the spring’s motion should be damped due to the forces of friction.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spring/dampingratio)*