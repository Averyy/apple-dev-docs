# init(duration:bounce:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a spring with the specified duration and bounce.

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
init(duration: TimeInterval = 0.5, bounce: Double = 0.0)
```

## Parameters

- `duration`: Defines the pace of the spring. This is approximately equal to the settling duration, but for springs with very large bounce values, will be the duration of the period of oscillation for the spring.
- `bounce`: How bouncy the spring should be. A value of 0 indicates no bounces (a critically damped spring), positive values indicate increasing amounts of bounciness up to a maximum of 1.0 (corresponding to undamped oscillation), and negative values indicate overdamped springs with a minimum value of -1.0.

## See Also

### Creating a spring
- [init(mass: Double, stiffness: Double, damping: Double, allowOverDamping: Bool)](./init%28mass,stiffness,damping,allowoverdamping%29.md)
  Creates a spring with the specified mass, stiffness, and damping.
- [init(response: Double, dampingRatio: Double)](./init%28response,dampingratio%29.md)
  Creates a spring with the specified response and damping ratio.
- [init(settlingDuration: TimeInterval, dampingRatio: Double, epsilon: Double)](./init%28settlingduration,dampingratio,epsilon%29.md)
  Creates a spring with the specified duration and damping ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spring/init(duration:bounce:))*