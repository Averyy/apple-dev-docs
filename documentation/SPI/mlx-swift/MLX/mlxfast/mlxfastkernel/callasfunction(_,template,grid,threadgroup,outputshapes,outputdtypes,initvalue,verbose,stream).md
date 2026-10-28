---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxfast/mlxfastkernel/callasfunction(_:template:grid:threadgroup:outputshapes:outputdtypes:initvalue:verbose:stream:)"
framework: "mlx-swift/MLX"
---

# callAsFunction(_:template:grid:threadGroup:outputShapes:outputDTypes:initValue:verbose:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Call the prepared metal kernel.

## Declaration

```swift
func callAsFunction(_ inputs: [any ScalarOrArray], template: [(String, any KernelTemplateArg)]? = nil, grid: (Int, Int, Int), threadGroup: (Int, Int, Int), outputShapes: some Sequence<Array<Int>>, outputDTypes: some Sequence<DType>, initValue: Float? = nil, verbose: Bool = false, stream: StreamOrDevice = .default) -> [MLXArray]
```

## Return Value

Array of `MLXArray`

## Discussion

See [`MLXFast.MLXFastKernel`](../mlxfastkernel.md) for example.  Use [`metalKernel(name:inputNames:outputNames:source:header:ensureRowContiguous:atomicOutputs:)`](../metalkernel%28name,inputnames,outputnames,source,header,ensurerowcontiguous,atomicoutputs%29.md) to create an instance.

## Parameters

- `inputs`: Inputs passed to the metal kernel
- `template`: Template arguments
- `grid`: 3-tuple specifying the grid to launch the kernel with
- `threadGroup`: 3-tuple specifying the threadgroup size to use
- `outputShapes`: List of shapes for each output in [`outputNames`](./outputnames.md)
- `outputDTypes`: List of data types for each output in [`outputNames`](./outputnames.md)
- `initValue`: Optional value to use to initialize all of the output arrays
- `verbose`: If true will print the full generated source code of the kernel when run
- `stream`: Stream to run on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxfast/mlxfastkernel/callasfunction(_:template:grid:threadgroup:outputshapes:outputdtypes:initvalue:verbose:stream:))*