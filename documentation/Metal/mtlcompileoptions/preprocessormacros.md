# preprocessorMacros

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

A list of preprocessor macros to apply when compiling the library source.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var preprocessorMacros: [String : NSObject]? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) NSDictionary<NSString *,NSObject *> * preprocessorMacros;
```

#### Discussion

Define the macros as a dictionary where each key is a string, and the values can be either an [`NSString`](../../Foundation/nsstring.md) or [`NSNumber`](../../Foundation/nsnumber.md) instance.

The default value is `nil`.

## See Also

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
- [var optimizationLevel: MTLLibraryOptimizationLevel](./optimizationlevel.md)
  An option that tells the compiler what to prioritize when it compiles Metal shader code.
- [var libraries: [any MTLDynamicLibrary]?](./libraries.md)
  An array of dynamic libraries the Metal compiler links against.
- [var fastMathEnabled: Bool](./fastmathenabled.md)
  A Boolean value that indicates whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcompileoptions/preprocessormacros)*