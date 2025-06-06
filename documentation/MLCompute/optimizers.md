# Optimizers

**Framework**: ML Compute

Create an optimizer to use with the training graph.

## Topics

### Optimizer Types
- [class MLCSGDOptimizer](mlcsgdoptimizer.md)
  An optimizer that represents the stochastic gradient decent algorithm.
- [class MLCRMSPropOptimizer](mlcrmspropoptimizer.md)
  An optimizer that represents the root mean square propagation algorithm.
- [class MLCAdamOptimizer](mlcadamoptimizer.md)
  An optimizer that represents the adaptive moment estimation algorithm.
- [class MLCAdamWOptimizer](mlcadamwoptimizer.md)
  An optimizer that represents the Adam algorithm with weight decay.
- [class MLCOptimizer](mlcoptimizer.md)
  The base class for all framework optimizers.
### Supporting Types
- [class MLCOptimizerDescriptor](mlcoptimizerdescriptor.md)
  A configuration object you use to create an optimizer.
- [enum MLCRegularizationType](mlcregularizationtype.md)
  A regularization function to use with an optimizer.

## See Also

- [convenience init(graphObjects: [MLCGraph], lossLayer: MLCLayer?, optimizer: MLCOptimizer?)](mlctraininggraph/init(graphobjects:losslayer:optimizer:).md)
  Creates a training graph with the layers from the graph objects, loss layer, and optimizer you specify.
- [class MLCTensorParameter](mlctensorparameter.md)
  A tensor parameter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/optimizers)*