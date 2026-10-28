# enableLogging

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

A Boolean value that enables shader logging.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var enableLogging: Bool { get set }
```

```objc
@property (nonatomic, readwrite) BOOL enableLogging;
```

## Mentions

- [Logging shader debug messages](../logging-shader-debug-messages.md)

## Discussion

Because logging incurs overhead, regardless of whether the system prints messages, you need to explicitly enable logging.

## See Also

### Configuring the compiler options
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
- [var fastMathEnabled: Bool](./fastmathenabled.md)
  A Boolean value that indicates whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcompileoptions/enablelogging)*