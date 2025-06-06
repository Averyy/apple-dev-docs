# value(target:initialVelocity:time:)

**Framework**: SwiftUI  
**Kind**: method

Calculates the value of the spring at a given time given a target amount of change.

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
func value<V>(target: V, initialVelocity: V = .zero, time: TimeInterval) -> V where V : VectorArithmetic
```

## See Also

- [func value<V>(fromValue: V, toValue: V, initialVelocity: V, time: TimeInterval) -> V](spring/value(fromvalue:tovalue:initialvelocity:time:).md)
  Calculates the value of the spring at a given time for a starting and ending value for the spring to travel.
- [func velocity<V>(target: V, initialVelocity: V, time: TimeInterval) -> V](spring/velocity(target:initialvelocity:time:).md)
  Calculates the velocity of the spring at a given time given a target amount of change.
- [func velocity<V>(fromValue: V, toValue: V, initialVelocity: V, time: TimeInterval) -> V](spring/velocity(fromvalue:tovalue:initialvelocity:time:).md)
  Calculates the velocity of the spring at a given time given a starting and ending value for the spring to travel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spring/value(target:initialvelocity:time:))*