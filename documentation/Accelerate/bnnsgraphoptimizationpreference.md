# BNNSGraphOptimizationPreference

**Framework**: Accelerate  
**Kind**: struct

Constants that describe the compilation optimization preference.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct BNNSGraphOptimizationPreference
```

## Topics

### Optimization preferences
- [init(UInt32)](bnnsgraphoptimizationpreference/init(_:).md)
  Creates a new instance.
- [init(rawValue: UInt32)](bnnsgraphoptimizationpreference/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance properties
- [var rawValue: UInt32](bnnsgraphoptimizationpreference/rawvalue.md)
  The corresponding value of the raw type.
- [var BNNSGraphOptimizationPreferenceIRSize: BNNSGraphOptimizationPreference](bnnsgraphoptimizationpreferenceirsize.md)
  A constant that specifies compilation optimization for smallest graph size on disk.
- [var BNNSGraphOptimizationPreferencePerformance: BNNSGraphOptimizationPreference](bnnsgraphoptimizationpreferenceperformance.md)
  A constant that specifies compilation optimization for best execution performance.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

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
- [func BNNSGraphCompileOptionsSetGenerateDebugInfo(bnns_graph_compile_options_t, Bool)](bnnsgraphcompileoptionssetgeneratedebuginfo(_:_:).md)
  Sets the option for the compiled graph to include debugging information.
- [func BNNSGraphCompileOptionsGetGenerateDebugInfo(bnns_graph_compile_options_t) -> Bool](bnnsgraphcompileoptionsgetgeneratedebuginfo(_:).md)
  Returns the option for the compiled graph to include debugging information.
- [var BNNSTargetSystemGeneric: BNNSTargetSystem](bnnstargetsystemgeneric.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraphoptimizationpreference)*