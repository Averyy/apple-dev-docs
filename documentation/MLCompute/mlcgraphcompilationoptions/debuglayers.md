# debugLayers

**Framework**: ML Compute  
**Kind**: property

The option to debug layers during graph compilation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
static var debugLayers: MLCGraphCompilationOptions { get }
```

#### Discussion

Include this option to disable various optimizations such as layer fusion, and ensure the framework synchronizes the resulting forward and gradients tensors host memory with device memory, for layers marked as debuggable.

## See Also

- [init(rawValue: UInt64)](mlcgraphcompilationoptions/init(rawvalue:).md)
  Creates a graph compilation option with the specified raw value.
- [static var disableLayerFusion: MLCGraphCompilationOptions](mlcgraphcompilationoptions/disablelayerfusion.md)
  The option to disable layer fusion during graph compilation.
- [static var linkGraphs: MLCGraphCompilationOptions](mlcgraphcompilationoptions/linkgraphs.md)
  The option to link graphs during graph compilation.
- [static var computeAllGradients: MLCGraphCompilationOptions](mlcgraphcompilationoptions/computeallgradients.md)
  The option to compute all gradients during graph compilation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgraphcompilationoptions/debuglayers)*