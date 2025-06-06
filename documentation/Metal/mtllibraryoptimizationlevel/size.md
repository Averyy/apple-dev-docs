# MTLLibraryOptimizationLevel.size

**Framework**: Metal  
**Kind**: case

An optimization option for the Metal compiler that prioritizes minimizing the size of its output binaries, which may also reduce compile time.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
case size
```

## Mentions

- [Minimizing the Binary Size of a Shader Library](minimizing-the-binary-size-of-a-shader-library.md)

#### Discussion

This option is similar to [`MTLLibraryOptimizationLevel.default`](mtllibraryoptimizationlevel/default.md), but adds optimizations that prioritize minimizing a shader’s executable size, which may also reduce compile time.

## See Also

- [MTLLibraryOptimizationLevel.default](mtllibraryoptimizationlevel/default.md)
  An optimization option for the Metal compiler that prioritizes runtime performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllibraryoptimizationlevel/size)*