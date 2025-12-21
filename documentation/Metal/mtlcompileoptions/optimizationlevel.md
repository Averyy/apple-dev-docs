# optimizationLevel

**Framework**: Metal  
**Kind**: property

An option that tells the compiler what to prioritize when it compiles Metal shader code.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var optimizationLevel: MTLLibraryOptimizationLevel { get set }
```

## Mentions

- [Minimizing the binary size of a shader library](minimizing-the-binary-size-of-a-shader-library.md)

## See Also

- [var enableLogging: Bool](mtlcompileoptions/enablelogging.md)
  A Boolean value that enables shader logging.
- [var mathMode: MTLMathMode](mtlcompileoptions/mathmode.md)
  An indication of whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.
- [var mathFloatingPointFunctions: MTLMathFloatingPointFunctions](mtlcompileoptions/mathfloatingpointfunctions.md)
  The FP32 math functions Metal uses.
- [var preserveInvariance: Bool](mtlcompileoptions/preserveinvariance.md)
  A Boolean value that indicates whether the compiler compiles vertex shaders conservatively to generate consistent position calculations.
- [var languageVersion: MTLLanguageVersion](mtlcompileoptions/languageversion.md)
  The language version for interpreting the library source code.
- [var preprocessorMacros: [String : NSObject]?](mtlcompileoptions/preprocessormacros.md)
  A list of preprocessor macros to apply when compiling the library source.
- [var libraries: [any MTLDynamicLibrary]?](mtlcompileoptions/libraries.md)
  An array of dynamic libraries the Metal compiler links against.
- [var fastMathEnabled: Bool](mtlcompileoptions/fastmathenabled.md)
  A Boolean value that indicates whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcompileoptions/optimizationlevel)*