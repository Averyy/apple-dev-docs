# MTLCompileOptions

**Framework**: Metal  
**Kind**: class

Compilation settings for a Metal shader library.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class MTLCompileOptions
```

## Mentions

- [Logging shader debug messages](logging-shader-debug-messages.md)
- [Minimizing the Binary Size of a Shader Library](minimizing-the-binary-size-of-a-shader-library.md)

#### Overview

You can configure the Metal compiler’s options by setting any or all of an [`MTLCompileOptions`](mtlcompileoptions.md) instance’s properties, including the following:

- Target previous OS releases by assigning the [`languageVersion`](mtlcompileoptions/languageversion.md) property to an [`MTLLanguageVersion`](mtllanguageversion.md) case.
- Set preprocessor macros for the Metal compiler by assigning a dictionary to the [`preprocessorMacros`](mtlcompileoptions/preprocessormacros.md) property.
- Choose what the Metal compiler’s optimizer prioritizes by setting the [`optimizationLevel`](mtlcompileoptions/optimizationlevel.md) property to an [`MTLLibraryOptimizationLevel`](mtllibraryoptimizationlevel.md) case.
- Allow the compiler to optimize for floating-point arithmetic that may violate the IEEE 754 standard by setting [`mathMode`](mtlcompileoptions/mathmode.md) to [`MTLMathMode.fast`](mtlmathmode/fast.md).

You can compile a library with your compile options instance by calling an [`MTLDevice`](mtldevice.md) instance’s [`makeLibrary(source:options:)`](mtldevice/makelibrary(source:options:).md) or [`makeLibrary(source:options:completionHandler:)`](mtldevice/makelibrary(source:options:completionhandler:).md) method.

## Topics

### Configuring the Compiler Options
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
- [var fastMathEnabled: Bool](mtlcompileoptions/fastmathenabled.md)
  A Boolean value that indicates whether the compiler can perform optimizations for floating-point arithmetic that may violate the IEEE 754 standard.
### Configuring the Library Output Options
- [var libraryType: MTLLibraryType](mtlcompileoptions/librarytype.md)
  The kind of library to create.
- [var installName: String?](mtlcompileoptions/installname.md)
  For a dynamic library, the name to use when installing the library.
### Instance Properties
- [var allowReferencingUndefinedSymbols: Bool](mtlcompileoptions/allowreferencingundefinedsymbols.md)
- [var compileSymbolVisibility: MTLCompileSymbolVisibility](mtlcompileoptions/compilesymbolvisibility.md)
- [var maxTotalThreadsPerThreadgroup: Int](mtlcompileoptions/maxtotalthreadsperthreadgroup.md)
- [var requiredThreadsPerThreadgroup: MTLSize](mtlcompileoptions/requiredthreadsperthreadgroup.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MTLLibrary](mtllibrary.md)
  A collection of Metal shader functions.
- [protocol MTLDynamicLibrary](mtldynamiclibrary.md)
  A dynamically linkable representation of compiled shader code for a specific Metal device object.
- [protocol MTLBinaryArchive](mtlbinaryarchive.md)
  A container for pipeline state descriptors and their associated compiled shader code.
- [enum MTLLibraryType](mtllibrarytype.md)
  A set of options for Metal library types.
- [enum MTLLanguageVersion](mtllanguageversion.md)
  Metal shading language versions.
- [enum MTLCompileSymbolVisibility](mtlcompilesymbolvisibility.md)
- [enum MTLLibraryOptimizationLevel](mtllibraryoptimizationlevel.md)
  The optimization options for the Metal compiler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcompileoptions)*