# logicallyComplete(after:)

**Framework**: SwiftUI  
**Kind**: method

Causes the animation to report logical completion after the specified duration, if it has not already logically completed.

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
func logicallyComplete(after duration: TimeInterval) -> Animation
```

#### Return Value

An animation that reports logical completion after the given duration.

#### Discussion

Note that the indicated duration will not cause the animation to continue running after the base animation has fully completed.

If the animation is removed before the given duration is reached, logical completion will be reported immediately.

## Parameters

- `duration`: The duration after which the animation should  report   that it is logically complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animation/logicallycomplete(after:))*