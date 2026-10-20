# settlingDuration(target:initialVelocity:epsilon:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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
func settlingDuration<V>(target: V, initialVelocity: V = .zero, epsilon: Double) -> TimeInterval where V : VectorArithmetic
```

#### Discussion

The epsilon value specifies the threshold for how small all subsequent values need to be before the spring is considered to have settled.

## See Also

### Calculating forces and durations
- [func force<V>(target: V, position: V, velocity: V) -> V](./force%28target,position,velocity%29.md)
  Calculates the force upon the spring given a current position, target, and velocity amount of change.
- [func force<V>(fromValue: V, toValue: V, position: V, velocity: V) -> V](./force%28fromvalue,tovalue,position,velocity%29.md)
  Calculates the force upon the spring given a current position, velocity, and divisor from the starting and end values for the spring to travel.
- [func settlingDuration<V>(fromValue: V, toValue: V, initialVelocity: V, epsilon: Double) -> TimeInterval](./settlingduration%28fromvalue,tovalue,initialvelocity,epsilon%29.md)
  The estimated duration required for the spring system to be considered at rest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spring/settlingduration(target:initialvelocity:epsilon:))*