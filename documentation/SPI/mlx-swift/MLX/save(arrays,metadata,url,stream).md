---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/save(arrays:metadata:url:stream:)"
framework: "mlx-swift/MLX"
---

# save(arrays:metadata:url:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Save dictionary of arrays in `safetensors` format.

## Declaration

```swift
func save(arrays: [String : MLXArray], metadata: [String : String] = [:], url: URL, stream: StreamOrDevice = .default) throws
```

## Mentions

- [Converting From Python](./converting-python.md)
- [Lazy Evaluation](./lazy-evaluation.md)

### See Also

- [`save(arrays:metadata:url:stream:)`](./save%28arrays,metadata,url,stream%29.md)
- [`loadArray(url:stream:)`](./loadarray%28url,stream%29.md)
- [`loadArrays(url:stream:)`](./loadarrays%28url,stream%29.md)

## Parameters

- `arrays`: Array to save
- `metadata`: Metadata to save
- `url`: URL of file to load
- `stream`: Stream or device to evaluate on

## See Also

### I/O
- [func loadArray(url: URL, stream: StreamOrDevice) throws -> MLXArray](./loadarray%28url,stream%29.md)
  Load array from a binary file in `.npy` format.
- [func loadArrays(url: URL, stream: StreamOrDevice) throws -> [String : MLXArray]](./loadarrays%28url,stream%29.md)
  Load dictionary of [`MLXArray`](./mlxarray.md) from a `safetensors` file.
- [func loadArraysAndMetadata(url: URL, stream: StreamOrDevice) throws -> ([String : MLXArray], [String : String])](./loadarraysandmetadata%28url,stream%29.md)
  Load dictionary of [`MLXArray`](./mlxarray.md) and metadata `[String:String]` from a `safetensors` file.
- [func save(array: MLXArray, url: URL, stream: StreamOrDevice) throws](./save%28array,url,stream%29.md)
  Save array to a binary file in `.npy` format.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/save(arrays:metadata:url:stream:))*