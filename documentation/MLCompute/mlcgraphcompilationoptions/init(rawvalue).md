# init(rawValue:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a graph compilation option with the specified raw value.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
init(rawValue: UInt64)
```

## Parameters

- `rawValue`: The bitmask raw value.

## See Also

### Creating Graph Compilation Options
- [static var debugLayers: MLCGraphCompilationOptions](./debuglayers.md)
  The option to debug layers during graph compilation.
- [static var disableLayerFusion: MLCGraphCompilationOptions](./disablelayerfusion.md)
  The option to disable layer fusion during graph compilation.
- [static var linkGraphs: MLCGraphCompilationOptions](./linkgraphs.md)
  The option to link graphs during graph compilation.
- [static var computeAllGradients: MLCGraphCompilationOptions](./computeallgradients.md)
  The option to compute all gradients during graph compilation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgraphcompilationoptions/init(rawvalue:))*