---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxfast/metalkernel(name:inputnames:outputnames:source:header:ensurerowcontiguous:atomicoutputs:)"
framework: "mlx-swift/MLX"
---

# metalKernel(name:inputNames:outputNames:source:header:ensureRowContiguous:atomicOutputs:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

A jit-compiled custom Metal kernel defined from a source string.

## Declaration

```swift
static func metalKernel(name: String, inputNames: some Sequence<String>, outputNames: some Sequence<String>, source: String, header: String = "", ensureRowContiguous: Bool = true, atomicOutputs: Bool = false) -> MLXFast.MLXFastKernel
```

#### Return Value

An [`MLXFast.MLXFastKernel`](./mlxfastkernel.md) – see that for information on how to call it

## Parameters

- `name`: Name for the kernel
- `inputNames`: Parameter names of the inputs in the function signature
- `outputNames`: Parameter names of the outputs in the function signature
- `source`: Source code – this is the body of a function in Metal, the function signature will be automatically generated.
- `header`: Header source code to include before the main function.  Useful for helper functions or includes that should live outside of the main function body.
- `ensureRowContiguous`: Whether to ensure the inputs are row contiguous before the kernel runs (at a performance cost)
- `atomicOutputs`: Whether to use atomic outputs in the function signature, e.g. `device atomic<float>`


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxfast/metalkernel(name:inputnames:outputnames:source:header:ensurerowcontiguous:atomicoutputs:))*