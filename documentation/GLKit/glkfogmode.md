# GLKFogMode

**Framework**: GLKit  
**Kind**: enum

A mode that describes how the fog component is calculated for the fragment.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
enum GLKFogMode
```

## Topics

### Constants
- [GLKFogMode.exp](glkfogmode/exp.md)
  The fog component is calculated as `exp(-density * distance)` and clamped to the range `[0.0, 1.0]`.
- [GLKFogMode.exp2](glkfogmode/exp2.md)
  The fog component is calculated as `exp(-(density * distance)^2)` and clamped to the range `[0.0, 1.0]`.
- [GLKFogMode.linear](glkfogmode/linear.md)
  The fog component is calculated as `(end - distance) / (end - start)` and clamped to the range `[0.0, 1.0]`.
### Initializers
- [init?(rawValue: GLint)](glkfogmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkfogmode)*