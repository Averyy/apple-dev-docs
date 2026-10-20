# duration

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The perceptual duration, which defines the pace of the spring.

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
var duration: TimeInterval { get }
```

## See Also

### Getting spring characteristics
- [var bounce: Double](./bounce.md)
  How bouncy the spring is.
- [var damping: Double](./damping.md)
  Defines how the spring’s motion should be damped due to the forces of friction.
- [var dampingRatio: Double](./dampingratio.md)
  The amount of drag applied, as a fraction of the amount needed to produce critical damping.
- [var mass: Double](./mass.md)
  The mass of the object attached to the end of the spring.
- [var response: Double](./response.md)
  The stiffness of the spring, defined as an approximate duration in seconds.
- [var settlingDuration: TimeInterval](./settlingduration.md)
  The estimated duration required for the spring system to be considered at rest.
- [var stiffness: Double](./stiffness.md)
  The spring stiffness coefficient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spring/duration)*