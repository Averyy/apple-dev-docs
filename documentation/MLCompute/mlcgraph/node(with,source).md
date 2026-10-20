# node(with:source:)

**Framework**: ML Compute  
**Kind**: method  
**Role**: Instance Method

Adds the layer and source tensor that you specify to the graph.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
func node(with layer: MLCLayer, source: MLCTensor) -> MLCTensor?
```

```objc
- (MLCTensor *) nodeWithLayer:(MLCLayer *) layer source:(MLCTensor *) source;
```

#### Return Value

A result tensor.

## Parameters

- `layer`: The layer.
- `source`: The source tensor.

## See Also

### Adding Layers to Graphs
- [func node(with: MLCLayer, sources: [MLCTensor]) -> MLCTensor?](./node%28with,sources%29.md)
  Adds the layer and source tensors that you specify to the graph.
- [func node(with: MLCLayer, sources: [MLCTensor], disableUpdate: Bool) -> MLCTensor?](./node%28with,sources,disableupdate%29.md)
  Adds the layer, source tensors, and option to disable optimizer updates that you specify to the graph.
- [func node(with: MLCLayer, sources: [MLCTensor], lossLabels: [MLCTensor]) -> MLCTensor?](./node%28with,sources,losslabels%29.md)
  Adds the layer, sources, and loss labels tensors that you specify to the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgraph/node(with:source:))*