---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/loadarrays(data:stream:)"
framework: "mlx-swift/MLX"
---

# loadArrays(data:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Load dictionary of [`MLXArray`](./mlxarray.md) from a `safetensors` `Data`.

## Declaration

```swift
func loadArrays(data: Data, stream: StreamOrDevice = .cpu) throws -> [String : MLXArray]
```

##### See Also

- [`saveToData(arrays:metadata:)`](./savetodata%28arrays,metadata%29.md)
- [`loadArraysAndMetadata(data:stream:)`](./loadarraysandmetadata%28data,stream%29.md)

## Parameters

- `data`: `Data` to load from
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/loadarrays(data:stream:))*