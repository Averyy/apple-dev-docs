# MTLMathMode.relaxed

**Framework**: Metal  
**Kind**: case

An indicator of the mode the compiler uses to make aggressive, potentially lossy assumptions about floating-point math, while honoring Inf/NaN.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
case relaxed
```

#### Discussion

This is the default for Apple silicon devices.

## See Also

- [MTLMathMode.fast](mtlmathmode/fast.md)
  An indicator of the mode the compiler uses to make aggressive, potentially lossy assumptions about floating-point math.
- [MTLMathMode.safe](mtlmathmode/safe.md)
  An indicator of the mode the compiler uses to disable unsafe floating-point optimizations by preventing the compiler from making any transformations that could affect the results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlmathmode/relaxed)*