# init(graphObjects:lossLayer:optimizer:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a training graph with the layers from the graph objects, loss layer, and optimizer you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init(graphObjects: [MLCGraph], lossLayer: MLCLayer?, optimizer: MLCOptimizer?)
```

```objc
+ (instancetype) graphWithGraphObjects:(NSArray<MLCGraph *> *) graphObjects lossLayer:(MLCLayer *) lossLayer optimizer:(MLCOptimizer *) optimizer;
```

#### Discussion

You can also add a loss layer to a training graph using the [`node(with:sources:lossLabels:)`](../mlcgraph/node%28with,sources,losslabels%29.md) method.

## Parameters

- `graphObjects`: The graph objects whose layers you add to the training graph.
- `lossLayer`: The loss layer.
- `optimizer`: The optimizer.

## See Also

### Creating Training Graphs
- [Optimizers](../optimizers.md)
  Create an optimizer to use with the training graph.
- [class MLCTensorParameter](../mlctensorparameter.md)
  A tensor parameter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctraininggraph/init(graphobjects:losslayer:optimizer:))*