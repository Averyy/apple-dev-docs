# MTLMathMode.safe

**Framework**: Metal  
**Kind**: case  
**Role**: Case

An indicator of the mode the compiler uses to disable unsafe floating-point optimizations by preventing the compiler from making any transformations that could affect the results.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
case safe
```

```c
MTLMathModeSafe
```

## See Also

### Modes
- [MTLMathMode.fast](./fast.md)
  An indicator of the mode the compiler uses to make aggressive, potentially lossy assumptions about floating-point math.
- [MTLMathMode.relaxed](./relaxed.md)
  An indicator of the mode the compiler uses to make aggressive, potentially lossy assumptions about floating-point math, while honoring Inf/NaN.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlmathmode/safe)*