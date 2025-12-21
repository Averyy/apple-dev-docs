# fastMathEnabled

**Framework**: Metal  
**Kind**: property

A Boolean value that indicates whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var fastMathEnabled: Bool { get set }
```

#### Discussion

The default value is [`true`](https://developer.apple.com/documentation/Swift/true). A [`true`](https://developer.apple.com/documentation/Swift/true) value also enables the high-precision variant of math functions for single-precision floating-point scalar and vector types.

## See Also

- [Metal Shading Language Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)
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
- [var optimizationLevel: MTLLibraryOptimizationLevel](mtlcompileoptions/optimizationlevel.md)
  An option that tells the compiler what to prioritize when it compiles Metal shader code.
- [var libraries: [any MTLDynamicLibrary]?](mtlcompileoptions/libraries.md)
  An array of dynamic libraries the Metal compiler links against.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcompileoptions/fastmathenabled)*