# debugLayers

**Framework**: ML Compute  
**Kind**: property  
**Role**: Type Property

The option to debug layers during graph compilation.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
static var debugLayers: MLCGraphCompilationOptions { get }
```

```c
MLCGraphCompilationOptionsDebugLayers
```

#### Discussion

Include this option to disable various optimizations such as layer fusion, and ensure the framework synchronizes the resulting forward and gradients tensors host memory with device memory, for layers marked as debuggable.

## See Also

### Creating Graph Compilation Options
- [init(rawValue: UInt64)](./init%28rawvalue%29.md)
  Creates a graph compilation option with the specified raw value.
- [static var disableLayerFusion: MLCGraphCompilationOptions](./disablelayerfusion.md)
  The option to disable layer fusion during graph compilation.
- [static var linkGraphs: MLCGraphCompilationOptions](./linkgraphs.md)
  The option to link graphs during graph compilation.
- [static var computeAllGradients: MLCGraphCompilationOptions](./computeallgradients.md)
  The option to compute all gradients during graph compilation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgraphcompilationoptions/debuglayers)*