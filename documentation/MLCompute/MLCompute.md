# ML Compute

**Framework**: ML Compute  
**Kind**: module  
**Role**: Framework

Accelerate training and validation of neural networks across the CPU and one or more GPUs.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

> **Deprecated**: ML Compute is deprecated. Instead, use [`BNNS`](../Accelerate/bnns.md) for CPU tasks, [Metal Performance Shaders](../MetalPerformanceShaders/MetalPerformanceShaders.md) for GPU work, and [Core ML](../CoreML/CoreML.md) for tensor APIs.

## Overview

ML Compute uses high performance [`BNNS`](../Accelerate/bnns.md) primitives from the Accelerate framework for the CPU, and [Metal Performance Shaders](../MetalPerformanceShaders/MetalPerformanceShaders.md) for the GPU.

## Topics

### Components
- [class MLCTensor](./mlctensor.md)
  The data object you use throughout the framework.
- [class MLCPlatform](./mlcplatform.md)
  A utility class for setting global properties in the framework.
- [Layers](./layers.md)
  Create and inspect layers that encapsulate operations and configuration details to receive, process, and output tensors.
- [Training and Validation](./training-and-validation.md)
  Create, train, and validate a graph to produce acceptable prediction results.
### Macros
- [MLCOMPUTE_AVAILABLE_STARTING](./mlcompute_available_starting.md)
- [MLCOMPUTE_AVAILABLE_STARTING_BUT_DEPRECATED](./mlcompute_available_starting_but_deprecated.md)
- [MLCOMPUTE_AVAILABLE_STARTING_BUT_DEPRECATED_MACOS14](./mlcompute_available_starting_but_deprecated_macos14.md)
- [MLCOMPUTE_CLASS_AVAILABLE_STARTING](./mlcompute_class_available_starting.md)
- [MLCOMPUTE_ENUM_AVAILABLE_STARTING](./mlcompute_enum_available_starting.md)
- [MLCOMPUTE_ENUM_AVAILABLE_STARTING_BUT_DEPRECATED](./mlcompute_enum_available_starting_but_deprecated.md)
- [MLCOMPUTE_PROTOCOL_AVAILABLE_STARTING](./mlcompute_protocol_available_starting.md)
- [MLCOMPUTE_UNAVAILABLE](./mlcompute_unavailable.md)
- [MLComputeTypes_h](./mlcomputetypes_h.md)
### Enumerations
- [MLCPaddingPolicy](./mlcpaddingpolicy-14ba7.md)
  A padding policy that you specify for a convolution or pooling layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/MLCompute)*