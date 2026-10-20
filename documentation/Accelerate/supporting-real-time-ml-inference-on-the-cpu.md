# Supporting real-time ML inference on the CPU

**Framework**: Accelerate  
**Role**: Sample Code  
**Download**: [SupportingRealTimeMLInferenceOnTheCPU.zip](https://docs-assets.developer.apple.com/published/a39fb3b0a5f6/SupportingRealTimeMLInferenceOnTheCPU.zip)

Add real-time digital signal processing to apps like Logic Pro X and GarageBand with the BNNS Graph API.

**Availability**:
- macOS 26.0+
- Xcode 26.0+

#### Overview

> **Note**: This sample code project is associated with WWDC25 session 276: [What’s new in BNNSGraph](https://developer.apple.com/videos/play/wwdc2025/276).

## See Also

### Building graphs in Swift
- [static func makeContext(options: BNNSGraph.CompileOptions, (inout BNNSGraph.Builder) -> [any BNNSGraph.TensorDescriptor]) throws -> BNNSGraph.Context](./bnnsgraph/makecontext%28options,_%29.md)
  Returns a new context that wraps a graph object that the given closure defines.
- [BNNSGraph.Builder](./bnnsgraph/builder.md)
  A structure thats provides a closure you can use to define the arguments and operations of a BNNS Graph.
- [BNNSGraph.Builder.Tensor](./bnnsgraph/builder/tensor.md)
  A structure that represents an abstract handle to a tensor that you use within a `BNNSGraph.makeContext` closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/supporting-real-time-ml-inference-on-the-cpu)*