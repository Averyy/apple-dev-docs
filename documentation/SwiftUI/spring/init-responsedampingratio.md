# init(response:dampingRatio:)

**Framework**: SwiftUI  
**Kind**: init

Creates a spring with the specified response and damping ratio.

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
init(response: Double, dampingRatio: Double)
```

## Parameters

- `response`: Defines the stiffness of the spring as an approximate   duration in seconds.
- `dampingRatio`: Defines the amount of drag applied as a fraction the   amount needed to produce critical damping.

## See Also

- [init(duration: TimeInterval, bounce: Double)](spring/init(duration:bounce:).md)
  Creates a spring with the specified duration and bounce.
- [init(mass: Double, stiffness: Double, damping: Double, allowOverDamping: Bool)](spring/init(mass:stiffness:damping:allowoverdamping:).md)
  Creates a spring with the specified mass, stiffness, and damping.
- [init(settlingDuration: TimeInterval, dampingRatio: Double, epsilon: Double)](spring/init(settlingduration:dampingratio:epsilon:).md)
  Creates a spring with the specified duration and damping ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spring/init(response:dampingratio:))*