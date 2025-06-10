# settlingDuration(fromValue:toValue:initialVelocity:epsilon:)

**Framework**: SwiftUI  
**Kind**: method

The estimated duration required for the spring system to be considered at rest.

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
func settlingDuration<V>(fromValue: V, toValue: V, initialVelocity: V, epsilon: Double) -> TimeInterval where V : Animatable
```

#### Discussion

The epsilon value specifies the threshold for how small all subsequent values need to be before the spring is considered to have settled.

## See Also

- [func force<V>(target: V, position: V, velocity: V) -> V](spring/force(target:position:velocity:).md)
  Calculates the force upon the spring given a current position, target, and velocity amount of change.
- [func force<V>(fromValue: V, toValue: V, position: V, velocity: V) -> V](spring/force(fromvalue:tovalue:position:velocity:).md)
  Calculates the force upon the spring given a current position, velocity, and divisor from the starting and end values for the spring to travel.
- [func settlingDuration<V>(target: V, initialVelocity: V, epsilon: Double) -> TimeInterval](spring/settlingduration(target:initialvelocity:epsilon:).md)
  The estimated duration required for the spring system to be considered at rest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spring/settlingduration(fromvalue:tovalue:initialvelocity:epsilon:))*