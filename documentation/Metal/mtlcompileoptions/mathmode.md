# mathMode

**Framework**: Metal  
**Kind**: property

An indication of whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var mathMode: MTLMathMode { get set }
```

#### Discussion

This property replaces the [`fastMathEnabled`](mtlcompileoptions/fastmathenabled.md) property.

If [`fastMathEnabled`](mtlcompileoptions/fastmathenabled.md) is `true`, the system sets [`mathMode`](mtlcompileoptions/mathmode.md) to [`MTLMathMode.fast`](mtlmathmode/fast.md) and [`mathFloatingPointFunctions`](mtlcompileoptions/mathfloatingpointfunctions.md) to [`MTLMathFloatingPointFunctions.fast`](mtlmathfloatingpointfunctions/fast.md).

If [`fastMathEnabled`](mtlcompileoptions/fastmathenabled.md) is `false`, the system sets [`mathMode`](mtlcompileoptions/mathmode.md) to [`MTLMathMode.safe`](mtlmathmode/safe.md) and [`mathFloatingPointFunctions`](mtlcompileoptions/mathfloatingpointfunctions.md) to [`MTLMathFloatingPointFunctions.precise`](mtlmathfloatingpointfunctions/precise.md).

Subsequent calls to [`mathMode`](mtlcompileoptions/mathmode.md) or [`mathFloatingPointFunctions`](mtlcompileoptions/mathfloatingpointfunctions.md) set the variables directly.

## Topics

### Supporting types
- [enum MTLMathMode](mtlmathmode.md)
  An indication of whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.

## See Also

- [var enableLogging: Bool](mtlcompileoptions/enablelogging.md)
  A Boolean value that enables shader logging.
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
- [var fastMathEnabled: Bool](mtlcompileoptions/fastmathenabled.md)
  A Boolean value that indicates whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcompileoptions/mathmode)*