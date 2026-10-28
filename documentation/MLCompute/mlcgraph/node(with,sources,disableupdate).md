# node(with:sources:disableUpdate:)

**Framework**: ML Compute  
**Kind**: method  
**Role**: Instance Method

Adds the layer, source tensors, and option to disable optimizer updates that you specify to the graph.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
func node(with layer: MLCLayer, sources: [MLCTensor], disableUpdate: Bool) -> MLCTensor?
```

```objc
- (MLCTensor *) nodeWithLayer:(MLCLayer *) layer sources:(NSArray<MLCTensor *> *) sources disableUpdate:(BOOL) disableUpdate;
```

## Return Value

A result tensor.

## Parameters

- `layer`: The layer.
- `sources`: An array that contains the source tensors.
- `disableUpdate`: A Boolean that indicates whether you choose to disable the optimizer updates for this layer.

## See Also

### Adding Layers to Graphs
- [func node(with: MLCLayer, source: MLCTensor) -> MLCTensor?](./node%28with,source%29.md)
  Adds the layer and source tensor that you specify to the graph.
- [func node(with: MLCLayer, sources: [MLCTensor]) -> MLCTensor?](./node%28with,sources%29.md)
  Adds the layer and source tensors that you specify to the graph.
- [func node(with: MLCLayer, sources: [MLCTensor], lossLabels: [MLCTensor]) -> MLCTensor?](./node%28with,sources,losslabels%29.md)
  Adds the layer, sources, and loss labels tensors that you specify to the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgraph/node(with:sources:disableupdate:))*