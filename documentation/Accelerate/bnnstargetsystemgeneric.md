# BNNSTargetSystemGeneric

**Framework**: Accelerate  
**Kind**: var

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var BNNSTargetSystemGeneric: BNNSTargetSystem { get }
```

## See Also

- [struct bnns_graph_compile_options_t](bnns_graph_compile_options_t.md)
  The compilation options that BNNS uses when compiling a source mlmodelc file to a graph object.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnstargetsystemgeneric)*