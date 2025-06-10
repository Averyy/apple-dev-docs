# Supporting real-time ML inference on the CPU

**Framework**: Accelerate

Add real-time digital signal processing to apps like Logic Pro X and GarageBand with the BNNS Graph API.

**Availability**:
- macOS 26.0+ (Beta)
- Xcode 26.0+ (Beta)

#### Overview

> **Note**: This sample code project is associated with WWDC25 session 276: [`What’s new in BNNSGraph`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2025/276).

## See Also

- [static func makeContext(options: BNNSGraph.CompileOptions, (inout BNNSGraph.Builder) -> [any BNNSGraph.TensorDescriptor]) throws -> BNNSGraph.Context](bnnsgraph/makecontext(options:_:).md)
  Returns a new context that wraps a graph object that the given closure defines.
- [BNNSGraph.Builder](bnnsgraph/builder.md)
  A structure thats provides a closure you can use to define the arguments and operations of a BNNS Graph.
- [BNNSGraph.Builder.Tensor](bnnsgraph/builder/tensor.md)
  A structure that represents an abstract handle to a tensor that you use within a `BNNSGraph.makeContext` closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/supporting-real-time-ml-inference-on-the-cpu)*