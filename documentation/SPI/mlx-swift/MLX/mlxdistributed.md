---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxdistributed"
framework: "mlx-swift/MLX"
---

# MLXDistributed

**Framework**: mlx-swift/MLX  
**Kind**: enum  
**Role**: Enumeration

Communication operations for running MLX across multiple processes.

## Declaration

```swift
enum MLXDistributed
```

## Overview

This mirrors `mlx.core.distributed` in the Python API.

Forming a group can fail as soon as it is attempted, so [`initialize(backend:strict:)`](./mlxdistributed/initialize%28backend,strict%29.md) and [`split(color:key:)`](./mlxdistributed/group/split%28color,key%29.md) throw.

The collectives and the point to point operations are lazy like every other MLX operation.  Invalid arguments – e.g. sending in a group of size one – are reported when the operation is created, and communication failures when its result is evaluated.  Use [`withError(_:)`](./witherror%28_%29-2wfiu.md) and [`checkedEval(_:)`](./checkedeval%28_%29-7a4cs.md) to receive either as a Swift error:

```swift
let group = try MLXDistributed.initialize(strict: true)
try withError {
    let sum = MLXDistributed.allSum(x, group: group)
    try checkedEval(sum)
}
```

Every operation evaluates on the CPU stream by default, which is where the ring, JACCL and MPI backends communicate.  NCCL, available only in a CUDA build, communicates on the GPU, so pass `stream: .gpu` for an NCCL group.

Every process must create *and evaluate* these operations in the same order.  They are lazy, so the communication happens where the result is evaluated: evaluating two collectives in one order in one process and in the other order in another makes the processes exchange mismatched buffers rather than report an error.  Beware of iterating a `Dictionary`, whose order differs from process to process.

## Topics

### Classes
- [MLXDistributed.Group](./mlxdistributed/group.md)
  A group of independent MLX processes that can communicate.
### Type Methods
- [static func allGather(MLXArray, group: MLXDistributed.Group?, stream: StreamOrDevice) -> MLXArray](./mlxdistributed/allgather%28_,group,stream%29.md)
  Gather arrays from all processes, concatenating along the first axis.
- [static func allMax(MLXArray, group: MLXDistributed.Group?, stream: StreamOrDevice) -> MLXArray](./mlxdistributed/allmax%28_,group,stream%29.md)
  All reduce max.
- [static func allMin(MLXArray, group: MLXDistributed.Group?, stream: StreamOrDevice) -> MLXArray](./mlxdistributed/allmin%28_,group,stream%29.md)
  All reduce min.
- [static func allSum(MLXArray, group: MLXDistributed.Group?, stream: StreamOrDevice) -> MLXArray](./mlxdistributed/allsum%28_,group,stream%29.md)
  All reduce sum.
- [static func initialize(backend: MLXDistributed.Backend, strict: Bool) throws -> MLXDistributed.Group](./mlxdistributed/initialize%28backend,strict%29.md)
  Initialize the distributed backend and return the global group.
- [static func isAvailable(MLXDistributed.Backend) -> Bool](./mlxdistributed/isavailable%28_%29.md)
  Check if a communication backend is available.
- [static func recv([Int], dtype: DType, from: Int, group: MLXDistributed.Group?, stream: StreamOrDevice) -> MLXArray](./mlxdistributed/recv%28_,dtype,from,group,stream%29.md)
  Receive an array with the given shape and type from the process with rank `src`.
- [static func recvLike(MLXArray, from: Int, group: MLXDistributed.Group?, stream: StreamOrDevice) -> MLXArray](./mlxdistributed/recvlike%28_,from,group,stream%29.md)
  Receive an array with the same shape and type as `x` from the process with rank `src`.
- [static func send(MLXArray, to: Int, group: MLXDistributed.Group?, stream: StreamOrDevice) -> MLXArray](./mlxdistributed/send%28_,to,group,stream%29.md)
  Send `x` to the process with rank `dst`.
- [static func sumScatter(MLXArray, group: MLXDistributed.Group?, stream: StreamOrDevice) -> MLXArray](./mlxdistributed/sumscatter%28_,group,stream%29.md)
  Sum `x` across the group and shard the result along the first axis.
### Enumerations
- [MLXDistributed.Backend](./mlxdistributed/backend.md)
  A communication backend.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxdistributed)*