# preserveInvariance

**Framework**: Metal  
**Kind**: property

A Boolean value that indicates whether the compiler compiles vertex shaders conservatively to generate consistent position calculations.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var preserveInvariance: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/swift/false). When [`true`](https://developer.apple.com/documentation/swift/true), the Metal shader compiler looks at the position value in all vertex output structures that it compiles. If the position value also has the `[[invariant]]` attribute, the compiler compiles the corresponding vertex shader conservatively to guarantee that the GPU performs the calculations the same way. You need to preserve invariance when your renderer contains multiple render passes and requires the same position calculations in each render pass.

## See Also

- [var enableLogging: Bool](mtlcompileoptions/enablelogging.md)
  A Boolean value that enables shader logging.
- [var mathMode: MTLMathMode](mtlcompileoptions/mathmode.md)
  An indication of whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.
- [var mathFloatingPointFunctions: MTLMathFloatingPointFunctions](mtlcompileoptions/mathfloatingpointfunctions.md)
  The FP32 math functions Metal uses.
- [var languageVersion: MTLLanguageVersion](mtlcompileoptions/languageversion.md)
  The language version for interpreting the library source code.
- [var preprocessorMacros: [String : NSObject]?](mtlcompileoptions/preprocessormacros.md)
  A list of preprocessor macros to apply when compiling the library source.
- [var optimizationLevel: MTLLibraryOptimizationLevel](mtlcompileoptions/optimizationlevel.md)
  An option that tells the compiler what to prioritize when it compiles Metal shader code.
- [var libraries: [any MTLDynamicLibrary]?](mtlcompileoptions/libraries.md)
  An array of dynamic libraries the Metal compiler links against.
- [var fastMathEnabled: Bool](mtlcompileoptions/fastmathenabled.md)
  A Boolean value that indicates whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcompileoptions/preserveinvariance)*