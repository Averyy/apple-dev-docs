# shouldMerge(previous:value:time:context:)

**Framework**: SwiftUI  
**Kind**: method

Returns a Boolean value that indicates whether the current animation should merge with a previous animation.

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
func shouldMerge<V>(previous: Animation, value: V, time: TimeInterval, context: inout AnimationContext<V>) -> Bool where V : VectorArithmetic
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animation/shouldmerge(previous:value:time:context:))*