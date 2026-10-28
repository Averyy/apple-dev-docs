# languageVersion

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The language version for interpreting the library source code.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var languageVersion: MTLLanguageVersion { get set }
```

```objc
@property (nonatomic, readwrite) MTLLanguageVersion languageVersion;
```

## Discussion

By default, Metal uses the most recent language version.

## See Also

### Related Documentation
- [enum MTLLanguageVersion](../mtllanguageversion.md)
  Metal shading language versions.
### Configuring the compiler options
- [var enableLogging: Bool](./enablelogging.md)
  A Boolean value that enables shader logging.
- [var mathMode: MTLMathMode](./mathmode.md)
  An indication of whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.
- [var mathFloatingPointFunctions: MTLMathFloatingPointFunctions](./mathfloatingpointfunctions.md)
  The FP32 math functions Metal uses.
- [var preserveInvariance: Bool](./preserveinvariance.md)
  A Boolean value that indicates whether the compiler compiles vertex shaders conservatively to generate consistent position calculations.
- [var preprocessorMacros: [String : NSObject]?](./preprocessormacros.md)
  A list of preprocessor macros to apply when compiling the library source.
- [var optimizationLevel: MTLLibraryOptimizationLevel](./optimizationlevel.md)
  An option that tells the compiler what to prioritize when it compiles Metal shader code.
- [var libraries: [any MTLDynamicLibrary]?](./libraries.md)
  An array of dynamic libraries the Metal compiler links against.
- [var fastMathEnabled: Bool](./fastmathenabled.md)
  A Boolean value that indicates whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcompileoptions/languageversion)*