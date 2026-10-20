# fastMathEnabled

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.

**Availability**:
- iOS 8.0+ - Deprecated in 18.0
- iPadOS 8.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use [`mathMode`](./mathmode.md) instead.

## Declaration

```swift
var fastMathEnabled: Bool { get set }
```

```objc
@property (nonatomic, readwrite) BOOL fastMathEnabled;
```

#### Discussion

The default value is [`true`](../../Swift/true.md). A [`true`](../../Swift/true.md) value also enables the high-precision variant of math functions for single-precision floating-point scalar and vector types.

## See Also

### Related Documentation
- [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)
### Configuring the compiler options
- [var enableLogging: Bool](./enablelogging.md)
  A Boolean value that enables shader logging.
- [var mathMode: MTLMathMode](./mathmode.md)
  An indication of whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.
- [var mathFloatingPointFunctions: MTLMathFloatingPointFunctions](./mathfloatingpointfunctions.md)
  The FP32 math functions Metal uses.
- [var preserveInvariance: Bool](./preserveinvariance.md)
  A Boolean value that indicates whether the compiler compiles vertex shaders conservatively to generate consistent position calculations.
- [var languageVersion: MTLLanguageVersion](./languageversion.md)
  The language version for interpreting the library source code.
- [var preprocessorMacros: [String : NSObject]?](./preprocessormacros.md)
  A list of preprocessor macros to apply when compiling the library source.
- [var optimizationLevel: MTLLibraryOptimizationLevel](./optimizationlevel.md)
  An option that tells the compiler what to prioritize when it compiles Metal shader code.
- [var libraries: [any MTLDynamicLibrary]?](./libraries.md)
  An array of dynamic libraries the Metal compiler links against.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcompileoptions/fastmathenabled)*