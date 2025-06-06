# Training and Validation

**Framework**: ML Compute

Create, train, and validate a graph to produce acceptable prediction results.

## Topics

### Devices
- [class MLCDevice](mlcdevice.md)
  An object that represents the CPU or one or more GPUs the framework uses to execute a neural network.
### Graphs
- [class MLCGraph](mlcgraph.md)
  A graph of layers you use to build a training or inference graph.
- [class MLCTrainingGraph](mlctraininggraph.md)
  A training graph that you create from one or more graph objects plus additional layers you add directly to the training graph.
- [class MLCInferenceGraph](mlcinferencegraph.md)
  An inference graph created from one or more MLCGraph instances plus additional layers added directly to the inference graph.

## See Also

- [class MLCTensor](mlctensor.md)
  The data object you use throughout the framework.
- [class MLCPlatform](mlcplatform.md)
  A utility class for setting global properties in the framework.
- [Layers](layers.md)
  Create and inspect layers that encapsulate operations and configuration details to receive, process, and output tensors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/training-and-validation)*