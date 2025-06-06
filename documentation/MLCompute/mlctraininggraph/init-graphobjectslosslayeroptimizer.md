# init(graphObjects:lossLayer:optimizer:)

**Framework**: ML Compute  
**Kind**: init

Creates a training graph with the layers from the graph objects, loss layer, and optimizer you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init(graphObjects: [MLCGraph], lossLayer: MLCLayer?, optimizer: MLCOptimizer?)
```

#### Discussion

You can also add a loss layer to a training graph using the [`node(with:sources:lossLabels:)`](mlcgraph/node(with:sources:losslabels:).md) method.

## Parameters

- `graphObjects`: The graph objects whose layers you add to the training graph.
- `lossLayer`: The loss layer.
- `optimizer`: The optimizer.

## See Also

- [Optimizers](optimizers.md)
  Create an optimizer to use with the training graph.
- [class MLCTensorParameter](mlctensorparameter.md)
  A tensor parameter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctraininggraph/init(graphobjects:losslayer:optimizer:))*