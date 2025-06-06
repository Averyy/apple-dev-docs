# velocity(value:time:context:)

**Framework**: SwiftUI  
**Kind**: method

Calculates the current velocity of the animation.

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
func velocity<V>(value: V, time: TimeInterval, context: AnimationContext<V>) -> V? where V : VectorArithmetic
```

#### Return Value

The current velocity of the animation, or `nil` if the the velocity isn’t available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animation/velocity(value:time:context:))*