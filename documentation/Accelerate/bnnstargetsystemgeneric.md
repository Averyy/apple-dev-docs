# BNNSTargetSystemGeneric

**Framework**: Accelerate  
**Kind**: var  
**Role**: Global Variable

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

```c
BNNSTargetSystemGeneric
```

## See Also

### Specifying and querying compilation options
- [struct bnns_graph_compile_options_t](./bnns_graph_compile_options_t.md)
  The compilation options that BNNS uses when compiling a source mlmodelc file to a graph object.
- [func BNNSGraphCompileOptionsMakeDefault() -> bnns_graph_compile_options_t](./bnnsgraphcompileoptionsmakedefault%28%29.md)
  Returns an allocated compilation options object with default values.
- [func BNNSGraphCompileOptionsDestroy(bnns_graph_compile_options_t)](./bnnsgraphcompileoptionsdestroy%28_%29.md)
  Destroys the specified compilation options object.
- [func BNNSGraphCompileOptionsSetOutputPath(bnns_graph_compile_options_t, UnsafePointer<CChar>?)](./bnnsgraphcompileoptionssetoutputpath%28_,_%29.md)
  Sets the option for graph compilation to generate the graph object directly to the specified file.
- [func BNNSGraphCompileOptionsGetOutputPath(bnns_graph_compile_options_t) -> UnsafePointer<CChar>?](./bnnsgraphcompileoptionsgetoutputpath%28_%29.md)
  Returns the option for the compiled graph’s output path.
- [func BNNSGraphCompileOptionsSetOutputFD(bnns_graph_compile_options_t, Int32)](./bnnsgraphcompileoptionssetoutputfd%28_,_%29.md)
  Sets the option for graph compilation to generate the graph object directly to the specified file descriptor.
- [func BNNSGraphCompileOptionsGetOutputFD(bnns_graph_compile_options_t) -> Int32](./bnnsgraphcompileoptionsgetoutputfd%28_%29.md)
  Returns the option for the compiled graph’s output file descriptor.
- [func BNNSGraphCompileOptionsSetTargetSingleThread(bnns_graph_compile_options_t, Bool)](./bnnsgraphcompileoptionssettargetsinglethread%28_,_%29.md)
  Sets the option for the compiled graph to execute on a single thread.
- [func BNNSGraphCompileOptionsGetTargetSingleThread(bnns_graph_compile_options_t) -> Bool](./bnnsgraphcompileoptionsgettargetsinglethread%28_%29.md)
  Returns the option for the compiled graph to execute on a single thread.
- [func BNNSGraphCompileOptionsSetOptimizationPreference(bnns_graph_compile_options_t, BNNSGraphOptimizationPreference)](./bnnsgraphcompileoptionssetoptimizationpreference%28_,_%29.md)
  Sets the option for the compiled graph to optimize for either size or performance.
- [func BNNSGraphCompileOptionsGetOptimizationPreference(bnns_graph_compile_options_t) -> BNNSGraphOptimizationPreference](./bnnsgraphcompileoptionsgetoptimizationpreference%28_%29.md)
  Returns the option for the compiled graph to optimize for either size or performance.
- [struct BNNSGraphOptimizationPreference](./bnnsgraphoptimizationpreference.md)
  Constants that describe the compilation optimization preference.
- [func BNNSGraphCompileOptionsSetGenerateDebugInfo(bnns_graph_compile_options_t, Bool)](./bnnsgraphcompileoptionssetgeneratedebuginfo%28_,_%29.md)
  Sets the option for the compiled graph to include debugging information.
- [func BNNSGraphCompileOptionsGetGenerateDebugInfo(bnns_graph_compile_options_t) -> Bool](./bnnsgraphcompileoptionsgetgeneratedebuginfo%28_%29.md)
  Returns the option for the compiled graph to include debugging information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnstargetsystemgeneric)*