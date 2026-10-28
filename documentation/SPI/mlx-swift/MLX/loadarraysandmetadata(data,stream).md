---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/loadarraysandmetadata(data:stream:)"
framework: "mlx-swift/MLX"
---

# loadArraysAndMetadata(data:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Load dictionary of [`MLXArray`](./mlxarray.md) and metadata from a `safetensors` `Data`.

## Declaration

```swift
func loadArraysAndMetadata(data: Data, stream: StreamOrDevice = .cpu) throws -> ([String : MLXArray], [String : String])
```

### See Also

- [`saveToData(arrays:metadata:)`](./savetodata%28arrays,metadata%29.md)
- [`loadArrays(data:stream:)`](./loadarrays%28data,stream%29.md)

## Parameters

- `data`: `Data` to load from
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/loadarraysandmetadata(data:stream:))*