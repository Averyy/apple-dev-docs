# summarizedDOTDescription

**Framework**: ML Compute  
**Kind**: property

A DOT representation of the graph.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
var summarizedDOTDescription: String { get }
```

#### Discussion

Edges with solid lines indicate layers whose gradients the framework backpropagates through those edges. Edges with dashed lines indicate layers whose gradients the framework doesn’t backpropagate.

## See Also

- [func sourceTensors(for: MLCLayer) -> [MLCTensor]](mlcgraph/sourcetensors(for:).md)
  Gets the source tensors for a layer in the training graph.
- [func resultTensors(for: MLCLayer) -> [MLCTensor]](mlcgraph/resulttensors(for:).md)
  Gets the result tensors for a layer in the training graph.
- [var device: MLCDevice?](mlcgraph/device.md)
  The device you’ll use for compiling and executing a graph.
- [var layers: [MLCLayer]](mlcgraph/layers.md)
  An array that contains the layers in the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgraph/summarizeddotdescription)*