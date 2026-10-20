# velocity(fromValue:toValue:initialVelocity:time:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Calculates the velocity of the spring at a given time given a starting and ending value for the spring to travel.

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
func velocity<V>(fromValue: V, toValue: V, initialVelocity: V, time: TimeInterval) -> V where V : Animatable
```

## See Also

### Getting spring state
- [func value<V>(target: V, initialVelocity: V, time: TimeInterval) -> V](./value%28target,initialvelocity,time%29.md)
  Calculates the value of the spring at a given time given a target amount of change.
- [func value<V>(fromValue: V, toValue: V, initialVelocity: V, time: TimeInterval) -> V](./value%28fromvalue,tovalue,initialvelocity,time%29.md)
  Calculates the value of the spring at a given time for a starting and ending value for the spring to travel.
- [func velocity<V>(target: V, initialVelocity: V, time: TimeInterval) -> V](./velocity%28target,initialvelocity,time%29.md)
  Calculates the velocity of the spring at a given time given a target amount of change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spring/velocity(fromvalue:tovalue:initialvelocity:time:))*