# ML Compute

**Framework**: ML Compute  
**Kind**: module

Accelerate training and validation of neural networks across the CPU and one or more GPUs.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

#### Overview

ML Compute uses high performance [`BNNS`](https://developer.apple.com/documentation/Accelerate/BNNS) primitives from the Accelerate framework for the CPU, and [`Metal Performance Shaders`](https://developer.apple.com/documentation/MetalPerformanceShaders) for the GPU.

## Topics

### Components
- [class MLCTensor](mlctensor.md)
  The data object you use throughout the framework.
- [class MLCPlatform](mlcplatform.md)
  A utility class for setting global properties in the framework.
- [Layers](layers.md)
  Create and inspect layers that encapsulate operations and configuration details to receive, process, and output tensors.
- [Training and Validation](training-and-validation.md)
  Create, train, and validate a graph to produce acceptable prediction results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/MLCompute)*