---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/savetodata(arrays:metadata:)"
framework: "mlx-swift/MLX"
---

# saveToData(arrays:metadata:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Save dictionary of arrays in `safetensors` format into `Data`.

## Declaration

```swift
func saveToData(arrays: [String : MLXArray], metadata: [String : String] = [:]) throws -> Data
```

##### See Also

- [`save(arrays:metadata:url:stream:)`](./save%28arrays,metadata,url,stream%29.md)
- [`loadArrays(data:stream:)`](./loadarrays%28data,stream%29.md)
- [`loadArraysAndMetadata(data:stream:)`](./loadarraysandmetadata%28data,stream%29.md)

## Parameters

- `arrays`: Arrays to save
- `metadata`: Metadata to save


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/savetodata(arrays:metadata:))*