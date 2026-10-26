---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxfast/mlxfastkernel"
framework: "mlx-swift/MLX"
---

# MLXFast.MLXFastKernel

**Framework**: mlx-swift/MLX  
**Kind**: class  
**Role**: Class

Container for a kernel created by [`callAsFunction(_:template:grid:threadGroup:outputShapes:outputDTypes:initValue:verbose:stream:)`](./mlxfastkernel/callasfunction%28_,template,grid,threadgroup,outputshapes,outputdtypes,initvalue,verbose,stream%29.md)

## Declaration

```swift
final class MLXFastKernel
```

#### Overview

The [`callAsFunction(_:template:grid:threadGroup:outputShapes:outputDTypes:initValue:verbose:stream:)`](./mlxfastkernel/callasfunction%28_,template,grid,threadgroup,outputshapes,outputdtypes,initvalue,verbose,stream%29.md) can be used to evaluate the kernel with inputs:

```swift
let a = normal([2, 2])
let kernel = MLXFast.metalKernel(
    name: "basic",
    inputNames: ["a"],
    outputNames: ["out1"],
    source: """
        uint elem = thread_position_in_grid.x;
        out1[elem] = a[elem];
    """,
    grid: (4, 1, 1),
    threadGroup: (2, 1, 1),
    outputShapes: [[2, 2]],
    outputDTypes: [.float32])

let out = kernel([a])
```

## Topics

### Instance Properties
- [let outputNames: [String]](./mlxfastkernel/outputnames.md)
### Instance Methods
- [func callAsFunction([any ScalarOrArray], template: [(String, any KernelTemplateArg)]?, grid: (Int, Int, Int), threadGroup: (Int, Int, Int), outputShapes: some Sequence<Array<Int>>, outputDTypes: some Sequence<DType>, initValue: Float?, verbose: Bool, stream: StreamOrDevice) -> [MLXArray]](./mlxfastkernel/callasfunction%28_,template,grid,threadgroup,outputshapes,outputdtypes,initvalue,verbose,stream%29.md)
  Call the prepared metal kernel.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxfast/mlxfastkernel)*