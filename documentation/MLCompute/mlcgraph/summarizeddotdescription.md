# summarizedDOTDescription

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

A DOT representation of the graph.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var summarizedDOTDescription: String { get }
```

```objc
@property (nonatomic, readonly) NSString * summarizedDOTDescription;
```

## Discussion

Edges with solid lines indicate layers whose gradients the framework backpropagates through those edges. Edges with dashed lines indicate layers whose gradients the framework doesn’t backpropagate.

## See Also

### Inspecting Graphs
- [func sourceTensors(for: MLCLayer) -> [MLCTensor]](./sourcetensors%28for%29.md)
  Gets the source tensors for a layer in the training graph.
- [func resultTensors(for: MLCLayer) -> [MLCTensor]](./resulttensors%28for%29.md)
  Gets the result tensors for a layer in the training graph.
- [var device: MLCDevice?](./device.md)
  The device you’ll use for compiling and executing a graph.
- [var layers: [MLCLayer]](./layers.md)
  An array that contains the layers in the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgraph/summarizeddotdescription)*