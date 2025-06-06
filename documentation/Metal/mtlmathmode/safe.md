# MTLMathMode.safe

**Framework**: Metal  
**Kind**: case

An indicator of the mode the compiler uses to disable unsafe floating-point optimizations by preventing the compiler from making any transformations that could affect the results.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
case safe
```

## See Also

- [MTLMathMode.fast](mtlmathmode/fast.md)
  An indicator of the mode the compiler uses to make aggressive, potentially lossy assumptions about floating-point math.
- [MTLMathMode.relaxed](mtlmathmode/relaxed.md)
  An indicator of the mode the compiler uses to make aggressive, potentially lossy assumptions about floating-point math, while honoring Inf/NaN.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlmathmode/safe)*