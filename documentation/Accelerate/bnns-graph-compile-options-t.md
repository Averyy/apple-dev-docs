# bnns_graph_compile_options_t

**Framework**: Accelerate  
**Kind**: struct

The compilation options that BNNS uses when compiling a source mlmodelc file to a graph object.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct bnns_graph_compile_options_t
```

#### Overview

Call [`BNNSGraphCompileOptionsMakeDefault()`](bnnsgraphcompileoptionsmakedefault().md) to create a default options structure and then call functions such as [`BNNSGraphCompileOptionsSetOptimizationPreference(_:_:)`](bnnsgraphcompileoptionssetoptimizationpreference(_:_:).md) to set indivual options.

## Topics

### Initializing an options structure
- [init()](bnns_graph_compile_options_t/init.md)
  Creates an empty compilation options structure.
- [init(data: UnsafeMutableRawPointer?, size: Int)](bnns_graph_compile_options_t/init(data:size:).md)
  Creates a compilation options structure from the specified opaque compilation options object.
### Specifying an options structure’s properties
- [var data: UnsafeMutableRawPointer?](bnns_graph_compile_options_t/data.md)
  A pointer to the opaque compilation options object.
- [var size: Int](bnns_graph_compile_options_t/size.md)
  The size, in bytes, of the opaque compilation options object.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [func BNNSGraphCompileOptionsMakeDefault() -> bnns_graph_compile_options_t](bnnsgraphcompileoptionsmakedefault().md)
  Returns an allocated compilation options object with default values.
- [func BNNSGraphCompileOptionsDestroy(bnns_graph_compile_options_t)](bnnsgraphcompileoptionsdestroy(_:).md)
  Destroys the specified compilation options object.
- [func BNNSGraphCompileOptionsSetOutputPath(bnns_graph_compile_options_t, UnsafePointer<CChar>?)](bnnsgraphcompileoptionssetoutputpath(_:_:).md)
  Sets the option for graph compilation to generate the graph object directly to the specified file.
- [func BNNSGraphCompileOptionsGetOutputPath(bnns_graph_compile_options_t) -> UnsafePointer<CChar>?](bnnsgraphcompileoptionsgetoutputpath(_:).md)
  Returns the option for the compiled graph’s output path.
- [func BNNSGraphCompileOptionsSetOutputFD(bnns_graph_compile_options_t, Int32)](bnnsgraphcompileoptionssetoutputfd(_:_:).md)
  Sets the option for graph compilation to generate the graph object directly to the specified file descriptor.
- [func BNNSGraphCompileOptionsGetOutputFD(bnns_graph_compile_options_t) -> Int32](bnnsgraphcompileoptionsgetoutputfd(_:).md)
  Returns the option for the compiled graph’s output file descriptor.
- [func BNNSGraphCompileOptionsSetTargetSingleThread(bnns_graph_compile_options_t, Bool)](bnnsgraphcompileoptionssettargetsinglethread(_:_:).md)
  Sets the option for the compiled graph to execute on a single thread.
- [func BNNSGraphCompileOptionsGetTargetSingleThread(bnns_graph_compile_options_t) -> Bool](bnnsgraphcompileoptionsgettargetsinglethread(_:).md)
  Returns the option for the compiled graph to execute on a single thread.
- [func BNNSGraphCompileOptionsSetOptimizationPreference(bnns_graph_compile_options_t, BNNSGraphOptimizationPreference)](bnnsgraphcompileoptionssetoptimizationpreference(_:_:).md)
  Sets the option for the compiled graph to optimize for either size or performance.
- [func BNNSGraphCompileOptionsGetOptimizationPreference(bnns_graph_compile_options_t) -> BNNSGraphOptimizationPreference](bnnsgraphcompileoptionsgetoptimizationpreference(_:).md)
  Returns the option for the compiled graph to optimize for either size or performance.
- [struct BNNSGraphOptimizationPreference](bnnsgraphoptimizationpreference.md)
  Constants that describe the compilation optimization preference.
- [func BNNSGraphCompileOptionsSetGenerateDebugInfo(bnns_graph_compile_options_t, Bool)](bnnsgraphcompileoptionssetgeneratedebuginfo(_:_:).md)
  Sets the option for the compiled graph to include debugging information.
- [func BNNSGraphCompileOptionsGetGenerateDebugInfo(bnns_graph_compile_options_t) -> Bool](bnnsgraphcompileoptionsgetgeneratedebuginfo(_:).md)
  Returns the option for the compiled graph to include debugging information.
- [var BNNSTargetSystemGeneric: BNNSTargetSystem](bnnstargetsystemgeneric.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns_graph_compile_options_t)*