# BNNSGraphCompileOptionsSetOutputFD(_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Sets the option for graph compilation to generate the graph object directly to the specified file descriptor.

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
func BNNSGraphCompileOptionsSetOutputFD(_ options: bnns_graph_compile_options_t, _ fd: Int32)
```

```c
void BNNSGraphCompileOptionsSetOutputFD(bnns_graph_compile_options_t options, int fd);
```

## Discussion

Use this option to specify that the graph [`BNNSGraphCompileFromFile(_:_:_:)`](./bnnsgraphcompilefromfile%28_,_,_%29.md) returns is a read-only memory-mapped file.

The option reduces the memory that compilation requires because BNNS doesn’t require the full set of graph weights to be memory resident.

Note that this option overrides the path that [`BNNSGraphCompileOptionsSetOutputPath(_:_:)`](./bnnsgraphcompileoptionssetoutputpath%28_,_%29.md) sets.

## Parameters

- `options`: The compilation options object.
- `fd`: The destination file descriptor. Pass `-1` to reset to the default behavior of strictly in-memory graph generation or the path that [`BNNSGraphCompileOptionsSetOutputPath(_:_:)`](./bnnsgraphcompileoptionssetoutputpath%28_,_%29.md) specifies.

  The file that the descriptor indicates must be open for writing. Graph compilation truncates and completely overwrites the file.

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
- [var BNNSTargetSystemGeneric: BNNSTargetSystem](./bnnstargetsystemgeneric.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraphcompileoptionssetoutputfd(_:_:))*