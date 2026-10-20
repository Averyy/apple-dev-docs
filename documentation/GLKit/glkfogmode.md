# GLKFogMode

**Framework**: GLKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum GLKFogMode : GLint;
```

## Topics

### Constants
- [GLKFogMode.exp](./glkfogmode/exp.md)
  The fog component is calculated as `exp(-density * distance)` and clamped to the range `[0.0, 1.0]`.
- [GLKFogMode.exp2](./glkfogmode/exp2.md)
  The fog component is calculated as `exp(-(density * distance)^2)` and clamped to the range `[0.0, 1.0]`.
- [GLKFogMode.linear](./glkfogmode/linear.md)
  The fog component is calculated as `(end - distance) / (end - start)` and clamped to the range `[0.0, 1.0]`.
### Initializers
- [init?(rawValue: GLint)](./glkfogmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkfogmode)*