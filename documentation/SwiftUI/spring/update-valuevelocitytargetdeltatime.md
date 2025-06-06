# update(value:velocity:target:deltaTime:)

**Framework**: SwiftUI  
**Kind**: method

Updates the current  value and velocity of a spring.

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
func update<V>(value: inout V, velocity: inout V, target: V, deltaTime: TimeInterval) where V : VectorArithmetic
```

## Parameters

- `value`: The current value of the spring.
- `velocity`: The current velocity of the spring.
- `target`: The target that   is moving towards.
- `deltaTime`: The amount of time that has passed since the spring was   at the position specified by  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spring/update(value:velocity:target:deltatime:))*