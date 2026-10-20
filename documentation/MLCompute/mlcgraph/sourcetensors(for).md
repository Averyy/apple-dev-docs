# sourceTensors(for:)

**Framework**: ML Compute  
**Kind**: method  
**Role**: Instance Method

Gets the source tensors for a layer in the training graph.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
func sourceTensors(for layer: MLCLayer) -> [MLCTensor]
```

```objc
- (NSArray<MLCTensor *> *) sourceTensorsForLayer:(MLCLayer *) layer;
```

#### Return Value

A list of source tensors.

## Parameters

- `layer`: A layer in the training graph.

## See Also

### Inspecting Graphs
- [func resultTensors(for: MLCLayer) -> [MLCTensor]](./resulttensors%28for%29.md)
  Gets the result tensors for a layer in the training graph.
- [var device: MLCDevice?](./device.md)
  The device you’ll use for compiling and executing a graph.
- [var layers: [MLCLayer]](./layers.md)
  An array that contains the layers in the graph.
- [var summarizedDOTDescription: String](./summarizeddotdescription.md)
  A DOT representation of the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgraph/sourcetensors(for:))*