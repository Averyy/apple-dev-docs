# device

**Framework**: ML Compute  
**Kind**: property

The device you’ll use for compiling and executing a graph.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
var device: MLCDevice? { get }
```

## See Also

- [func sourceTensors(for: MLCLayer) -> [MLCTensor]](mlcgraph/sourcetensors(for:).md)
  Gets the source tensors for a layer in the training graph.
- [func resultTensors(for: MLCLayer) -> [MLCTensor]](mlcgraph/resulttensors(for:).md)
  Gets the result tensors for a layer in the training graph.
- [var layers: [MLCLayer]](mlcgraph/layers.md)
  An array that contains the layers in the graph.
- [var summarizedDOTDescription: String](mlcgraph/summarizeddotdescription.md)
  A DOT representation of the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgraph/device)*