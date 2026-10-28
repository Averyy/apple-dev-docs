---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/loadarray(url:stream:)"
framework: "mlx-swift/MLX"
---

# loadArray(url:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Load array from a binary file in `.npy` format.

## Declaration

```swift
func loadArray(url: URL, stream: StreamOrDevice = .cpu) throws -> MLXArray
```

## Mentions

- [Converting From Python](./converting-python.md)

### See Also

- [`loadArrays(url:stream:)`](./loadarrays%28url,stream%29.md)
- [`save(array:url:stream:)`](./save%28array,url,stream%29.md)
- [`save(arrays:metadata:url:stream:)`](./save%28arrays,metadata,url,stream%29.md)

## Parameters

- `url`: URL of file to load
- `stream`: Stream or device to evaluate on

## See Also

### I/O
- [func loadArrays(url: URL, stream: StreamOrDevice) throws -> [String : MLXArray]](./loadarrays%28url,stream%29.md)
  Load dictionary of [`MLXArray`](./mlxarray.md) from a `safetensors` file.
- [func loadArraysAndMetadata(url: URL, stream: StreamOrDevice) throws -> ([String : MLXArray], [String : String])](./loadarraysandmetadata%28url,stream%29.md)
  Load dictionary of [`MLXArray`](./mlxarray.md) and metadata `[String:String]` from a `safetensors` file.
- [func save(array: MLXArray, url: URL, stream: StreamOrDevice) throws](./save%28array,url,stream%29.md)
  Save array to a binary file in `.npy` format.
- [func save(arrays: [String : MLXArray], metadata: [String : String], url: URL, stream: StreamOrDevice) throws](./save%28arrays,metadata,url,stream%29.md)
  Save dictionary of arrays in `safetensors` format.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/loadarray(url:stream:))*