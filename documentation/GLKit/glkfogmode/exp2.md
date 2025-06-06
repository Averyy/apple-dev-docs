# GLKFogMode.exp2

**Framework**: GLKit  
**Kind**: case

The fog component is calculated as `exp(-(density * distance)^2)` and clamped to the range `[0.0, 1.0]`.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
case exp2
```

## See Also

- [GLKFogMode.exp](glkfogmode/exp.md)
  The fog component is calculated as `exp(-density * distance)` and clamped to the range `[0.0, 1.0]`.
- [GLKFogMode.linear](glkfogmode/linear.md)
  The fog component is calculated as `(end - distance) / (end - start)` and clamped to the range `[0.0, 1.0]`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkfogmode/exp2)*