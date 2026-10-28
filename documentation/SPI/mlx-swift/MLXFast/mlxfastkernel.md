---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxfast/mlxfastkernel"
framework: "mlx-swift/MLXFast"
---

# MLXFastKernel

**Framework**: mlx-swift/MLXFast  
**Kind**: typealias  
**Role**: Type Alias

Container for a kernel created by [`metalKernel(name:inputNames:outputNames:source:header:ensureRowContiguous:atomicOutputs:)`](./metalkernel%28name,inputnames,outputnames,source,header,ensurerowcontiguous,atomicoutputs%29.md)

## Declaration

```swift
typealias MLXFastKernel = MLXFast.MLXFastKernel
```

## Discussion

The [`MLXFastKernel`](./mlxfastkernel.md) can be used to evaluate the kernel with inputs:

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


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxfast/mlxfastkernel)*