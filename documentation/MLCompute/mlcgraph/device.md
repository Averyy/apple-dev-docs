# device

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The device you’ll use for compiling and executing a graph.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var device: MLCDevice? { get }
```

```objc
@property (nonatomic, retain, readonly, nullable) MLCDevice * device;
```

## See Also

### Inspecting Graphs
- [func sourceTensors(for: MLCLayer) -> [MLCTensor]](./sourcetensors%28for%29.md)
  Gets the source tensors for a layer in the training graph.
- [func resultTensors(for: MLCLayer) -> [MLCTensor]](./resulttensors%28for%29.md)
  Gets the result tensors for a layer in the training graph.
- [var layers: [MLCLayer]](./layers.md)
  An array that contains the layers in the graph.
- [var summarizedDOTDescription: String](./summarizeddotdescription.md)
  A DOT representation of the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgraph/device)*