# animate(value:time:context:)

**Framework**: SwiftUI  
**Kind**: method

Calculates the current value of the animation.

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
func animate<V>(value: V, time: TimeInterval, context: inout AnimationContext<V>) -> V? where V : VectorArithmetic
```

#### Return Value

The current value of the animation, or `nil` if the animation has finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animation/animate(value:time:context:))*