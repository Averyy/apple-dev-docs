---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxdistributed/initialize(backend:strict:)"
framework: "mlx-swift/MLX"
---

# initialize(backend:strict:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Initialize the distributed backend and return the global group.

## Declaration

```swift
@discardableResult
static func initialize(backend: MLXDistributed.Backend = .any, strict: Bool = false) throws -> MLXDistributed.Group
```

## Return Value

The global group

## Discussion

If no backend is configured and `strict` is `false` this returns a group of size one, in which the collectives return their input unchanged, so the same code also runs as a single process.  Forming a real group waits for the other processes to connect.

Throws if the backend cannot be initialized: when `strict` is `true` and no backend is configured, and – even when `strict` is `false` – when a backend is configured but cannot form its group, e.g. the ring backend with a malformed `MLX_HOSTFILE`.

MLX caches the group for each backend for the life of the process, including the group of size one that a non-strict call falls back to, and a later strict call for that backend returns the cached group instead of throwing.  A non-strict [`MLXDistributed.Backend.any`](./backend/any.md) that finds no backend caches its fallback under [`MLXDistributed.Backend.jaccl`](./backend/jaccl.md).  Initialize strictly before anything else initializes the backend.

## Parameters

- `backend`: The backend to use, defaulting to [`MLXDistributed.Backend.any`](./backend/any.md)
- `strict`: If `true`, throw rather than fall back to a group of size one when no backend can be initialized


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxdistributed/initialize(backend:strict:))*