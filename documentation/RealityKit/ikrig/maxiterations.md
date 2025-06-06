# maxIterations

**Framework**: RealityKit  
**Kind**: property

The maximum number of iterations the solver is allowed to do per frame.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var maxIterations: Int
```

#### Discussion

If the pose satisfies all of the demands using less iterations, the solve stops early.

> **Note**: Values of `0` or less, result in the constant output of the last solved pose.

Values of `0` or less, result in the constant output of the last solved pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikrig/maxiterations)*