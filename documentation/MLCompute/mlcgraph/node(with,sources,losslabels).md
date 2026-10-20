# node(with:sources:lossLabels:)

**Framework**: ML Compute  
**Kind**: method

Adds the layer, sources, and loss labels tensors that you specify to the graph.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
func node(with layer: MLCLayer, sources: [MLCTensor], lossLabels: [MLCTensor]) -> MLCTensor?
```

#### Return Value

A result tensor.

## Parameters

- `layer`: The layer.
- `sources`: An array that contains the source tensors.
- `lossLabels`: An array that contains the loss labels tensors.

## See Also

- [func node(with: MLCLayer, source: MLCTensor) -> MLCTensor?](mlcgraph/node(with:source:).md)
  Adds the layer and source tensor that you specify to the graph.
- [func node(with: MLCLayer, sources: [MLCTensor]) -> MLCTensor?](mlcgraph/node(with:sources:).md)
  Adds the layer and source tensors that you specify to the graph.
- [func node(with: MLCLayer, sources: [MLCTensor], disableUpdate: Bool) -> MLCTensor?](mlcgraph/node(with:sources:disableupdate:).md)
  Adds the layer, source tensors, and option to disable optimizer updates that you specify to the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgraph/node(with:sources:losslabels:))*