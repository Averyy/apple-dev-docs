# MTLLibraryOptimizationLevel.size

**Framework**: Metal  
**Kind**: case  
**Role**: Case

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

```c
MTLLibraryOptimizationLevelSize
```

## Mentions

- [Minimizing the binary size of a shader library](../minimizing-the-binary-size-of-a-shader-library.md)

## Discussion

This option is similar to [`MTLLibraryOptimizationLevel.default`](./default.md), but adds optimizations that prioritize minimizing a shader’s executable size, which may also reduce compile time.

## See Also

### Optimization options
- [MTLLibraryOptimizationLevel.default](./default.md)
  An optimization option for the Metal compiler that prioritizes runtime performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllibraryoptimizationlevel/size)*